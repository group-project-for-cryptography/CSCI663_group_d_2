import unittest
from cryptography.hazmat.primitives import padding
from aes import AESCipher

class TestAESCipher(unittest.TestCase):
    def setUp(self):
        self.key = b'Sixteen byte key'
        self.plaintext = b'This is a test.'
        self.aes_cipher = AESCipher(self.key)

    def test_encrypt_decrypt(self):
        ciphertext = self.aes_cipher.encrypt(self.plaintext)
        decrypted_text = self.aes_cipher.decrypt(ciphertext)
        self.assertEqual(decrypted_text, self.plaintext)

    def test_padding(self):
        # Test if padding is correctly applied and removed
        padder = padding.PKCS7(128).padder()
        padded_plaintext = padder.update(self.plaintext) + padder.finalize()

        # Encrypt the padded plaintext
        ciphertext = self.aes_cipher.encrypt(padded_plaintext)

        # Decrypt the ciphertext
        decrypted_text = self.aes_cipher.decrypt(ciphertext)

        # Remove padding from decrypted text
        unpadder = padding.PKCS7(128).unpadder()
        unpadded_text = unpadder.update(decrypted_text) + unpadder.finalize()

        self.assertEqual(unpadded_text, self.plaintext)

if __name__ == '__main__':
    unittest.main()
