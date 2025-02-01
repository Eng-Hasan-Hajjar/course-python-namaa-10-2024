import tkinter as tk
from tkinter import messagebox, ttk
import random
import json
from PIL import Image, ImageTk

# Load or create the list of verses
try:
    with open("sentences.json", "r", encoding="utf-8") as file:
        sentences = json.load(file)
except FileNotFoundError:
    sentences = [
        "وَمَن يَتَّقِ اللَّهَ يَجْعَل لَّهُ مَخْرَجًا وَيَرْزُقْهُ مِنْ حَيْثُ لَا يَحْتَسِبُ",
        "وَلَا تَيْأَسُوا مِن رَّوْحِ اللَّهِ...",
        "قَالَ رَبِّ اشْرَحْ لِي صَدْرِي...",
        "فَإِنَّ مَعَ الْعُسْرِ يُسْرًا...",
        "إِنَّ اللَّهَ مَعَ الصَّابِرِينَ",
        "ادْعُونِي أَسْتَجِبْ لَكُمْ",
        "وَقُلْ رَبِّ زِدْنِي عِلْمًا",
        "لَا تَحْزَنْ إِنَّ اللَّهَ مَعَنَا"
    ]

# Load favorites
try:
    with open("favorites.json", "r", encoding="utf-8") as file:
        favorite_sentences = json.load(file)
except FileNotFoundError:
    favorite_sentences = []

categories = {
    "التفاؤل": ["وَلَا تَيْأَسُوا مِن رَّوْحِ اللَّهِ...", "فَإِنَّ مَعَ الْعُسْرِ يُسْرًا...", "لَا تَحْزَنْ إِنَّ اللَّهَ مَعَنَا"],
    "الصبر": ["وَٱصْبِرْ لِحُكْمِ رَبِّكَ...", "إِنَّ اللَّهَ مَعَ الصَّابِرِينَ"],
    "الدعاء": ["قَالَ رَبِّ اشْرَحْ لِي صَدْرِي...", "ادْعُونِي أَسْتَجِبْ لَكُمْ", "وَقُلْ رَبِّ زِدْنِي عِلْمًا"]
}

# Save sentences to file
def save_sentences():
    with open("sentences.json", "w", encoding="utf-8") as file:
        json.dump(sentences, file, ensure_ascii=False)

# Save favorites to file
def save_favorites():
    with open("favorites.json", "w", encoding="utf-8") as file:
        json.dump(favorite_sentences, file, ensure_ascii=False)

# Refresh random verse
def refresh_sentence():
    random_sentence = random.choice(sentences)
    label.config(text=random_sentence)
    progress_label.config(text=f"عرضت {sentences.index(random_sentence)+1} من {len(sentences)}")

# Add a new verse
def add_sentence():
    new_sentence = entry.get().strip()
    if new_sentence and new_sentence not in sentences:
        sentences.append(new_sentence)
        entry.delete(0, tk.END)
        messagebox.showinfo("نجاح", "تمت إضافة الآية بنجاح!")
    elif new_sentence in sentences:
        messagebox.showwarning("تحذير", "هذه الآية موجودة بالفعل!")
    else:
        messagebox.showwarning("تحذير", "لا يمكن إضافة آية فارغة!")

# Add to favorites
def add_to_favorites():
    current_sentence = label.cget("text")
    if current_sentence not in favorite_sentences:
        favorite_sentences.append(current_sentence)
        messagebox.showinfo("نجاح", "تمت إضافة الآية إلى المفضلة!")
    else:
        messagebox.showwarning("تحذير", "هذه الآية موجودة بالفعل في المفضلة!")

# Show favorites
def show_favorite_sentences():
    if not favorite_sentences:
        messagebox.showinfo("مفضلة فارغة", "لا توجد آيات في المفضلة حالياً.")
        return
    favorite_window = tk.Toplevel(root)
    favorite_window.title("المفضلة")
    favorite_window.geometry("400x300")
    tk.Label(favorite_window, text="الآيات المفضلة", font=("Arial", 14)).pack()
    listbox = tk.Listbox(favorite_window, font=("Arial", 12))
    for sentence in favorite_sentences:
        listbox.insert(tk.END, sentence)
    listbox.pack(padx=10, pady=10)

# Export favorites
def export_favorites():
    with open("favorites.txt", "w", encoding="utf-8") as file:
        for sentence in favorite_sentences:
            file.write(sentence + "\n")
    messagebox.showinfo("نجاح", "تم تصدير الآيات المفضلة إلى ملف!")

# UI setup
root = tk.Tk()
root.title("آيات قرآنية")
root.geometry("500x700")
root.configure(bg="#f7f7f7")

# Background image
try:
    background = Image.open("background.jpg")
    background = background.resize((500, 700))
    bg_img = ImageTk.PhotoImage(background)
    bg_label = tk.Label(root, image=bg_img)
    bg_label.place(relwidth=1, relheight=1)
except Exception as e:
    messagebox.showerror("خطأ", f"لم يتم العثور على صورة الخلفية: {e}")

# Verse label
label = tk.Label(root, text=random.choice(sentences), font=("Arial", 18), wraplength=400, bg="#f7f7f7", fg="darkgreen")
label.pack(pady=20)

# Progress label
progress_label = tk.Label(root, text=f"عرضت 1 من {len(sentences)}", font=("Arial", 12), bg="#f7f7f7")
progress_label.pack(pady=5)

# Buttons
refresh_button = tk.Button(root, text="تحديث الآية", command=refresh_sentence, bg="blue", fg="white", font=("Arial", 14))
refresh_button.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

add_button = tk.Button(root, text="إضافة آية", command=add_sentence, bg="green", fg="white", font=("Arial", 14))
add_button.pack(pady=10)

fav_button = tk.Button(root, text="إضافة إلى المفضلة", command=add_to_favorites, bg="red", fg="white", font=("Arial", 14))
fav_button.pack(pady=10)

favorite_button = tk.Button(root, text="عرض المفضلة", command=show_favorite_sentences, bg="orange", fg="white", font=("Arial", 14))
favorite_button.pack(pady=10)

export_button = tk.Button(root, text="تصدير المفضلة", command=export_favorites, bg="purple", fg="white", font=("Arial", 14))
export_button.pack(pady=10)

exit_button = tk.Button(root, text="خروج", command=lambda: [save_sentences(), save_favorites(), root.destroy()], bg="black", fg="white", font=("Arial", 14))
exit_button.pack(pady=10)

root.mainloop()