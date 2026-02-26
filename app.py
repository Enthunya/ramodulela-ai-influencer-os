# app.py - AI Influencer OS Dashboard (Starter)
# Run with: python app.py  (after installing deps and Ollama)

import gradio as gr
from langchain_ollama import OllamaLLM  # pip install langchain-ollama
from langchain.prompts import PromptTemplate

# Basic character personality (expand this later into a full "bible")
CHARACTER_PERSONALITY = """
You are an energetic, motivational fitness influencer named "Zara Fit".
You speak in an upbeat, empowering tone, use emojis 💪🔥, short sentences,
and always end with a call-to-action like "Tag a friend who needs this!".
Keep responses fun, relatable, and under 150 words.
"""

# Simple prompt template for script generation
prompt_template = PromptTemplate.from_template(
    "{personality}\n\nUser request: {user_prompt}\n\nGenerate a short social media script (Reel/TikTok style):"
)

# Load Ollama model (pull llama3.1 or mistral first: ollama pull llama3.1)
llm = OllamaLLM(model="llama3.1")  # Change to your preferred model

# Main generation function
def generate_script(user_prompt):
    if not user_prompt.strip():
        return "Please enter a prompt! 😊"
    
    full_prompt = prompt_template.format(
        personality=CHARACTER_PERSONALITY,
        user_prompt=user_prompt
    )
    
    try:
        response = llm.invoke(full_prompt)
        return response.strip()
    except Exception as e:
        return f"Error: {str(e)}\nMake sure Ollama is running and model is pulled!"

# Gradio Interface
with gr.Blocks(title="AI Influencer OS - Starter Dashboard") as demo:
    gr.Markdown(
        """
        # AI Influencer OS
        **Generate scripts for your AI influencer!**
        
        Enter a topic or idea below (e.g., "Morning motivation workout" or "Protein shake recipe review").
        """
    )
    
    input_prompt = gr.Textbox(
        label="Your Prompt / Idea",
        placeholder="E.g., Create a Reel about leg day motivation...",
        lines=3
    )
    
    generate_btn = gr.Button("Generate Script 🔥")
    
    output = gr.Textbox(
        label="Generated Script",
        lines=8,
        interactive=False
    )
    
    generate_btn.click(
        fn=generate_script,
        inputs=input_prompt,
        outputs=output
    )
    
    gr.Markdown(
        """
        **Next steps:** Add persistent memory, image generation (Flux), video, lip-sync...
        Run Ollama first: `ollama run llama3.1`
        """
    )

# Launch the app
demo.launch(share=False)  # share=True for public link (temporary)
