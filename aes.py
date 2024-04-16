from aes_utils import key_expansion, aes_encrypt, aes_decrypt
from cryptography.hazmat.primitives import padding

class AESCipher:
    def __init__(self, key):
        self.key = key_expansion(key)    # Perform key expansion to generate round keys


    def encrypt(self, plaintext):
        # Use PKCS7 padding to ensure the plaintext length is a multiple of the block size
        padder = padding.PKCS7(128).padder()
        padded_plaintext = padder.update(plaintext) + padder.finalize()

        # Perform AES encryption on the padded plaintext using the first round key
        return aes_encrypt(self.key[0], padded_plaintext)

    def decrypt(self, ciphertext):
        # Perform AES decryption on the ciphertext using the first round key
        unpadder = padding.PKCS7(128).unpadder()
        decrypted_text = aes_decrypt(self.key[0], ciphertext)

        # Use PKCS7 unpadding to remove the padding after decryption
        return unpadder.update(decrypted_text) + unpadder.finalize()

# Define the key and plaintext
key = b'Sixteen byte key'
plaintext = b'This is a test.'

# Instantiate the AESCipher class with the provided key
aes_cipher = AESCipher(key)

# Encryption
ciphertext = aes_cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Decryption
decrypted_text = aes_cipher.decrypt(ciphertext)
print("Decrypted Text:", decrypted_text.decode('utf-8'))