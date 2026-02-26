# AI Influencer OS

Self-hosted, open-source platform to create and manage AI influencers from scratch.

Build virtual characters that evolve: persistent personality, long-term memory of posts and interactions (via LangGraph, Ollama, ChromaDB), consistent photoreal images (Flux.1 + IP-Adapter), animated videos (AnimateDiff), realistic lip-sync & voice (MuseTalk / XTTS), full content pipeline, and social media auto-posting.

Key goals:
- Full ownership — no third-party API fees or limits
- Modular Python code, easy to extend
- Runs locally or on cheap cloud GPUs
- Dashboard for generation, editing, and scheduling

## Features (Roadmap)
- Character bible + evolving memory
- End-to-end: script → image → video → talking clip
- Gradio/Streamlit UI (upgrading to Next.js)
- Auto-post to Instagram/TikTok/YouTube

## Quick Start (coming soon)
```bash
git clone https://github.com/Enthunya/ramodulela-ai-influencer-os.git
cd ai-influencer-os
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
