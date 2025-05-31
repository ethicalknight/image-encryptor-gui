import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

KEY = 25  # You can make this user-defined too


def encrypt_image(img):
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + KEY) % 256, (g + KEY) % 256, (b + KEY) % 256)
    return img


def decrypt_image(img):
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - KEY) % 256, (g - KEY) % 256, (b - KEY) % 256)
    return img


class ImageEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryptor GUI")
        self.root.geometry("800x600")
        self.root.config(bg="#f0f0f0")

        self.image_label = tk.Label(self.root, bg="#f0f0f0")
        self.image_label.pack(pady=20)

        self.button_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.button_frame.pack()

        tk.Button(self.button_frame, text="Load Image", command=self.load_image, width=20, bg="#6c5ce7", fg="white").grid(row=0, column=0, padx=10)
        tk.Button(self.button_frame, text="Encrypt Image", command=self.encrypt, width=20, bg="#00b894", fg="white").grid(row=0, column=1, padx=10)
        tk.Button(self.button_frame, text="Decrypt Image", command=self.decrypt, width=20, bg="#d63031", fg="white").grid(row=0, column=2, padx=10)
        tk.Button(self.button_frame, text="Save Image", command=self.save_image, width=20, bg="#0984e3", fg="white").grid(row=0, column=3, padx=10)

        self.original_img = None
        self.current_img = None
        self.tk_img = None

    def load_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if path:
            self.original_img = Image.open(path).convert("RGB")
            self.current_img = self.original_img.copy()
            self.show_image(self.current_img)

    def show_image(self, img):
        resized = img.resize((400, 300))
        self.tk_img = ImageTk.PhotoImage(resized)
        self.image_label.config(image=self.tk_img)

    def encrypt(self):
        if self.current_img:
            self.current_img = encrypt_image(self.current_img.copy())
            self.show_image(self.current_img)
        else:
            messagebox.showwarning("No Image", "Please load an image first!")

    def decrypt(self):
        if self.current_img:
            self.current_img = decrypt_image(self.current_img.copy())
            self.show_image(self.current_img)
        else:
            messagebox.showwarning("No Image", "Please load an image first!")

    def save_image(self):
        if self.current_img:
            path = filedialog.asksaveasfilename(defaultextension=".png")
            if path:
                self.current_img.save(path)
                messagebox.showinfo("Saved", f"Image saved to {path}")
        else:
            messagebox.showwarning("No Image", "No image to save!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorApp(root)
    root.mainloop()
