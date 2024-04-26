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
1.	**Key Additional Layer [linear].**\
　　　XOR addition of subkeys for each round generated from the input key. 
2. **Byte Substitution Layer (S-BoX) [nonlinear].**\
　　　Performs a Galois nonlinear operation on the input data.\
Diffusion Layer [linear]\
　　3.1 **ShiftRows Layer**\
　　　　　Shifts data byte by byte.\
　　3.2 **MixColumn Layer**\
　　　　　Performs matrix operation on Galois field.

The actual order of processing is \
2\ 
↓
3.1\
↓
3.2\
↓ 
1

![スクリーンショット 2024-04-26 19 48 48](https://github.com/group-project-for-cryptography/CSCI663_group_d_2/assets/58361623/da29fd7b-8f60-4de4-a993-1eec9060c9d4)

◾️ The Diffie–Hellman key exchange\
In preparing.

## Note for Code

◾️ AES\
**AES operates on blocks of fixed size (128 bits or 16 bytes), and the input data must be a multiple of this block size.**

An error is often caused by the length of the plaintext not being a multiple of 16. To fix this, we pad the plaintext to the appropriate length. We use PKCS7 padding, which is a commonly used padding scheme.

[PKCS7](https://cryptography.io/en/latest/hazmat/primitives/padding/#cryptography.hazmat.primitives.padding.PKCS7.unpadder)

When calling `padder()` or `unpadder()` the result will conform to the `PaddingContext` interface. You can then call `update(data)` with data until you have fed everything into the context. Once that is done call `finalize()` to finish the operation and obtain the remainder of the data.

**Hazmat / Hazardous Materials**

The “hazmat” or “Hazardous Materials” layer is one of two levels that derives from the cryptography library, and it is often regarded as low-level cryptographic primitives, which requires users to have a deep understanding of cryptographic concepts and beware of its potential dangers of usage. Inside the hazmat layer, there is another layer called primitives, which will be used for the AES implementation. It offers many useful built-in modules that will assist our project.

◾️ The Diffie–Hellman key exchange\
In preparing.
