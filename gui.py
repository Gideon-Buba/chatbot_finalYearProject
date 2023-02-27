import tkinter as tk
from chatbot import predict_class, get_response

class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot")

        # Create chat history text box
        self.chat_history = tk.Text(master, state=tk.DISABLED)
        self.chat_history.grid(row=0, column=0, padx=10, pady=10)

        # Create user input text box
        self.user_input = tk.Entry(master)
        self.user_input.grid(row=1, column=0, padx=10, pady=10)

        # Create send button
        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        # Bind enter key to send message function
        master.bind('<Return>', self.send_message)

        # Initialize chat history
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.insert(tk.END, "Chatbot: Hi there! How can I help you today?\n\n")
        self.chat_history.config(state=tk.DISABLED)

    def send_message(self, event=None):
        # Get user input text
        user_input_text = self.user_input.get()

        # Add user input to chat history
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.insert(tk.END, "You: " + user_input_text + "\n\n")
        self.chat_history.config(state=tk.DISABLED)

        # Predict chatbot response
        predicted_tag = predict_class(user_input_text)
        response = get_response(predicted_tag)

        # Add chatbot response to chat history
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.insert(tk.END, "Chatbot: " + response + "\n\n")
        self.chat_history.config(state=tk.DISABLED)

        # Clear user input text box
        self.user_input.delete(0, tk.END)

root = tk.Tk()
chatbot_gui = ChatbotGUI(root)
root.mainloop()
