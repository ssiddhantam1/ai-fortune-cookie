import streamlit as st
from transformers import pipeline, set_seed
import random
import time

# --- Page Config ---
st.set_page_config(page_title="AI Fortune Cookie", page_icon="🥠")

# --- Load small model ---
@st.cache_resource
def load_model():
    set_seed(42)
    return pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

generator = load_model()

# --- UI ---
st.title("🥠 AI Fortune Cookie")
st.image("cookie_gif.gif", caption="Click the cookie, your fortune awaits...", use_container_width=True)

name = st.text_input("Your Name", placeholder="e.g. Alex")
mood = st.selectbox("How are you feeling today?", ["Happy", "Tired", "Curious", "Stressed", "Just here for cookies"])
theme = st.radio("Pick your fortune theme:", ["General", "Tech Wisdom", "Career", "Silly Chaos"])
use_ai = st.toggle("🧠 Occasionally let AI write my fortune", value=True)

# --- Curated Fortunes ---
fallback_fortunes = {
    "General": [
        "Greatness is coming. Probably tomorrow. Sleep in today.",
        "Don’t take advice from cookies. Except this one."
    ],
    "Tech Wisdom": [
        "Your code will run… eventually.",
        "May your semicolons be ever in place."
    ],
    "Career": [
        "Opportunities are brewing. So is coffee.",
        "Imposter syndrome is just success in disguise."
    ],
    "Silly Chaos": [
        "You will forget why you walked into the room. Twice.",
        "Your left sock has secrets. Ask it no questions."
    ]
}

# --- Prompt generator ---
def generate_prompt(mood, theme):
    return f"Write a witty and short fortune cookie message for someone who is {mood.lower()} about {theme.lower()}."

# --- Reveal button ---
if st.button("🥠 Crack Open Fortune"):
    st.markdown("### ✨ Your fortune is being crafted...")

    with st.spinner("Cracking the cookie..."):
        time.sleep(1)

        use_model = use_ai and random.random() < 0.5  # 50% chance of AI use
        if use_model:
            prompt = generate_prompt(mood, theme)
            raw = generator(prompt, max_length=40, do_sample=True, top_k=50,truncation=True,pad_token_id=50256)[0]["generated_text"]
            fortune = raw.replace(prompt, "").strip().split(".")[0] + "."
        else:
            fortune = random.choice(fallback_fortunes[theme])

    # --- Typing effect ---
    placeholder = st.empty()
    typed = ""
    for char in fortune:
        typed += char
        placeholder.markdown(f"<div style='font-size:22px; text-align:center;'>✨ {typed} ✨</div>", unsafe_allow_html=True)
        time.sleep(0.03)

    # --- Lucky numbers ---
    st.markdown("---")
    lucky = random.sample(range(1, 100), 6)
    st.markdown(f"🎰 **Lucky Numbers:** {' - '.join(map(str, lucky))}")
    st.markdown("<small style='color:gray;'>Model: GPT-Neo 125M • Powered by Hugging Face • Cookie GIF: Giphy</small>", unsafe_allow_html=True)

