# AI Influencer OS

Self-hosted, open-source platform to create and manage AI influencers from scratch.

Build virtual characters that evolve: persistent personality, long-term memory of posts and interactions (via LangGraph, Ollama, ChromaDB), consistent photoreal images (Flux.1 + IP-Adapter), animated videos (AnimateDiff), realistic lip-sync and voice (MuseTalk / XTTS-v2), full content pipeline, and social media auto-posting.

### Key Goals
- Full ownership — no third-party API fees or limits
- Modular Python code, easy to extend
- Runs locally or on cheap cloud GPUs
- Dashboard for generation, editing, and scheduling

## Features (Roadmap)
- Character bible + evolving memory
- End-to-end: script → image → video → talking clip
- Gradio / Streamlit UI (upgrading to Next.js + FastAPI)
- Auto-post to Instagram / TikTok / YouTube
- Feedback loop from comments → memory updates

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/Enthunya/ramodulela-ai-influencer-os.git

# 2. Enter the directory
cd ramodulela-ai-influencer-os

# 3. Create and activate virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
# source venv/bin/activate

# 4. Install dependencies (once we add requirements.txt)
pip install -r requirements.txt

# 5. Run the dashboard (once app.py is created)
python app.py
