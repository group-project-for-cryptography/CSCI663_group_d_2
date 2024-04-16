import unittest
from aes_utils import key_expansion, aes_encrypt, aes_decrypt
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

        ciphertext = self.aes_cipher.encrypt(self.plaintext)

        decrypted_text = self.aes_cipher.decrypt(ciphertext)

        self.assertEqual(decrypted_text, padded_plaintext)

if __name__ == '__main__':
    unittest.main()
