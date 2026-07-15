//! rustc my_ls.rs && ./my_ls -lah
use std::env;
use std::fs;
use std::path::PathBuf;

fn is_hidden_path(path: &PathBuf) -> bool {
    // TODO
    println!("is_hidden_path is unimplemented");
    return true;
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
        
        if is_hidden_path(&path) && !a_flag {
            continue;
        }

        println!(
            "{} {} {} bytes {:?}",
            entry.file_name().into_string().unwrap(),
            path.display(),
            metadata.len(),
            metadata,
        );
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
