import tkinter as tk
from tkinter import messagebox
import random
import json
from PIL import Image, ImageTk  # استيراد مكتبة Pillow

# Load or create the list of verses
try:
    with open("sentences.json", "r", encoding="utf-8") as file:
        sentences = json.load(file)
except FileNotFoundError:
    sentences = [
        "وَمَن يَتَّقِ اللَّهَ يَجْعَل لَّهُ مَخْرَجًا وَيَرْزُقْهُ مِنْ حَيْثُ لَا يَحْتَسِبُ",
        "وَلَا تَيْأَسُوا مِن رَّوْحِ اللَّهِ...",
        "قَالَ رَبِّ اشْرَحْ لِي صَدْرِي...",
        "فَإِنَّ مَعَ الْعُسْرِ يُسْرًا...",
        "إِنَّ اللَّهَ مَعَ الصَّابِرِينَ",
        "ادْعُونِي أَسْتَجِبْ لَكُمْ",
        "وَقُلْ رَبِّ زِدْنِي عِلْمًا",
        "لَا تَحْزَنْ إِنَّ اللَّهَ مَعَنَا"
    ]

# Load or create the list of favorite verses
try:
    with open("favorites.json", "r", encoding="utf-8") as file:
        favorite_sentences = json.load(file)
except FileNotFoundError:
    favorite_sentences = []

# Save sentences to file
def save_sentences():
    with open("sentences.json", "w", encoding="utf-8") as file:
        json.dump(sentences, file, ensure_ascii=False)

# Save favorite sentences to file
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
        save_sentences()
    elif new_sentence in sentences:
        messagebox.showwarning("تحذير", "هذه الآية موجودة بالفعل!")
    else:
        messagebox.showwarning("تحذير", "لا يمكن إضافة آية فارغة!")

# Add current verse to favorites
def add_to_favorites():
    current_sentence = label.cget("text")
    if current_sentence not in favorite_sentences:
        favorite_sentences.append(current_sentence)
        messagebox.showinfo("نجاح", "تمت إضافة الآية إلى المفضلة!")
        save_favorites()
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
    favorite_window.configure(bg="#000")

    tk.Label(favorite_window, text="الآيات المفضلة", font=("Arial", 14), bg="#eee").pack(pady=10)

    listbox = tk.Listbox(favorite_window, font=("Arial", 12), width=50, height=10)
    for sentence in favorite_sentences:
        listbox.insert(tk.END, sentence)
    listbox.pack(padx=10, pady=10)

    # Button to remove selected favorite
    def remove_favorite():
        selected = listbox.curselection()
        if selected:
            favorite_sentences.pop(selected[0])
            listbox.delete(selected)
            save_favorites()
            messagebox.showinfo("نجاح", "تمت إزالة الآية من المفضلة!")
        else:
            messagebox.showwarning("تحذير", "لم يتم اختيار آية!")

    remove_button = tk.Button(favorite_window, text="حذف من المفضلة", command=remove_favorite, bg="red", fg="white", font=("Arial", 12))
    remove_button.pack(pady=10)

# Export favorites
def export_favorites():
    if not favorite_sentences:
        messagebox.showwarning("تحذير", "لا توجد آيات في المفضلة!")
        return
    with open("favorites.txt", "w", encoding="utf-8") as file:
        for sentence in favorite_sentences:
            file.write(sentence + "\n")
    messagebox.showinfo("نجاح", "تم تصدير الآيات المفضلة إلى ملف!")

# UI setup
root = tk.Tk()
root.title("آيات قرآنية")
root.geometry("500x700")

# Load background image using Pillow
try:
    background_image = Image.open("background.jpg")  # تأكد من وجود ملف background.jpg في نفس المجلد
    background_image = background_image.resize((500, 700), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(background_image)
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)
except FileNotFoundError:
    # إذا لم توجد الصورة، استخدم لون خلفية عادي
    root.configure(bg="#f7f7f7")

# Verse label
label = tk.Label(root, text=random.choice(sentences), font=("Arial", 18), wraplength=400, bg="white", fg="darkgreen")
label.pack(pady=20)

# Progress label
progress_label = tk.Label(root, text=f"عرضت 1 من {len(sentences)}", font=("Arial", 12), bg="white")
progress_label.pack(pady=5)

# Buttons
refresh_button = tk.Button(root, text="تحديث الآية", command=refresh_sentence, bg="blue", fg="white", font=("Arial", 14))
refresh_button.pack(pady=10)

add_to_fav_button = tk.Button(root, text="إضافة إلى المفضلة", command=add_to_favorites, bg="gold", fg="black", font=("Arial", 14))
add_to_fav_button.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

add_button = tk.Button(root, text="إضافة آية", command=add_sentence, bg="green", fg="white", font=("Arial", 14))
add_button.pack(pady=10)

favorite_button = tk.Button(root, text="عرض المفضلة", command=show_favorite_sentences, bg="orange", fg="white", font=("Arial", 14))
favorite_button.pack(pady=10)

export_button = tk.Button(root, text="تصدير المفضلة", command=export_favorites, bg="purple", fg="white", font=("Arial", 14))
export_button.pack(pady=10)

# Exit button
exit_button = tk.Button(root, text="خروج", command=lambda: [save_sentences(), save_favorites(), root.destroy()], bg="black", fg="white", font=("Arial", 14))
exit_button.pack(pady=10)

root.mainloop()