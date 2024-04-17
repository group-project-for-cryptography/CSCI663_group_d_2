import tkinter as tk
from tkinter import messagebox
import random

def fast_raise_power_books(x, n, p):
    nb = bin(n)[2:]
    result = 1
    for i in nb:
        result = (result * result) % p
        if i == '1':
            result = (result * x) % p
    return result

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generatePrime(n):
    lower = 10**n
    higher = 10**(n+1) - 1
    while True:
        p = random.randrange(lower, higher)
        if isPrime(p):
            return p

def generateBase(p):
    return random.randrange(2, p - 1)

def submit_callback(input_entry, input_entry1):
    try:
        alice_key = int(input_entry.get())
        bob_key = int(input_entry1.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid integers for both keys.")
        return

    p = generatePrime(3)  # Generate a prime with 3 digits
    g = generateBase(p)  # Generate base g where g < p

    alice_public = fast_raise_power_books(g, alice_key, p)
    bob_public = fast_raise_power_books(g, bob_key, p)

    shared_key_alice = fast_raise_power_books(bob_public, alice_key, p)
    shared_key_bob = fast_raise_power_books(alice_public, bob_key, p)

    messagebox.showinfo("Diffie-Hellman Key Exchange", f"Shared key computed successfully: {shared_key_alice}")

window = tk.Tk()
window.title('Hellman Key Exchanger')
window.geometry('350x350')

input_label = tk.Label(window, text="Enter Alice Key: ", font=("Times New Roman", 10))
input_label.grid(column=0, row=1, padx=10, pady=25)
input_entry = tk.Entry(window, font=("Times New Roman", 10))
input_entry.grid(column=1, row=1, padx=10, pady=25)

input_label1 = tk.Label(window, text="Enter Bob Key: ", font=("Times New Roman", 10))
input_label1.grid(column=0, row=2, padx=10, pady=25)
input_entry1 = tk.Entry(window, font=("Times New Roman", 10))
input_entry1.grid(column=1, row=2, padx=10, pady=25)

submit_button = tk.Button(window, text="Submit Both", command=lambda: submit_callback(input_entry, input_entry1))
submit_button.grid(column=2, row=1, rowspan=2, pady=25)

window.mainloop()
