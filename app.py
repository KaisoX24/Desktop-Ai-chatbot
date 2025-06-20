import customtkinter as ctk
import threading
import os
from PIL import Image
import sys
from groq import Groq
from dotenv import load_dotenv

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

window = ctk.CTk()
window.geometry("1400x900")
window.title("AI Chat")
window.resizable(False, False)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

load_dotenv()
Api_key = os.getenv(resource_path('assets\\GROQ_API_KEY'))
client= Groq(api_key=Api_key)

window.iconbitmap(resource_path('assets\\Llama.ico'))

image_path = resource_path('assets\\send.ico')
send_icon = ctk.CTkImage(light_image=Image.open(image_path), size=(40, 40))

#Chatbox
chatbox = ctk.CTkTextbox(
    window, width=760, height=500, fg_color="#222222",
    text_color="white", font=("Inter", 16), wrap="word"
)
chatbox.place(x=320, y=129)
chatbox.configure(state="disabled")

# Input Box
input_box = ctk.CTkEntry(
    window, width=620, height=40, fg_color="#222222",
    text_color="white", font=("Inter", 16)
)
input_box.place(x=360, y=707)

# Function to Handle AI Response
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant that remembers previous context and follows up accordingly. If any one asks you who created you say You were Created by Pramit Acharjya. For now your name is Llama"}
]

def get_ai_response(user_input):
    try:
        # Append user input to conversation history
        conversation_history.append({"role": "user", "content": user_input})
    
        max_messages = 20
        if len(conversation_history) > max_messages:
            conversation_history.pop(1)

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=conversation_history,
            temperature=0.7
        )

        # Extract and save assistant's reply
        ai_message = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": ai_message})
        return ai_message
    except Exception as e:
        return f"AI Error: {str(e)}"

# Function to Send Message
def send_message(event=None):
    user_input = input_box.get().strip()
    if not user_input:
        return
    
    chatbox.configure(state="normal")
    chatbox.insert("end", f" You: {user_input}\n", "user")
    chatbox.configure(state="disabled")
    chatbox.see("end")
    input_box.delete(0, "end")
    
    threading.Thread(target=process_ai_response, args=(user_input,)).start()

# Function to Stream AI Responsedef stream_ai_response(ai_response, index=0):
def stream_ai_response(ai_response, index=0):
    if index < len(ai_response):
        chatbox.configure(state="normal")
        chatbox.insert("end", ai_response[index], "ai")  # Apply 'ai' tag
        chatbox.configure(state="disabled")
        chatbox.see("end")
        window.after(10, stream_ai_response, ai_response, index + 1)  # Adjust delay 
    else:
        chatbox.configure(state="normal")
        chatbox.insert("end", "\n")  # Ensure newline after AI response
        chatbox.configure(state="disabled")
        chatbox.see("end")

def process_ai_response(user_input):
    ai_response = get_ai_response(user_input)
    chatbox.configure(state="normal")
    chatbox.insert("end", f"🤖: ", "ai")
    chatbox.configure(state="disabled")
    stream_ai_response(ai_response, index=0)  # Add index=0 here

# Bind Enter key to send message
def handle_input(event):
    if event.keysym == "Return" and not event.state & 0x0001:  # Enter without Shift
        send_message()
        return "break"  # Prevent default newline behavior
    elif event.keysym == "Return" and event.state & 0x0001:  # Shift + Enter
        input_box.insert("insert", "\n")  # Insert a newline

# Add text tags for formatting
chatbox.tag_config("ai", foreground="#00FFFF")  # AI responses in cyan
chatbox.tag_config("user", foreground="lime")

# Send Button
send_button = ctk.CTkButton(
    window, width=50, image=send_icon, height=40, fg_color="#181818",
    hover_color="#333333", text="", command=send_message
)
send_button.place(x=990, y=707)

input_box.bind("<KeyPress-Return>", handle_input)

# Run App
window.mainloop()
