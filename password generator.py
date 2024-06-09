import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()

        self.length_var = tk.IntVar(value=12)
        self.length_entry = tk.Entry(root, textvariable=self.length_var)
        self.length_entry.pack()

        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.include_uppercase)
        self.include_uppercase_check.pack()

        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_lowercase_check = tk.Checkbutton(root, text="Include Lowercase Letters", variable=self.include_lowercase)
        self.include_lowercase_check.pack()

        self.include_digits = tk.BooleanVar(value=True)
        self.include_digits_check = tk.Checkbutton(root, text="Include Digits", variable=self.include_digits)
        self.include_digits_check.pack()

        self.include_special = tk.BooleanVar(value=True)
        self.include_special_check = tk.Checkbutton(root, text="Include Special Characters", variable=self.include_special)
        self.include_special_check.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(root, textvariable=self.password_var, state='readonly', width=50)
        self.password_entry.pack()

        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack()

    def generate_password(self):
        length = self.length_var.get()
        if length <= 0:
            messagebox.showerror("Invalid Input", "Password length must be greater than 0")
            return

        char_set = ""
        if self.include_uppercase.get():
            char_set += string.ascii_uppercase
        if self.include_lowercase.get():
            char_set += string.ascii_lowercase
        if self.include_digits.get():
            char_set += string.digits
        if self.include_special.get():
            char_set += string.punctuation

        if not char_set:
            messagebox.showerror("Invalid Input", "You must select at least one character set")
            return

        password = ''.join(random.choice(char_set) for _ in range(length))
        self.password_var.set(password)

    def copy_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.password_var.get())
        messagebox.showinfo("Clipboard", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()