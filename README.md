# 🥠 AI Fortune Cookie App

Crack open a digital fortune cookie and get a witty, sarcastic, or thoughtful message — powered by AI and curated wisdom.

![cookie gif](./cookie_gif.gif)

---

## 💡 What is This?

The **AI Fortune Cookie App** is a fun, interactive Streamlit web app that generates personalized fortunes based on:
- Your **mood** (Happy, Curious, Tired, etc.)
- Your **theme** (Tech Wisdom, Career, Sassy Chaos, etc.)
- Optionally, AI-generated fortunes using a lightweight NLP model (`EleutherAI/gpt-neo-125M`) via Hugging Face

---

## 🚀 Live Demo

🔗 [Click here to open the app on Streamlit Cloud]([https://your-app-url.streamlit.app](https://2cj78v6urjwb3pyzndjo6q.streamlit.app/)


---

## 🎯 Features

- 🧠 Toggle between hardcoded and AI-generated fortunes
- 💬 Typing animation for immersive experience
- 🎰 Lucky numbers with every fortune
- 🖼️ Custom cookie GIFs for visual delight
- 🧩 Uses Hugging Face's `gpt-neo-125M` model for creativity
- 💻 Lightweight — works on low-spec machines

---

## ⚙️ Tech Stack

| Tool        | Usage                        |
|-------------|------------------------------|
| Python      | Programming language    |
| Streamlit   | Web UI framework             |
| Hugging Face Transformers | Fortune generation (AI) |
| Torch       | Model backend                |
| Git + GitHub| Version control + deployment |

---

## 📁 Project Structure
📁 AI Fortune Cookie/ ├── app.py ├── requirements.txt ├── .streamlit/ │ └── config.toml ├── cookie_closed.png ├── cookie_open.png ├── cookie_gif.gif └── README.md
