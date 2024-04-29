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
**2**\
↓\
**3.1**\
↓\
**3.2**\
↓\
**1**

![スクリーンショット 2024-04-26 19 48 48](https://github.com/group-project-for-cryptography/CSCI663_group_d_2/assets/58361623/da29fd7b-8f60-4de4-a993-1eec9060c9d4)

◾️ The Diffie–Hellman key exchange\
• provides a practical solution to the key distribution problem by allowing two parties to derive a common secret key by communicating over an insecure channel.
\
• it consists of two protocols, the set-up protocol and the main protocol, which performs the actual key exchange.
\
 * The set-up protocol consists of the following steps:
   <img width="1294" alt="Screenshot 2024-04-29 at 8 40 17 in the morning" src="https://github.com/group-project-for-cryptography/CSCI663_group_d_2/assets/100827012/6c34dfcf-30a7-488c-8c3b-fd7aaec39480">
     - Bob and Alice publicly choose p and α.
  \
 * The key-exchange protocol consists of the following steps:
   <img width="1283" alt="Screenshot 2024-04-29 at 8 41 24 in the morning" src="https://github.com/group-project-for-cryptography/CSCI663_group_d_2/assets/100827012/30db3d36-671b-4aa5-ac9a-0eef31bed64c">
     - Bob and Alice then choose their own private key *a* and *b* respectively. These private keys enable them to           generate a joint secret key.
     - In these ways, they securely send each other encrypted message and decrypt it with their own private key.


## Note for Code

◾️ AES\
**AES operates on blocks of fixed size (128 bits or 16 bytes), and the input data must be a multiple of this block size.**

An error is often caused by the length of the plaintext not being a multiple of 16. To fix this, we pad the plaintext to the appropriate length. We use PKCS7 padding, which is a commonly used padding scheme.

[PKCS7](https://cryptography.io/en/latest/hazmat/primitives/padding/#cryptography.hazmat.primitives.padding.PKCS7.unpadder)

Padding is a way to take data that may or may not be a multiple of the block size for a cipher and extend it out so that it is. This is required for many block cipher modes as they require the data to be encrypted to be an exact multiple of the block size.

PKCS7 padding is a generalization of PKCS5 padding (also known as standard padding). PKCS7 padding works by appending `N` bytes with the value of `chr(N)`, where `N` is the number of bytes required to make the final block of data the same size as the block size.

When calling `padder()` or `unpadder()` the result will conform to the `PaddingContext` interface. You can then call `update(data)` with data until you have fed everything into the context. Once that is done call `finalize()` to finish the operation and obtain the remainder of the data.

**Hazmat / Hazardous Materials**

The “hazmat” or “Hazardous Materials” layer is one of two levels that derives from the cryptography library, and it is often regarded as low-level cryptographic primitives, which requires users to have a deep understanding of cryptographic concepts and beware of its potential dangers of usage. Inside the hazmat layer, there is another layer called primitives, which will be used for the AES implementation. It offers many useful built-in modules that will assist our project.

◾️ The Diffie–Hellman key exchange\
In preparing.
