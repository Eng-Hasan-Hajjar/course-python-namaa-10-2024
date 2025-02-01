import tkinter as tk
from tkinter import messagebox
import random

class MultiplicationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("تعلم جدول الضرب")
        self.root.geometry("300x200")

        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)

        self.question_label = tk.Label(root, text=f"ما هو ناتج ضرب {self.num1} في {self.num2}؟", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Arial", 14))
        self.answer_entry.pack(pady=10)

        self.check_button = tk.Button(root, text="تحقق", command=self.check_answer, font=("Arial", 14))
        self.check_button.pack(pady=10)

    def check_answer(self):
        user_answer = self.answer_entry.get()
        try:
            user_answer = int(user_answer)
            correct_answer = self.num1 * self.num2

            if user_answer == correct_answer:
                messagebox.showinfo("نتيجة", "إجابة صحيحة! أحسنت!")
            else:
                messagebox.showerror("نتيجة", f"إجابة خاطئة. الإجابة الصحيحة هي {correct_answer}.")

            self.generate_new_question()
        except ValueError:
            messagebox.showerror("خطأ", "الرجاء إدخال رقم صحيح.")

    def generate_new_question(self):
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.question_label.config(text=f"ما هو ناتج ضرب {self.num1} في {self.num2}؟")
        self.answer_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiplicationApp(root)
    root.mainloop()