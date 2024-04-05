import tkinter as tk
from tkinter import Label, Entry, Button, messagebox

def process_input():
    user_input = entry.get()
    if user_input:
        output_text.set(f"Processed: {user_input}")
    else:
        messagebox.showwarning("Empty Input", "Please enter some text.")

# Create the main application window
root = tk.Tk()
root.title("Input and Output Operations")

# Create and place widgets in the window
label = Label(root, text="Enter Text:")
label.pack(pady=10)

entry = Entry(root, width=30)
entry.pack(pady=10)

process_button = Button(root, text="Process", command=process_input)
process_button.pack(pady=10)

output_text = tk.StringVar()
output_label = Label(root, textvariable=output_text)
output_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
