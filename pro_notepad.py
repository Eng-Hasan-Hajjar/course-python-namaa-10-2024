import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Notepad")
        self.root.geometry("600x400")

        # إنشاء مربع النص الرئيسي مع دعم التمرير العمودي
        self.text_area = tk.Text(self.root, wrap="word", undo=True)
        self.text_area.pack(expand=1, fill="both")
        
        # شريط القوائم
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        
        # قائمة "ملف"
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        
        # قائمة "تحرير"
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=lambda: self.root.focus_get().event_generate("<<Cut>>"))
        self.edit_menu.add_command(label="Copy", command=lambda: self.root.focus_get().event_generate("<<Copy>>"))
        self.edit_menu.add_command(label="Paste", command=lambda: self.root.focus_get().event_generate("<<Paste>>"))
        
        self.file_path = None  # تخزين مسار الملف الحالي
    
    def new_file(self):
        """إنشاء ملف جديد"""
        self.text_area.delete(1.0, tk.END)
        self.file_path = None
    
    def open_file(self):
        """فتح ملف نصي"""
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())
                self.file_path = file_path
    
    def save_file(self):
        """حفظ المحتوى إلى ملف"""
        if self.file_path:
            with open(self.file_path, "w", encoding="utf-8") as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            self.save_file_as()
    
    def save_file_as(self):
        """حفظ الملف بإسم جديد"""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.text_area.get(1.0, tk.END))
                self.file_path = file_path

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
