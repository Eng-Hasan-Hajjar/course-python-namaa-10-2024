import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageEnhance

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Editor")
        self.root.geometry("800x600")

        # إعداد المتغيرات
        self.image = None
        self.modified_image = None

        # أزرار التحكم
        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.resize_button = tk.Button(root, text="Resize", command=self.resize_image)
        self.resize_button.pack(pady=5)

        self.bw_button = tk.Button(root, text="Convert to B&W", command=self.convert_to_bw)
        self.bw_button.pack(pady=5)

        self.contrast_button = tk.Button(root, text="Enhance Contrast", command=self.enhance_contrast)
        self.contrast_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_button.pack(pady=10)

        # معاينة الصورة
        self.canvas = tk.Label(root)
        self.canvas.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            self.image = Image.open(file_path)
            self.modified_image = self.image.copy()
            self.display_image(self.image)

    def resize_image(self):
        if not self.image:
            messagebox.showerror("Error", "Please upload an image first.")
            return
        try:
            width = int(self.root.simpledialog.askstring("Resize", "Enter new width:"))
            height = int(self.root.simpledialog.askstring("Resize", "Enter new height:"))
            self.modified_image = self.image.resize((width, height))
            self.display_image(self.modified_image)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def convert_to_bw(self):
        if not self.image:
            messagebox.showerror("Error", "Please upload an image first.")
            return
        self.modified_image = self.image.convert("L")
        self.display_image(self.modified_image)

    def enhance_contrast(self):
        if not self.image:
            messagebox.showerror("Error", "Please upload an image first.")
            return
        enhancer = ImageEnhance.Contrast(self.image)
        self.modified_image = enhancer.enhance(2)  # زيادة التباين بمقدار 2x
        self.display_image(self.modified_image)

    def save_image(self):
        if not self.modified_image:
            messagebox.showerror("Error", "No image to save.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg")])
        if file_path:
            self.modified_image.save(file_path)
            messagebox.showinfo("Saved", "Image saved successfully!")

    def display_image(self, image):
        image.thumbnail((500, 500))  # ضبط الحجم للعرض فقط
        tk_image = ImageTk.PhotoImage(image)
        self.canvas.config(image=tk_image)
        self.canvas.image = tk_image

# تشغيل التطبيق
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()
