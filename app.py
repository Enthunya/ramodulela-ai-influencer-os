# app.py - AI Influencer OS Dashboard

import gradio as gr
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate  # ← this is the correct import

# CHARACTER PERSONALITY - Edit this block freely
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
        return f"Error: {str(e)}\nMake sure Ollama is running (`ollama run llama3.1` in another cmd)."

with gr.Blocks(title="AI Influencer OS - Zara Fit") as demo:
    gr.Markdown(
        """
        # AI Influencer OS – Zara Fit
        **Generate Reels/TikTok scripts!**
        Edit CHARACTER_PERSONALITY in app.py to customize her.
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
        **Tips:** Keep Ollama running in another window (`ollama run llama3.1`).
        """
    )

demo.launch(share=False)
