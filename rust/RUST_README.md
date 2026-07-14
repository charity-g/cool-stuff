
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
Two types of crates:
- Binary crates → produce an executable.
- Library crates → produce a library that other crates can use.

A crate is determined by the crate root (main.rs for a binary crate or lib.rs
for a library crate). Every module reachable from that root belongs to the same
crate.


## Vim learning:
- https://www.youtube.com/watch?v=JBKoBuuoF28&list=PLT98CRl2KxKHy4A5N70jMRYAROzzC2a6x&index=3




