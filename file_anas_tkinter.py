
import tkinter as tk
from tkinter import filedialog, messagebox

def load_file():
    """يفتح نافذة اختيار الملف ويعرض محتوى الملف النصي بشكل منظم."""
    file_path = filedialog.askopenfilename(
        title="اختر ملفًا نصيًا",
        filetypes=[("ملفات نصية", ".txt"), ("كل الملفات", ".*")]
    )

    if not file_path:
        return  # إذا لم يتم اختيار ملف، لا تفعل شيئًا

    try:
        # قراءة محتوى الملف
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # عرض المحتوى في واجهة المستخدم
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, content)

        # تحديث عنوان النافذة باسم الملف
        root.title(f"عرض الملف - {file_path}")

    except Exception as e:
        messagebox.showerror("خطأ", f"تعذر قراءة الملف:\n{e}")

# إعداد النافذة الرئيسية
root = tk.Tk()
root.title("عارض الملفات النصية")
root.geometry("800x600")
root.minsize(600, 400)

# إطار للزر
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# زر تحميل الملف
load_button = tk.Button(
    button_frame, 
    text="تحميل ملف", 
    command=load_file, 
    font=("Segoe UI", 12), 
    bg="dodgerblue", 
    fg="white",
    padx=10, 
    pady=5
)
load_button.pack()

# عنصر Text Widget لعرض المحتوى
text_widget = tk.Text(
    root, 
    wrap=tk.WORD, 
    font=("Consolas", 12), 
    bg="white", 
    fg="black", 
    padx=10, 
    pady=10
)
text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# بدء تشغيل التطبيق
root.mainloop()