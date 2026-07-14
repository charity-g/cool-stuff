
## Installation:
- Use the site: https://rust-lang.org/tools/install/
- install on WSL via
    `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`

## Toolchain management with `rustup`:
- Rust has 6 week releases
- update installation `rustup update`

In the Rust development environment:
- all tools are installed to the `~/.cargo/bin` directory
- contains all Rust toolchains ie: `rustc`, `cargo`, and `rustup`

### This is how rust tooling works:


```
Your code
    │
    ▼
Cargo (optional but recommended)
    │
    ▼
rustc (the compiler)
    │
    ▼
Executable
```

A crate is the smallest unit of compilation.
Whenever `rustc some_file.rs` is called, `some_file.rs` is treated as the crate file. If `some_file.rs` has mod declarations in it, then the contents of the module files would be inserted in places where mod declarations in the crate file are found, before running the compiler over it.

In other words, modules do not get compiled individually, only crates get compiled.

Two types of crates:
- Binary crates → produce an executable.
- Library crates → produce a library that other crates can use.
By default, rustc will produce a binary from a crate. This behavior can be overridden by passing the --crate-type flag to lib.


A crate is determined by the crate root (main.rs for a binary crate or lib.rs
for a library crate). Every module reachable from that root belongs to the same
crate.


## Vim learning:
- https://www.youtube.com/watch?v=JBKoBuuoF28&list=PLT98CRl2KxKHy4A5N70jMRYAROzzC2a6x&index=3




