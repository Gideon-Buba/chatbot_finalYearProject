import tkinter as tk
from chatbot import Chatbot

class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot")

        self.chatbot = Chatbot()

        self.conversation_text = tk.Text(master, state=tk.DISABLED, width=50, height=20)
        self.conversation_text.grid(row=0, column=0, padx=10, pady=10)

        self.input_label = tk.Label(master, text="You:")
        self.input_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        self.input_entry = tk.Entry(master, width=50)
        self.input_entry.grid(row=2, column=0, padx=10, pady=10)

        self.send_button = tk.Button(master, text="Send", command=self.send)
        self.send_button.grid(row=2, column=1, padx=10, pady=10)

    def send(self):
        user_input = self.input_entry.get()
        self.input_entry.delete(0, tk.END)

        response = self.chatbot.get_response(user_input)

        self.conversation_text.configure(state=tk.NORMAL)
        self.conversation_text.insert(tk.END, "You: " + user_input + "\n")
        self.conversation_text.insert(tk.END, "Chatbot: " + response + "\n\n")
        self.conversation_text.configure(state=tk.DISABLED)

root = tk.Tk()
my_gui = ChatbotGUI(root)
root.mainloop()
