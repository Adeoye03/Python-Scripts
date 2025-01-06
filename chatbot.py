import tkinter as tk
from tkinter import scrolledtext

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("400x500")

        # Chat display area
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
        self.chat_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # User input area
        self.user_input = tk.Entry(root, width=50)
        self.user_input.pack(pady=10, padx=10, fill=tk.X)
        self.user_input.bind("<Return>", self.process_input)

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.process_input)
        self.send_button.pack(pady=10)

    def process_input(self, event=None):
        user_input = self.user_input.get().strip().lower()
        if user_input:
            self.display_message(f"You: {user_input}")
            self.user_input.delete(0, tk.END)
            self.respond(user_input)

    def display_message(self, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.config(state='disabled')
        self.chat_display.yview(tk.END)

    def respond(self, user_input):
        if "hi" in user_input or "hello" in user_input:
            response = "Chatbot: Hi there! How can I help you?"
        elif "bye" in user_input:
            response = "Chatbot: Goodbye! Have a great day!"
        elif "your name" in user_input:
            response = "Chatbot: I'm a simple AI chatbot, still learning new things!"
        else:
            response = "Chatbot: I'm not sure how to respond to that. Can you ask something else?"
        
        self.display_message(response)
        if "bye" in user_input:
            self.root.after(2000, self.root.quit)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()


