

// Rust program mostly made up of statements
// ie: variable bindings
// expression

fn statements() {
    // variable binding
    let x = 5;

    // expression;
    x;
    x + 1;
    15;
}

// Blocks are expressions too, so they can be used as values in assignments
fn blocks() {
    let x = 5u32;

    let y = {
        let x_squared = x * x;
        let x_cube = x_squared * x;

        // This expression will be assigned to `y`
        x_cube + x_squared + x
    };

    let z = {
        // The semicolon suppresses this expression and `()` is assigned to `z`
        2 * x;
    };

    println!("x is {:?}", x);
    println!("y is {:?}", y);
    println!("z is {:?}", z);
}

fn main() {
    // statements();
    blocks();
}
