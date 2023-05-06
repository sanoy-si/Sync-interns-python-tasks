import tkinter as tk
import datetime
import random


def _input():
    user_input = input_box.get()

    conversation.insert(tk.END, "User: " + user_input + "\n")

    input_box.delete(0, tk.END)

    bot_response = generate_response(user_input)

    conversation.insert(tk.END, "Bot: " + bot_response + "\n")

root = tk.Tk()

root.title("Chat Bot")

conversation = tk.Text(root, width=50, height=20)
conversation.pack()

input_frame = tk.Frame(root)
input_label = tk.Label(input_frame, text="User input:")
input_label.pack(side=tk.LEFT)
input_box = tk.Entry(input_frame, width=40)
input_box.pack(side=tk.LEFT)
submit_button = tk.Button(input_frame, text="Send", command=_input)
submit_button.pack(side=tk.LEFT)
input_frame.pack()
    

responses = {
    "hello": ["Hello!  What can I help you?", "Hi there! What can I help you?", "Greetings! What can I help you?"],
    "hi":["Hello!  What can I help you?", "Hi there! What can I help you?", "Greetings! I'm Jarvis. What can I help you?"],
    "what time is it": ["It\'s "+datetime.datetime.now().strftime("%H:%M")+'.'],
    "what's your name": ["I'm Jarvis. What can i help?"],
    "how are you": ["I'm doing well, thank you! how can i be a help today?", "I'm fine, thanks for asking! how can i be a help today?", "I'm great! how can i be a help today?"],
    "what's up": ["Not much, just chatting with you!", "Just hanging out, how about you?", "Nothing much, how about you?"],
    "bye": ["See you later!", "Have a nice day!"],
    "default": ["I'm sorry, I don't understand.", "Can you rephrase that?", "I'm not sure what you mean."]
}



def generate_response(user_input):

    user_input = user_input.lower()
    
    for key in responses:

        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])



root.mainloop()



