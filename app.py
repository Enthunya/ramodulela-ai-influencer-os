# app.py - AI Influencer OS Dashboard (Easy Personality Editing)

import gradio as gr
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# ────────────────────────────────────────────────
# CHARACTER PERSONALITY - EDIT THIS BLOCK ONLY
# Change name, age, tone, rules, backstory, memory hints, etc.
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
Future memory rule: Remember previous scripts and user feedback. Reference them naturally, e.g., "Like I said last week about squats...".
"""
# ────────────────────────────────────────────────

prompt_template = PromptTemplate.from_template(
    "{personality}\n\nUser request: {user_prompt}\n\nGenerate a short social media script (Reel/TikTok style):"
)

llm = OllamaLLM(model="llama3.1")

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
        return f"Error: {str(e)}\n\nMake sure Ollama is running (`ollama run llama3.1` in another cmd window)."

with gr.Blocks(title="AI Influencer OS - Zara Fit") as demo:
    gr.Markdown(
        """
        # AI Influencer OS – Zara Fit
        **Generate Reels/TikTok scripts for your fitness influencer!**
        
        Edit the `CHARACTER_PERSONALITY` block in app.py to change her vibe, add memory rules, backstory, etc.
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
        lines=12,
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
        - Run Ollama separately: `ollama run llama3.1`
        - Next steps: Add long-term memory (ChromaDB), images (Flux), video, auto-posting.
        """
    )

demo.launch(share=False)  # share=True for temporary public link
