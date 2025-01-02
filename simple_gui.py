import tkinter as tk
from tkinter import messagebox

#create the main window
root = tk.Tk()
root.title("Simple GUI")
root.geometry("300x200")

#function to handle button click
def on_button_click():
    user_input = entry.get()
    if user_input:
        messagebox.showinfo("Message", f"You entered: {user_input}")
    else:
        messagebox.showwarning("Warning", "please enter something!")

#add a label
label = tk.Label(root, text="Enter something", font=("Arial", 12))
label.pack(pady=10)

#add an entry field
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

#add a button
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack(pady=10)

root.mainloop()