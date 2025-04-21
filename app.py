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
mood = st.selectbox(
    "How are you feeling today?", 
    [
        "Happy", 
        "Tired", 
        "Curious", 
        "Stressed", 
        "Just here for cookies",
        "Excited",
        "Anxious",
        "Hopeful",
        "Lost in thought",
        "Motivated",
        "Hungry",
        "Procrastinating"
    ]
)
theme = st.radio("Pick your fortune theme:", ["General", "Tech Wisdom", "Career", "Silly Chaos"])
use_ai = st.toggle("🧠 Occasionally let AI write my fortune", value=True)

# --- Curated Fortunes ---
mood_based_fortunes  = "Excited": [
        "Buckle up. Greatness is speeding your way!",
        "Your energy could power a small city today.",
        "Ride this wave—it's a good one.",
    ],
    "Anxious": [
        "Breathe. You’ve overcome worse with less.",
        "Even the moon has phases. This will pass.",
        "Kindness begins with you—be gentle with your mind.",
    ],
    "Hopeful": [
        "That feeling in your chest? That’s potential.",
        "Hope is the seed of extraordinary days.",
        "You’re closer than you think. Keep going.",
    ],
    "Lost in thought": [
        "Answers are in the silence. Listen closely.",
        "Even the clouds make space for the sun.",
        "Wandering minds find magical places.",
    ],
    "Motivated": [
        "Today is for building empires, even small ones.",
        "You’ve got this. The data agrees.",
        "Let momentum be your superpower today.",
    ],
    "Hungry": [
        "Fortune favors the well-fed. Treat yourself.",
        "Your next idea comes after snacks. Probably cookies.",
        "Food for thought? Maybe just food first.",
    ],
    "Procrastinating": [
        "Even your distractions are masterpieces.",
        "You’ll start after this fortune. Pinky swear.",
        "Rest is productive, too. Unless it's your 5th break."
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
            if mood in mood_based_fortunes and random.random() < 0.5:
                fortune = random.choice(mood_based_fortunes[mood])
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

