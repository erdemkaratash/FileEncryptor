from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os
import glob
import hashlib
import tkinter as tk
from tkinter import messagebox
import base64

def encrypt_file(file_path, key):
    cipher = AES.new(key, AES.MODE_ECB)

    with open(file_path, 'rb') as f:
        file_data = f.read()

    encrypted_data = cipher.encrypt(pad(file_data, AES.block_size))
    encrypted_file_path = os.path.join(os.path.dirname(file_path), base64.urlsafe_b64encode(cipher.encrypt(pad(os.path.basename(file_path).encode(), AES.block_size))).decode())

    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_data)

    os.remove(file_path)

def decrypt_file(file_path, key):
    cipher = AES.new(key, AES.MODE_ECB)

    with open(file_path, 'rb') as f:
        encrypted_data = f.read()

    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    decrypted_file_path = os.path.join(os.path.dirname(file_path), unpad(cipher.decrypt(base64.urlsafe_b64decode(os.path.basename(file_path))), AES.block_size).decode())

    with open(decrypted_file_path, 'wb') as f:
        f.write(decrypted_data)

    os.remove(file_path)

def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

def run_operation():
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password.")
        return

    key = password.encode()
    key = hashlib.sha256(key).digest()

    if var.get() == 'E':
        encrypt_folder(folder_path, key)
        messagebox.showinfo("Success", "Folder encrypted")
    elif var.get() == 'D':
        decrypt_folder(folder_path, key)
        messagebox.showinfo("Success", "Folder decrypted")

folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Private")

root = tk.Tk()

var = tk.StringVar(value='E')
encrypt_rb = tk.Radiobutton(root, text='Encrypt', variable=var, value='E')
encrypt_rb.pack()

decrypt_rb = tk.Radiobutton(root, text='Decrypt', variable=var, value='D')
decrypt_rb.pack()

password_label = tk.Label(root, text='Password:')
password_label.pack()

password_entry = tk.Entry(root, show='*')
password_entry.pack()

run_button = tk.Button(root, text='Run', command=run_operation)
run_button.pack()

root.mainloop()
