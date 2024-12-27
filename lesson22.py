### tkinter

import tkinter as tk
root =tk.Tk()

root.title("first 1 interface")
root.geometry("400x600")

labe3=tk.Label(root,text="grid:",font=("Arial",16),bg="red")
labe3.pack(side="left")

label=tk.Label(root,text="name:",font=("Arial",16),bg="yellow")
label.pack(side="left")

entry=tk.Entry(root,width=30)
entry.pack(pady=1,side="right")

label2=tk.Label(root,text="password:",font=("Arial",16),bg="yellow")
label2.pack()

entry2=tk.Entry(root,width=30,show="*")
entry2.pack(pady=1)
#Text
text=tk.Text(root,width=30,height=5)
text.pack(pady=1)

#Checkbutton
var = tk.BooleanVar()
check = tk.Checkbutton(root,text="تفعيل الخيار",variable=var)
check.pack()


##ٌradiobutton
selected_option=tk.StringVar()
radio1=tk.Radiobutton(root,text="1 choice",variable=selected_option,value="1")
radio2=tk.Radiobutton(root,text="2 choice",variable=selected_option,value="2")
radio1.pack()
radio2.pack()


##Listbox
listbox=tk.Listbox(root)
listbox.insert(1,"red")
listbox.insert(2,"blue")
listbox.insert(3,"black")
listbox.pack()

button=tk.Button(root,text="click",command=lambda:print("excuted"))
button.pack(pady=1)

root.mainloop()


