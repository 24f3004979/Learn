# Git & DSA Exploration

## 1. Git Internal Storage (Binary Trees)
Git doesn't exactly use a standard Binary Search Tree, but a **Merkle Tree** (specifically a Merkle DAG). 
- Objects (commits, trees, blobs) are identified by their SHA-1 hash.
- A "Tree" object points to other "Tree" objects or "Blobs" (files).
- This structure allows Git to quickly determine if two versions of a project are different by just comparing the top-level hashes.

## 2. SHA-1 vs Caesar Cipher
- **Caesar Cipher:** A simple substitution cipher where each letter is shifted a fixed number of positions. It is easily broken.
- **SHA-1 (Git):** A cryptographic hash function. It takes any input and produces a unique 40-character string. It is one-way (you can't go back to the original data) and collision-resistant.

## 3. Dynamic Programming & DSA
- **Dynamic Programming (DP):** Solving complex problems by breaking them down into simpler subproblems and storing the results (memoization) to avoid redundant work.
- **Threaded Programming:** Running multiple sequences of instructions (threads) concurrently within a single process.
