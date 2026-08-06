# Python Cybersecurity Basics
A collection of Python scripts developed during my cybersecurity studies. These projects demonstrate fundamental cybersecurity concepts including hashing, password security, and basic cryptographic operations.

## Projects

### 1. SHA-256 Hash Generator
Generates a SHA-256 hash from user-provided text.

#### Code Concepts
- Python input/output
- String encoding
- Cryptographic hashing
- SHA-256
- hashlib module

#### Example Output
```text
Enter Message: hello

SHA-256 Hash:
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

---

### 2. Password Hashing Example
Demonstrates how a password can be converted into a SHA-256 hash before storage.

#### Code Concepts
- Password hashing
- Cybersecurity fundamentals
- String encoding
- SHA-256
- hashlib module

#### Example Output
```text
Enter Password: qwerty

Stored Password Hash:
65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5
```

---

## Technologies Used
- Python
- hashlib

## Learning Outcome
These projects helped me understand:

- How cryptographic hashing works
- How SHA-256 generates unique hash values
- The role of hashing in cybersecurity
- Basic Python programming concepts
- Password storage concepts

## Note
Real-world password storage systems typically use specialized password hashing algorithms such as bcrypt, Argon2, or PBKDF2 rather than plain SHA-256.I built these scripts to practice hashing for university coursework

