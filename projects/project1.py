import tkinter as tk
from tkinter import messagebox

# دالة لتحليل الجملة بناءً على تقسيم السلسلة النصية
def analyze_sentence():
    sentence = entry.get().strip()  # جلب الجملة التي أدخلها المستخدم وإزالة الفراغات الزائدة
    if not sentence:
        messagebox.showerror("خطأ", "يرجى إدخال جملة صحيحة.")
        return
    
    # تقسيم الجملة إلى كلمات
    words = sentence.split()
    
    # تعريف المتغيرات الأساسية للفاعل، الفعل، المفعول به
    subject, verb, obj = "", "", ""
    
    # إذا كانت الجملة تتكون من ثلاث كلمات أو أكثر، نفترض أن أول كلمة هي الفاعل، الثانية هي الفعل، والثالثة هي المفعول به
    if len(words) >= 3:
        subject = words[0]
        verb = words[1]
        obj = words[2]
        # البقية من الجملة
        others = " ".join(words[3:]) if len(words) > 3 else ""
    else:
        messagebox.showerror("خطأ", "يرجى إدخال جملة أطول.")
        return

    # إظهار النتيجة
    result = f"الفاعل: {subject}\nالفعل: {verb}\nالمفعول به: {obj}\nالبقية: {others}"
    messagebox.showinfo("نتيجة التحليل", result)

# إعداد واجهة المستخدم باستخدام tkinter
root = tk.Tk()
root.title("تحليل الجملة الإنجليزية")

# تعليمات المستخدم
label = tk.Label(root, text="أدخل جملة صحيحة قواعدياً باللغة الإنجليزية:")
label.pack(pady=10)

# مربع الإدخال للمستخدم
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# زر للتحليل
analyze_button = tk.Button(root, text="تحليل", command=analyze_sentence)
analyze_button.pack(pady=10)

# بدء حلقة الأحداث
root.mainloop()
