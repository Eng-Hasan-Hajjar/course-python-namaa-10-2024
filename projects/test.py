import tkinter as tk

# إنشاء نافذة رئيسية
root = tk.Tk()
root.title("مثال على استخدام pack")

# إنشاء عناصر متعددة
label1 = tk.Label(root, text="العنصر الأول")
label2 = tk.Label(root, text="العنصر الثاني")
label3 = tk.Label(root, text="العنصر الثالث")

# استخدام pack مع pady لتحديد المسافات
label1.pack(pady=10)  # مسافة 10 بكسل أعلى وأسفل العنصر الأول
label2.pack(pady=(5, 15))  # مسافة 5 بكسل أعلى و15 بكسل أسفل العنصر الثاني
label3.pack(pady=0)  # بدون مسافات عمودية للعنصر الثالث

# بدء واجهة المستخدم
root.mainloop()