//! rustc my_ls.rs && ./my_ls -lah

use std::fs;
use std::env;
use std::fmt;
use std::ffi::OsStr;
use chrono::{DateTime, Utc};
use std::os::unix::fs::MetadataExt;

#[derive(Debug)]
struct LongFormatAttributes {
    ftype_perms: String,
    hard_links: u64,
    owner_name: String,
    group_name: String,
    fsize_bytes: u64,
    last_mod_time: String,
    filename: String,
}

impl fmt::Display for LongFormatAttributes {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Use `self.number` to refer to each positional data point.
        write!(
            f, "{} {} {} {} {} {} {}",  
            self.ftype_perms, self.hard_links, self.owner_name, self.group_name, self.fsize_bytes, self.last_mod_time, self.filename)
    }
}


fn is_hidden_file(file_name: &OsStr) -> bool {
    
    let Some(filename_str) = file_name.to_str() else {
        return false;
    };
    filename_str.starts_with(".")    
}

fn convert_date(time: i64) -> String {
    let Some(datetime) = DateTime::from_timestamp(seconds, time) else {
        return "".to_string();
    };
    datetime.format("%H:%M:%S").to_string()
}


fn collect_folders(a_flag: bool, h_flag: bool, l_flag: bool) {
    // let results: Result<ReadDir> = fs::read_dir(".");
    // note that enum Result<T, E> { Ok(T), Err(E), }
    // Result.unwrap() = use result if Ok, else crash program

    let dirEntries = fs::read_dir(".").unwrap();
    // println!("{:?}", dirEntries); // This prints the ReadDir iterator
    for entry in dirEntries {
        let entry = entry.unwrap();

        let path = entry.path();
        let metadata = fs::metadata(&path).unwrap();
        
        if is_hidden_file(&entry.file_name()) && !a_flag {
            continue;
        }
        
        if !l_flag {
            println!("{}", entry.file_name().into_string().unwrap());
        } else {
            let long_format: LongFormatAttributes = LongFormatAttributes {
                ftype_perms:    metadata.mode(), //TODO fix to string instead of u32
                hard_links:     metadata.nlink(),
                owner_name:     metadata.uid(), //TODO get owner name instead of id
                group_name:     metadata.gid(), // TODO get group name instead of i
                fsize_bytes:    metadata.len(),
                last_mod_time:  convert_date(metadata.mtime()),
                filename:       (&entry.file_name().to_str().unwrap()).to_string(),           
            };

        }

     //   println!(
     //       "{} {} {} bytes {:?}",
     //       entry.file_name().into_string().unwrap(),
     //       path.display(),
     //       metadata.len(),
     //       metadata,
     //   );
    }
    // note: you cannot collect this: println!("uninplemented {:?}", dirEntries);
}

/**
 * Command line usage: 
 * Root folder to start from: assumes user is asking about current directory
 *
 * Flags -lah in any order, or none existent. 
 *  a = all = show hidden files
 *  h = human-readable
 *  l = long format = Show detailed information
 *    
*/ 
fn main() {
    let args: Vec<String> = env::args().collect();
    dbg!(&args);
    
    let flags: Vec<char> = args
    .iter()
    .skip(1)
    .flat_map(|arg| arg.trim_start_matches('-').chars())
    .collect();


    let a_flag : bool = flags.contains(&'a');
    let h_flag : bool = flags.contains(&'h');
    let l_flag : bool = flags.contains(&'l');

    // dbg!(a_flag,h_flag,l_flag);

    collect_folders(a_flag, h_flag, l_flag);
}
