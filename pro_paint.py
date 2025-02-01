import tkinter as tk
from tkinter import colorchooser

# دالة الرسم
def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    canvas.create_line((last_x, last_y, event.x, event.y), fill=brush_color, width=brush_size, capstyle=tk.ROUND, smooth=True)
    last_x, last_y = event.x, event.y

# تغيير لون الفرشاة
def change_color():
    global brush_color
    color = colorchooser.askcolor()[1]  # فتح نافذة اختيار اللون
    if color:
        brush_color = color

# تغيير حجم الفرشاة
def change_size(size):
    global brush_size
    brush_size = size

# مسح اللوحة
def clear_canvas():
    canvas.delete("all")

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("برنامج الرسم البسيط")

# إعداد المتغيرات
brush_color = "black"  # لون الفرشاة الافتراضي
brush_size = 2  # حجم الفرشاة الافتراضي
last_x, last_y = None, None  # إحداثيات الرسم

# إنشاء لوحة الرسم
canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack(fill=tk.BOTH, expand=True)

# ربط أحداث الفأرة
canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

# إنشاء إطار للأزرار
controls_frame = tk.Frame(root)
controls_frame.pack(fill=tk.X)

# أزرار تغيير اللون
colors = ["black", "red", "green", "blue", "yellow"]
for color in colors:
    btn = tk.Button(controls_frame, bg=color, width=2, command=lambda c=color: change_color() if c == "custom" else setattr(globals(), 'brush_color', c))
    btn.pack(side=tk.LEFT, padx=2, pady=2)

# زر اختيار لون مخصص
custom_color_btn = tk.Button(controls_frame, text="لون مخصص", command=change_color)
custom_color_btn.pack(side=tk.LEFT, padx=2, pady=2)

# أزرار تغيير حجم الفرشاة
sizes = [2, 5, 10, 15]
for size in sizes:
    btn = tk.Button(controls_frame, text=str(size), command=lambda s=size: change_size(s))
    btn.pack(side=tk.LEFT, padx=2, pady=2)

# زر مسح اللوحة
clear_btn = tk.Button(controls_frame, text="مسح اللوحة", command=clear_canvas)
clear_btn.pack(side=tk.LEFT, padx=2, pady=2)

# تشغيل النافذة
root.mainloop()