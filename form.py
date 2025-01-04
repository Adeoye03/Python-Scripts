import tkinter as tk
from tkinter import messagebox

class SimpleForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Form")
        self.root.geometry("400x300")

        #create form fields
        tk.Label(root, text="Personal Information Form", font=('Arial', 14, 'bold')).pack(pady=10)

        # Name field
        tk.Label(root, text="Full Name:").pack()
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.pack(pady=5)

        # Email field
        tk.Label(root, text="Email:").pack()
        self.email_entry = tk.Entry(root, width=30)
        self.email_entry.pack(pady=5)

        # Age field
        tk.Label(root, text="Age:").pack()
        self.age_entry = tk.Entry(root, width=30)
        self.age_entry.pack(pady=5)

        # Comments field
        tk.Label(root, text="Comments:").pack()
        self.comment_text = tk.Text(root, width=30, height=4)
        self.comment_text.pack(pady=5)

        # Submit button
        tk.Button(root, text="submit", command=self.submit_form).pack(pady=20)

    def submit_form(self):
        # Get values from form fields
        name = self.name_entry.get()
        email = self.email_entry.get()
        age = self.age_entry.get()
        comments = self.comment_text.get("1.0", tk.END)

        # Basic validation
        if not name or not email or not age:
            messagebox.showerror("Error", "please fill in all fields!")
            return
        
        # Show success message
        message = f"Form submitted successfully!\n\nName: {name}\nEmail: {email}\nAge: {age}\nComments: {comments}"
        messagebox.showinfo("Success", message)

        # Clear form fields
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.comment_text.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleForm(root)
    root.mainloop()