# Implementation of AES and Diffie-Hellman key exchange in group projects

## Overview
”Implement DES, AES, RSA, and Key exchange algorithms to cryptosystems”. And we chose AES and the Diffie–Hellman key exchange.

## Descriptions
◾️ AES Algorithm\
•	 block cipher with 128 bit block size 
\
•	 three key lengths must be supported: 128, 192 and 256 bit 
\
•	 the number of internal rounds of the cipher is a function of the key length according to Table 4.1. 
\
•	 Galois field arithmetic is used in most layers

![スクリーンショット 2024-03-01 15 03 16](https://github.com/group-project-for-cryptography/CSCI663_group_d_2/assets/58361623/751b03b1-5e45-47e7-a65b-87f34e227262)

- A brief description of the layers: \
Key Addition layer ...\
Byte Substitution layer (S-Box) ...\
Diffusion layer ...\
•	The ShiftRows layer ...\
•	The MixColumn layer ...

◾️ The Diffie–Hellman key exchange\
In preparing.

## Note for Code
◾️ AES\
**AES operates on blocks of fixed size (128 bits or 16 bytes), and the input data must be a multiple of this block size.**

An error is often caused by the length of the plaintext not being a multiple of 16. To fix this, we pad the plaintext to the appropriate length. We use PKCS7 padding, which is a commonly used padding scheme. \

(Add the explanation for “hazmat” library.)

◾️ The Diffie–Hellman key exchange\
In preparing.
