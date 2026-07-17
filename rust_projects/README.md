

## 1. File System Projects (Beginner → Intermediate)

### Build your own `ls`

Implement a simplified version of:

```bash
ls -lah
```

You'll learn:

* `std::fs`
* `Path` and `PathBuf`
* metadata
* permissions
* sorting
* unix specific imports
* directory traversal
* https://en.wikipedia.org/wiki/File-system_permissions#Read_(r)
* https://linuxize.com/post/how-to-list-files-in-linux-using-the-ls-command/#understanding-ls--al-and-long-format
---

### Build `find`

Example:

```bash
find ./src -name "*.rs"
```

Learn:

* recursive traversal
* iterators
* filtering
* recursion

---

### Disk Usage (`du`)

Compute folder sizes.

```bash
du -sh ./Downloads
```

Learn:

* recursive algorithms
* metadata
* handling symbolic links

---

### File Synchronizer

Like a tiny Dropbox.

```
Folder A
   ↓
Folder B
```

Features:

* compare timestamps
* compare hashes
* copy changed files
* delete stale files

This introduces hashing (`sha256`) and efficient I/O.

---

### Mini Git

Implement:

```
init
add
commit
status
```

You don't need branching initially.

You'll learn:

* hashing
* serialization
* object storage
* snapshots

This is one of the best Rust learning projects.

---

## 2. Networking Projects

### TCP Chat Server

Multiple clients connect.

```
Client A
     \
      \
    Server
      /
     /
Client B
```

Learn:

* `TcpListener`
* `TcpStream`
* threads
* synchronization

---

### HTTP Server

Like a tiny web server.

Handle:

```
GET /
GET /about
GET /index.html
```

Then later:

* POST
* routing
* static files

You'll understand HTTP deeply.

---

### HTTP Client

Implement something like

```bash
curl https://example.com
```

Learn:

* sockets
* parsing HTTP
* DNS
* TLS (later)

---

### FTP Server

Implement commands:

```
USER
PASS
LIST
RETR
STOR
```

Great protocol implementation exercise.

---

### DNS Resolver

Implement:

```
dig google.com
```

Learn:

* UDP
* binary protocols
* packet parsing

---

## 3. Protocol Projects

Protocols are fantastic in Rust because Rust excels at binary parsing.

### BitTorrent Client

Implement:

* bencoding
* peer discovery
* piece downloading
* hashing

Excellent intermediate project.

---

### SMTP Mail Server

Receive mail via

```
HELO
MAIL FROM
RCPT TO
DATA
```

---

### IRC Server

Classic networking project.

Supports:

```
JOIN
PART
PRIVMSG
```

Many tutorials exist for this.

---

### SSH Client (minimal)

Implement:

* TCP
* key exchange
* authentication

Much harder.

---

## 4. File System + Networking

These combine both areas.

### Dropbox Clone

```
Computer A
     |
Internet
     |
Computer B
```

Features:

* file watching
* hashing
* synchronization
* conflict resolution

---

### Network File System

Clients can

```
open()
read()
write()
```

over TCP.

Very educational.

---

### Distributed Key-Value Store

Think Redis.

```
SET name charity
GET name
```

Then add

* persistence
* networking
* replication

---

## 5. Compression

Implement

```
gzip
zip
tar
```

Learn:

* binary formats
* streams
* buffers

---

## 6. Databases

Implement

```
CREATE TABLE
INSERT
SELECT
```

Or simpler:

```
SET
GET
DELETE
```

Excellent way to learn storage engines.

---

# Real Rust Open Source Projects

Once you've built a few of these, reading real Rust code is extremely valuable. Some excellent projects include:

* Tokio — asynchronous runtime used by many network services.
* Hyper — HTTP implementation built on Tokio.
* Axum — web framework demonstrating modern async Rust.
* Tantivy — search engine with interesting file and indexing code.
* Redox OS — an operating system written largely in Rust.
* BorgBackup — backup and deduplication concepts (though the main project is Python, there are Rust ecosystem alternatives).

## A learning path

Given the questions you've been asking about Rust modules, visibility, and systems programming, a progression like this will steadily build your skills:

1. `ls` clone (filesystem basics)
2. `find` clone (recursion and paths)
3. TCP chat server (networking)
4. HTTP server (protocol parsing)
5. `curl`-like HTTP client
6. Mini Git (hashing and storage)
7. Dropbox-style file synchronizer (filesystem + networking)
8. BitTorrent client (real-world protocol and concurrency)
