### tkinter

import tkinter as tk
root =tk.Tk()
root.title("first 1 interface")
root.geometry("600x600")


"""
label=tk.Label(root,text="grid:",font=("Arial",16),bg="red")
label.grid(row=0,column=0,padx=5)
label2=tk.Label(root,text="grid:",font=("Arial",16),bg="blue")
label2.grid(row=0,column=5)
"""



label=tk.Label(root,text="place:",font=("Arial",16),bg="red")
label.place(x=0,y=0)
label2=tk.Label(root,text="grid:",font=("Arial",16),bg="blue")
label2.place(x=10,y=100)


root.mainloop()