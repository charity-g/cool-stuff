// to create library
// > rustc --crate-type=lib rary.rs
// > ls lib*
// you will see `library.rlib`


// NOTE:
// - Libraries get prefixed with “lib”
// - by default they get named after their crate file
// - Can override above by passing --crate-name option to rustc or using crate_name attribute

pub fn public_function() {
    println!("called rary's `public_function()`");
}

fn private_function() {
    println!("called rary's `private_function()`");
}

pub fn indirect_access() {
    print!("called rary's `indirect_access()`, that\n> ");

    private_function();
}
