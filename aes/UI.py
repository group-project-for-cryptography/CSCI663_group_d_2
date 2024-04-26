import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import aes

class AESGUI:
    def __init__(self, master):
        self.master = master
        master.title("AES Encryption and Decryption")

        self.plaintext_label = ttk.Label(master, text="Plaintext:")
        self.plaintext_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.plaintext_entry = ttk.Entry(master, width=40)
        self.plaintext_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

        self.key_label = ttk.Label(master, text="Symmetric Key:")
        self.key_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.key_entry = ttk.Entry(master, width=40)
        self.key_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        self.encrypt_button = ttk.Button(master, text="Encrypt", command=self.encrypt)
        self.encrypt_button.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.ciphertext_label = ttk.Label(master, text="Ciphertext:")
        self.ciphertext_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.ciphertext_entry = ttk.Entry(master, width=40)
        self.ciphertext_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

        self.decrypt_button = ttk.Button(master, text="Decrypt", command=self.decrypt)
        self.decrypt_button.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        self.decrypted_label = ttk.Label(master, text="Decrypted Plaintext:")
        self.decrypted_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        self.decrypted_entry = ttk.Entry(master, width=40)
        self.decrypted_entry.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

    def encrypt(self):
        plaintext = self.plaintext_entry.get().encode('utf-8')
        key = self.key_entry.get().encode('utf-8')

        if not plaintext or not key:
            showinfo("Error", "Please enter both plaintext and key.")
            return

        aes_cipher = aes.AESCipher(key)
        ciphertext = aes_cipher.encrypt(plaintext)

        self.ciphertext_entry.delete(0, tk.END)
        self.ciphertext_entry.insert(0, ciphertext.hex())

    def decrypt(self):
        ciphertext_hex = self.ciphertext_entry.get()
        key = self.key_entry.get().encode('utf-8')

        if not ciphertext_hex or not key:
            showinfo("Error", "Please enter both ciphertext and key.")
            return

        try:
            ciphertext = bytes.fromhex(ciphertext_hex)
        except ValueError:
            showinfo("Error", "Invalid ciphertext format.")
            return

        aes_cipher = aes.AESCipher(key)
        decrypted_text = aes_cipher.decrypt(ciphertext)

        self.decrypted_entry.delete(0, tk.END)
        self.decrypted_entry.insert(0, decrypted_text.decode('utf-8'))

root = tk.Tk()
app = AESGUI(root)
root.mainloop()
