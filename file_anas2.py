import tkinter as tk
from tkinter import filedialog, messagebox

def load_file():
    """
    يفتح نافذة اختيار ملف ويعرض محتواه داخل Text Widget.
    """
    global current_file_path  # لجعل مسار الملف متاحًا لحفظ التعديلات

    # فتح نافذة اختيار الملف
    file_path = filedialog.askopenfilename(
        title="اختر ملفًا نصيًا",
        filetypes=[("ملفات نصية", ".txt"), ("كل الملفات", ".*")]
    )
    if not file_path:  # إذا لم يتم اختيار ملف
        return

    try:
        # قراءة محتوى الملف
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # عرض المحتوى داخل Text Widget
        text_widget.delete(1.0, tk.END)  # مسح النص الموجود سابقًا
        text_widget.insert(tk.END, content)

        # تحديث عنوان النافذة مع اسم الملف
        root.title(f"تعديل الملف النصي - {file_path}")
        current_file_path = file_path  # حفظ مسار الملف الحالي

    except Exception as e:
        messagebox.showerror("خطأ", f"تعذر قراءة الملف:\n{e}")

def save_file():
    """
    يحفظ التعديلات في الملف النصي الحالي.
    """
    global current_file_path

    if not current_file_path:
        messagebox.showwarning("تحذير", "لم يتم تحميل أي ملف للحفظ!")
        return

    try:
        # الحصول على النص من Text Widget
        content = text_widget.get(1.0, tk.END).strip()

        # كتابة النص إلى الملف
        with open(current_file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        messagebox.showinfo("نجاح", "تم حفظ التعديلات بنجاح!")

    except Exception as e:
        messagebox.showerror("خطأ", f"تعذر حفظ التعديلات:\n{e}")

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("عارض وتعديل الملفات النصية")
root.geometry("800x600")
root.minsize(600, 400)

# مسار الملف الحالي
current_file_path = None

# إطار للأزرار
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
load_button.pack(side=tk.LEFT, padx=5)

# زر حفظ التعديلات
save_button = tk.Button(
    button_frame,
    text="حفظ التعديلات",
    command=save_file,
    font=("Segoe UI", 12),
    bg="green",
    fg="white",
    padx=10,
    pady=5
)
save_button.pack(side=tk.LEFT, padx=5)

# عنصر Text Widget لعرض النصوص وتعديلها
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