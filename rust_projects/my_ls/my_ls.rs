//! rustc my_ls.rs && ./my_ls -lah
use std::env;
    
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

    dbg!(a_flag,h_flag,l_flag);
}
