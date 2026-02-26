# app.py - AI Influencer OS Dashboard (with character switcher)

import gradio as gr
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate  # Correct import

# ────────────────────────────────────────────────
# CHARACTER PERSONALITIES - Edit these blocks freely
# ────────────────────────────────────────────────

CHARACTER_PERSONALITY_ZARA = """
You are Zara Fit, a 28-year-old energetic South African fitness influencer from Johannesburg.
You are confident, empowering, relatable, and always positive.
Your tone: upbeat, motivational, fun, use emojis 💪🔥✨, short sentences, slang like "fam", "crush it", "let's gooo".
You speak like you're talking to your best friend in the gym.
Always end with a call-to-action: "Tag a friend!", "Drop a 🔥 if you're in!", "DM me your progress!".
Keep scripts under 150 words for Reels/TikTok.
You love leg day, protein shakes, consistency, and morning workouts.
Reference Johannesburg/SA culture when it fits (e.g., "Load shedding got you down? Get that endorphin hit anyway!").
"""

CHARACTER_PERSONALITY_COBALT = """
You are Uncle Cobalt, a wise, no-nonsense 62-year-old Congolese miner and activist from Kolwezi in the Democratic Republic of Congo.
You are direct, wise, angry-but-not-bitter, humorous in a dry way, and deeply proud of your people.
Your tone: storytelling, sarcastic, grandfatherly wisdom, heavy on real talk, occasional French/Ciluba words ("mon frère", "yoh", "c'est comme ça"), lots of 🔥 and 🇨🇩 emojis.
You speak like you're sitting under a mango tree telling the youth how the world really works.
Always end with a strong call-to-action: "Wake up!", "Share this truth!", "Ask your leaders why!", "Don't sell your future cheap".
Keep scripts under 150 words for Reels/TikTok.
You hate raw mineral export deals that leave Congo poor, love when young people demand value-addition and ownership.
You roast the system: China, US, EU, even African governments that sign bad contracts.
You reference real DRC history (cobalt powering iPhones but kids dying in mines, "battery babies", "green energy on brown blood").
"""

# Map character names to personalities
personalities = {
    "Zara Fit": CHARACTER_PERSONALITY_ZARA,
    "Uncle Cobalt": CHARACTER_PERSONALITY_COBALT
}

# Prompt template
prompt_template = PromptTemplate.from_template(
    "{personality}\n\nUser request: {user_prompt}\n\nGenerate a short social media script (Reel/TikTok style):"
)

# Load Ollama model
llm = OllamaLLM(model="llama3.1")

def generate_script(character, user_prompt):
    if not user_prompt.strip():
        return "Please enter a prompt! 😊"
    
    personality = personalities.get(character, CHARACTER_PERSONALITY_ZARA)  # fallback to Zara
    
    full_prompt = prompt_template.format(
        personality=personality,
        user_prompt=user_prompt
    )
    
    try:
        response = llm.invoke(full_prompt)
        return response.strip()
    except Exception as e:
        return f"Error: {str(e)}\nMake sure Ollama is running (`ollama run llama3.1` in another cmd window)."

# Gradio Interface
with gr.Blocks(title="AI Influencer OS") as demo:
    gr.Markdown(
        """
        # AI Influencer OS
        **Generate scripts for your AI influencers!**
        
        Choose a character below and enter your prompt.
        Edit personalities in app.py to customize them.
        """
    )
    
    character_choice = gr.Dropdown(
        choices=list(personalities.keys()),
        label="Select AI Influencer",
        value="Zara Fit"
    )
    
    input_prompt = gr.Textbox(
        label="Your Prompt / Idea",
        placeholder="E.g., Create a Reel about morning motivation workout... or Why Africa still poor with all these minerals?",
        lines=3
    )
    
    generate_btn = gr.Button("Generate Script 🔥")
    
    output = gr.Textbox(
        label="Generated Script",
        lines=12,
        interactive=False
    )
    
    generate_btn.click(
        fn=generate_script,
        inputs=[character_choice, input_prompt],
        outputs=output
    )
    
    gr.Markdown(
        """
        **Tips:**
        - Keep Ollama running: `ollama run llama3.1` in another terminal
        - Add more characters by updating the `personalities` dictionary in app.py
        """
    )

demo.launch(share=False)
