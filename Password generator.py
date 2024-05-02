import random
import string
import tkinter as tk
from tkinter import ttk

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.password_length_var = tk.IntVar()
        self.use_uppercase_var = tk.BooleanVar()
        self.use_numbers_var = tk.BooleanVar()
        self.use_special_chars_var = tk.BooleanVar()

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.master, text="Password Length:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(self.master, width=5, textvariable=self.password_length_var).grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Checkbutton(self.master, text="Include Uppercase Letters", variable=self.use_uppercase_var).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Checkbutton(self.master, text="Include Numbers", variable=self.use_numbers_var).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        ttk.Checkbutton(self.master, text="Include Special Characters", variable=self.use_special_chars_var).grid(row=3, column=0, padx=5, pady=5, sticky="w")

        ttk.Button(self.master, text="Generate Password", command=self.generate_password).grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.password_label = ttk.Label(self.master, text="")
        self.password_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def generate_password(self):
        length = self.password_length_var.get()
        use_uppercase = self.use_uppercase_var.get()
        use_numbers = self.use_numbers_var.get()
        use_special_chars = self.use_special_chars_var.get()

        if length < 1:
            self.password_label.config(text="Error: Password length must be at least 1")
            return

        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase if use_uppercase else ""
        numbers = string.digits if use_numbers else ""
        special_chars = string.punctuation if use_special_chars else ""

        all_chars = lowercase_letters + uppercase_letters + numbers + special_chars

        if not all_chars:
            self.password_label.config(text="Error: At least one character set must be enabled")
            return

        password = "".join(random.choice(all_chars) for _ in range(length))
        self.password_label.config(text=f"Generated Password: {password}")

root = tk.Tk()
app = PasswordGeneratorApp(root)
root.mainloop()
