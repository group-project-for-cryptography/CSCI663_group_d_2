# Implementation of AES and Diffie-Hellman key exchange in group projects

## Overview

”Implement DES, AES, RSA, and Key exchange algorithms to cryptosystems”. And we chose AES and the Diffie–Hellman key exchange.

## Descriptions

◾️ AES Algorithm\
• block cipher with 128 bit block size
\
• three key lengths must be supported: 128, 192 and 256 bit
\
• the number of internal rounds of the cipher is a function of the key length according to Table 4.1.
\
• Galois field arithmetic is used in most layers

![スクリーンショット 2024-03-01 15 03 16](https://github.com/group-project-for-cryptography/CSCI663_group_d_2/assets/58361623/751b03b1-5e45-47e7-a65b-87f34e227262)

- A brief description of the layers: 
1.	Key Additional Layer [linear].\
　　　XOR addition of subkeys for each round generated from the input key. \
2. Byte Substitution Layer (S-BoX) [nonlinear].\
　　　Performs a Galois nonlinear operation on the input data.\
　Diffusion Layer [linear]\
　　3.1 ShiftRows Layer\
　　　　　Shifts data byte by byte.\
　　3.2 MixColumn Layer\
　　　　　Performs matrix operation on Galois field.\


◾️ The Diffie–Hellman key exchange\
In preparing.

## Note for Code

◾️ AES\
**AES operates on blocks of fixed size (128 bits or 16 bytes), and the input data must be a multiple of this block size.**

An error is often caused by the length of the plaintext not being a multiple of 16. To fix this, we pad the plaintext to the appropriate length. We use PKCS7 padding, which is a commonly used padding scheme.

**Hazmat / Hazardous Materials**

The “hazmat” or “Hazardous Materials” layer is one of two levels that derives from the cryptography library, and it is often regarded as low-level cryptographic primitives, which requires users to have a deep understanding of cryptographic concepts and beware of its potential dangers of usage. Inside the hazmat layer, there is another layer called primitives, which will be used for the AES implementation. It offers many useful built-in modules that will assist our project such as:

- Authenticated encryption
- Asymmetric algorithms
- Constant time functions
- Key derivation functions
- Key wrapping
- Message authentication codes
- Messages digests (Hashing)
- Symmetric encryption
- Symmetric Padding
- Two-factor authentication

◾️ The Diffie–Hellman key exchange\
In preparing.
