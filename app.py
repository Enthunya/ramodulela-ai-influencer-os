# app.py - AI Influencer OS Dashboard (Updated with Easy Personality Editing)

import gradio as gr
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# ────────────────────────────────────────────────
# CHARACTER PERSONALITY - Edit this block freely!
# This is the "brain" of your influencer. Change anything here.
# ────────────────────────────────────────────────
CHARACTER_PERSONALITY = """
You are Zara Fit, a 28-year-old energetic South African fitness influencer from Johannesburg.
You are confident, empowering, relatable, and always positive.
Your tone: upbeat, motivational, fun, use emojis 💪🔥✨, short sentences, slang like "fam", "crush it", "let's gooo".
You speak like you're talking to your best friend in the gym.
Always end with a call-to-action: "Tag a friend!", "Drop a 🔥 if you're in!", "DM me your progress!".
Keep scripts under 150 words for Reels/TikTok.
You love leg day, protein shakes, consistency, and morning workouts.
Reference Johannesburg/SA culture when it fits (e.g., "Load shedding got you down? Get that endorphin hit anyway!").
"""
# ────────────────────────────────────────────────

# Prompt template (don't edit unless you want advanced changes)
prompt_template = PromptTemplate.from_template(
    "{personality}\n\nUser request: {user_prompt}\n\nGenerate a short social media script (Reel/TikTok style):"
)

# Load Ollama model (make sure you ran `ollama pull llama3.1`)
llm = OllamaLLM(model="llama3.1")  # or "llama3.1:8b" for smaller/faster

def generate_script(user_prompt):
    if not user_prompt.strip():
        return "Please enter a prompt! 😊 Let's get moving!"
    
    full_prompt = prompt_template.format(
        personality=CHARACTER_PERSONALITY,
        user_prompt=user_prompt
    )
    
    try:
        response = llm.invoke(full_prompt)
        return response.strip()
    except Exception as e:
        return f"Error connecting to Ollama: {str(e)}\nMake sure Ollama is running (`ollama run llama3.1` in another window)."

# Gradio Interface
with gr.Blocks(title="AI Influencer OS - Zara Fit") as demo:
    gr.Markdown(
        """
        # AI Influencer OS – Zara Fit Edition
        **Generate scripts for your fitness influencer!**
        
        Edit the `CHARACTER_PERSONALITY` section in app.py to change her vibe, backstory, tone, or add memory rules.
        """
    )
    
    input_prompt = gr.Textbox(
        label="Your Prompt / Idea",
        placeholder="E.g., Create a Reel about morning motivation workout...",
        lines=3
    )
    
    generate_btn = gr.Button("Generate Script 🔥")
    
    output = gr.Textbox(
        label="Zara Fit's Script",
        lines=10,
        interactive=False
    )
    
    generate_btn.click(
        fn=generate_script,
        inputs=input_prompt,
        outputs=output
    )
    
    gr.Markdown(
        """
        **Tips:**
        - Run Ollama in another cmd: `ollama run llama3.1`
        - Next: Add memory so Zara remembers past scripts!
        """
    )

# Launch the app
demo.launch(share=False)  # Change to True for temporary public link
