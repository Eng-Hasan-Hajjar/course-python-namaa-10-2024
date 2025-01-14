import tkinter as tk
from tkinter import messagebox
import random
import string

# وظيفة توليد كلمة المرور
def generate_password():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showerror("خطأ", "يجب أن يكون طول كلمة المرور 4 على الأقل.")
            return

        # تجميع الأحرف بناءً على الخيارات المحددة
        characters = ""
        if var_uppercase.get():
            characters += string.ascii_uppercase
        if var_lowercase.get():
            characters += string.ascii_lowercase
        if var_numbers.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("خطأ", "يرجى اختيار معيار واحد على الأقل!")
            return

        # توليد كلمة المرور
        password = "".join(random.choice(characters) for _ in range(length))
        text_password.delete("1.0", tk.END)
        text_password.insert(tk.END, password)

    except ValueError:
        messagebox.showerror("خطأ", "يرجى إدخال رقم صحيح في حقل الطول.")

# إعداد نافذة Tkinter
root = tk.Tk()
root.title("مولد كلمات مرور قوية")
root.geometry("400x300")

# الطول
label_length = tk.Label(root, text="طول كلمة المرور:")
label_length.pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# خيارات المعايير
var_uppercase = tk.BooleanVar()
var_lowercase = tk.BooleanVar()
var_numbers = tk.BooleanVar()
var_symbols = tk.BooleanVar()

check_uppercase = tk.Checkbutton(root, text="تضمين أحرف كبيرة", variable=var_uppercase)
check_uppercase.pack(anchor="w", padx=20)
check_lowercase = tk.Checkbutton(root, text="تضمين أحرف صغيرة", variable=var_lowercase)
check_lowercase.pack(anchor="w", padx=20)
check_numbers = tk.Checkbutton(root, text="تضمين أرقام", variable=var_numbers)
check_numbers.pack(anchor="w", padx=20)
check_symbols = tk.Checkbutton(root, text="تضمين رموز", variable=var_symbols)
check_symbols.pack(anchor="w", padx=20)

# زر توليد كلمة المرور
btn_generate = tk.Button(root, text="توليد كلمة المرور", command=generate_password)
btn_generate.pack(pady=10)

# عرض كلمة المرور
text_password = tk.Text(root, height=2, width=40)
text_password.pack(pady=5)

# بدء التطبيق
root.mainloop()
