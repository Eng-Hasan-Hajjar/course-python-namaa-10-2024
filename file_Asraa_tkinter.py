import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext

def upload_file():
    # Open a file dialog and allow the user to select a file
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            # Read the content of the selected file
            with open(file_path, 'r') as file:
                content = file.read()
            # Display the content in the text widget
            text_area.delete('1.0', tk.END)  # Clear existing content
            text_area.insert(tk.END, content)
        except Exception as e:
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.END, f"Error reading file: {e}")

# Create the main tkinter window
root = tk.Tk()
root.title("File Viewer")

# Set the size of the window
root.geometry("600x400")

# Create a button to upload a file
upload_button = tk.Button(root, text="Upload File", command=upload_file)
upload_button.pack(pady=10)

# Create a scrolled text widget to display file content
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Run the tkinter event loop
root.mainloop()