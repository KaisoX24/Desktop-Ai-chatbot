# 🦙 Llama AI Chatbot (Desktop App)

A sleek and responsive AI chatbot desktop app built using `CustomTkinter`, powered by [Groq](https://groq.com) and the **LLaMA 3.1** model. Llama is a context-aware assistant that remembers previous conversations and responds intelligently.

---

## ✨ Features

- 🖥️ Beautiful dark-themed desktop UI using `customtkinter`
- 🧠 Context-aware conversations powered by Groq API + LLaMA 3.1
- 🔄 Streaming AI responses with typing effect
- 🔐 API key loaded securely via `.env`
- 📁 Resource-safe asset loading with `PyInstaller` compatibility

---

## 📸 Screenshots

> Screenshots are stored in the `assets/` folder.

| Chat Window | Icon |
|-------------|------|
| ![Chat UI](assets/screenshot.png) | ![App Icon](assets/Llama.ico) |

---

## ⚙️ Tech Stack

| Technology         | Purpose                                               |
|--------------------|-------------------------------------------------------|
| Python             | Core programming language                             |
| CustomTkinter      | Desktop UI framework with modern widgets              |
| Groq API (LLaMA 3) | AI model for chatbot responses                        |
| Pillow (PIL)       | Image handling                                        |
| dotenv             | Securely manage API keys                              |
| threading / sys / os | System utilities and multithreading support       |

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/llama-chatbot.git
cd llama-chatbot
```
---

### 2. **Install Requirements**

- Create a virtual environment (optional but recommended):
 ```bash
 python -m venv venv
 venv\Scripts\activate  # Mac: source venv/bin/activate
 ```
- Install Dependencies:
 ```bash
pip install -r requirements.txt
 ```
