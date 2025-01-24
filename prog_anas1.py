import tkinter as tk
import random

sentences = [
    "وَمَن يَتَّقِ اللَّهَ يَجْعَل لَّهُ مَخْرَجًا وَيَرْزُقْهُ مِنْ حَيْثُ لَا يَحْتَسِبُ",
    "وَلَا تَيْأَسُوا مِن رَّوْحِ اللَّهِ ۖ إِنَّهُ لَا يَيْأَسُ مِن رَّوْحِ اللَّهِ إِلَّا الْقَوْمُ الْكَافِرُونَ",
    "قَالَ رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي وَاحْلُلْ عُقْدَةً مِّن لِّسَانِي يَفْقَهُوا قَوْلِي",
    "وَٱصْبِرْ لِحُكْمِ رَبِّكَ فَإِنَّكَ بِأَعْيُنِنَا ۖ وَسَبِّحْ بِحَمْدِ رَبِّكَ حِينَ تَقُومُ ",
    "وَمَنْ يَتَّقِ اللَّهَ يَجْعَلْ لَهُ مَخْرَجًا، وَيَرْزُقْهُ مِنْ حَيْثُ لَا يَحْتَسِب "
]
random_sentence = random.choice(sentences)


root = tk.Tk()
root.title("ايات قرانيه")

root.geometry("500x200")  #حجم النافذة

label = tk.Label(root, text=random_sentence, font=("Arial", 16), wraplength=400, justify="center")  # إنشاء عنصر لعرض النص
label.pack(pady=20)

exit_button = tk.Button(root, text="خروج", command=root.destroy, font=("Arial", 14), bg="black", fg="white")
exit_button.pack(pady=10)

root.mainloop()