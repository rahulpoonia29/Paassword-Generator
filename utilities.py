import tkinter as tk
from tkinter import filedialog


def clipboard(label, root, text):
    if text == "":
        error_text = "Please first generate password"
        label.config(text=error_text, foreground="red")
    else:
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()
        error_text = "Password successfully copied to clipboard"
        label.config(text=error_text, foreground="green")


def save_file(text):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
    )
    if file_path:
        with open(file_path, "a") as file:
            file.write(f"{text}\n")
