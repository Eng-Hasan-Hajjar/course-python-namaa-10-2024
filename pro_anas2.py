import tkinter as tk
import random
import json

# تحميل أو إنشاء قائمة الآيات
try:
    with open("sentences.json", "r", encoding="utf-8") as file:
        sentences = json.load(file)
except FileNotFoundError:
    sentences = [
        "وَمَن يَتَّقِ اللَّهَ يَجْعَل لَّهُ مَخْرَجًا وَيَرْزُقْهُ مِنْ حَيْثُ لَا يَحْتَسِبُ",
        "وَلَا تَيْأَسُوا مِن رَّوْحِ اللَّهِ ۖ إِنَّهُ لَا يَيْأَسُ مِن رَّوْحِ اللَّهِ إِلَّا الْقَوْمُ الْكَافِرُونَ",
        "قَالَ رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي وَاحْلُلْ عُقْدَةً مِّن لِّسَانِي يَفْقَهُوا قَوْلِي",
        "وَٱصْبِرْ لِحُكْمِ رَبِّكَ فَإِنَّكَ بِأَعْيُنِنَا ۖ وَسَبِّحْ بِحَمْدِ رَبِّكَ حِينَ تَقُومُ",
        "وَمَنْ يَتَّقِ اللَّهَ يَجْعَلْ لَهُ مَخْرَجًا، وَيَرْزُقْهُ مِنْ حَيْثُ لَا يَحْتَسِب",
        "فَإِنَّ مَعَ الْعُسْرِ يُسْرًا إِنَّ مَعَ الْعُسْرِ يُسْرًا",
        "إِنَّ اللَّهَ مَعَ الصَّابِرِينَ",
        "ادْعُونِي أَسْتَجِبْ لَكُمْ",
        "وَقُلْ رَبِّ زِدْنِي عِلْمًا",
        "لَا تَحْزَنْ إِنَّ اللَّهَ مَعَنَا"
    ]

categories = {
    "التفاؤل": ["وَلَا تَيْأَسُوا مِن رَّوْحِ اللَّهِ...", "فَإِنَّ مَعَ الْعُسْرِ يُسْرًا...", "لَا تَحْزَنْ إِنَّ اللَّهَ مَعَنَا"],
    "الصبر": ["وَٱصْبِرْ لِحُكْمِ رَبِّكَ...", "إِنَّ اللَّهَ مَعَ الصَّابِرِينَ"],
    "الدعاء": ["قَالَ رَبِّ اشْرَحْ لِي صَدْرِي...", "ادْعُونِي أَسْتَجِبْ لَكُمْ", "وَقُلْ رَبِّ زِدْنِي عِلْمًا"]
}

# حفظ الآيات إلى ملف
def save_sentences():
    with open("sentences.json", "w", encoding="utf-8") as file:
        json.dump(sentences, file, ensure_ascii=False)

# تحديث الآية عشوائيًا
def refresh_sentence():
    random_sentence = random.choice(sentences)
    label.config(text=random_sentence)

# إضافة آية جديدة
def add_sentence():
    new_sentence = entry.get()
    if new_sentence.strip():
        sentences.append(new_sentence)
        entry.delete(0, tk.END)

# عرض جميع الآيات في نافذة جديدة
def show_all_sentences():
    all_sentences_window = tk.Toplevel(root)
    all_sentences_window.title("جميع الآيات")
    all_sentences_window.geometry("400x300")

    for sentence in sentences:
        tk.Label(all_sentences_window, text=sentence, font=("Arial", 12), wraplength=350, justify="center").pack(pady=5)

# تبديل الآيات تلقائيًا
def auto_refresh():
    refresh_sentence()
    root.after(10000, auto_refresh)  # تحديث كل 10 ثوانٍ

# اختيار فئة لعرض آية منها
def choose_category(category):
    random_sentence = random.choice(categories[category])
    label.config(text=random_sentence)

root = tk.Tk()
root.title("ايات قرانيه")
root.geometry("500x500")
root.configure(bg="#f7f7f7")

random_sentence = random.choice(sentences)

label = tk.Label(root, text=random_sentence, font=("Arial", 16), wraplength=400, justify="center", bg="#f7f7f7", fg="darkgreen")
label.pack(pady=20)

refresh_button = tk.Button(root, text="تحديث الآية", command=refresh_sentence, font=("Arial", 14), bg="blue", fg="white")
refresh_button.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="إضافة آية", command=add_sentence, font=("Arial", 14), bg="green", fg="white")
add_button.pack(pady=10)

all_sentences_button = tk.Button(root, text="عرض جميع الآيات", command=show_all_sentences, font=("Arial", 14), bg="purple", fg="white")
all_sentences_button.pack(pady=10)

category_menu = tk.OptionMenu(root, tk.StringVar(value="اختر فئة"), *categories.keys(), command=choose_category)
category_menu.pack(pady=10)

exit_button = tk.Button(root, text="خروج", command=lambda: [save_sentences(), root.destroy()], font=("Arial", 14), bg="black", fg="white")
exit_button.pack(pady=10)

# تشغيل التحديث التلقائي
auto_refresh()

# بدء البرنامج
root.protocol("WM_DELETE_WINDOW", lambda: [save_sentences(), root.destroy()])
root.mainloop()