# Cryptography Projects

This repository contains a collection of cryptography-related projects, focusing on implementing and exploring cryptographic algorithms. The primary goal is to gain a deeper understanding of how these algorithms work and their applications in securing data.

## Table of Contents
- [Overview](#overview)
- [Implemented Projects](#implemented-projects)
  - [1. RSA Encryption](#1-rsa-encryption)
- [Setup](#setup)
- [Usage](#usage)
- [Future Plans](#future-plans)
- [Contributing](#contributing)
- [License](#license)

## Overview
This repository is a learning-focused collection of cryptography projects. It serves as a personal playground to explore cryptographic concepts, implement them in Python, and understand their real-world applications. The repository starts with an implementation of the RSA algorithm.

## Implemented Projects

### 1. RSA Encryption
**RSA (Rivest-Shamir-Adleman)** is an asymmetric encryption algorithm widely used for secure data transmission. This project includes:
- **Key Generation:** Generate public and private keys using large prime numbers.
- **Encryption:** Encrypt plaintext into ciphertext using the public key.
- **Decryption:** Decrypt ciphertext back into plaintext using the private key.

**Features:**
- Implements efficient key generation using probabilistic prime tests.
- Converts plaintext to blocks for encryption and decryption.
- Supports encoding and decoding of ASCII text.

### Future Plans
- Add more cryptographic algorithms like AES, Diffie-Hellman, and SHA-256.
- Build command-line tools for encryption and decryption.

## Setup
To get started, clone this repository and install the necessary dependencies.
```
git clone https://github.com/Alir3zaRaisi/Cryptography
cd Cryptography
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Dependencies
- Python 3.7+
- `random`, `math`, and other standard libraries

For additional libraries, use:
```
pip install -r requirements.txt
```

## Usage
1. Navigate to the RSA directory:
    ```bash
    cd RSA
    ```
2. Run the example usage script:
    ```bash
    python3 example_usage.py
    ```
3. Follow the instructions to test encryption and decryption.

## Future Plans
- Add implementations for additional cryptographic algorithms like AES, Diffie-Hellman, and SHA-256.
- Include tools for file encryption/decryption.


