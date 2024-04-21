import unittest
from aes_utils import key_expansion, aes_encrypt, aes_decrypt
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives import hashes

class TestAESUtils(unittest.TestCase):

    def test_key_expansion(self):
        key = b'secretkey123456'
        expected_key_expansion = [b'secretkey123456']
        self.assertEqual(key_expansion(key), expected_key_expansion)

    def test_aes_encrypt_decrypt(self):
        key = b'secretkey12345678'[:16]  # Key size: 16 bytes
        plaintext = b'Hello, AES!'

        # Padding the plaintext
        padder = PKCS7(128).padder()
        padded_plaintext = padder.update(plaintext) + padder.finalize()

        ciphertext = aes_encrypt(key, padded_plaintext)

        # Decrypting and unpadding the ciphertext
        decrypted_text = aes_decrypt(key, ciphertext)
        unpadder = PKCS7(128).unpadder()
        unpadded_decrypted_text = unpadder.update(decrypted_text) + unpadder.finalize()

        # Check if the unpadded decrypted text matches the original plaintext
        self.assertEqual(unpadded_decrypted_text, plaintext)

if __name__ == '__main__':
    unittest.main()
