# 🤖 Buddy Bot

Buddy Bot is an AI-powered conversational companion that understands your emotions, chats naturally, and can cheer you up when you’re feeling low.  
It uses **Hugging Face Transformers** for sentiment analysis and conversational AI.

## ✨ Features
- 💬 Natural conversation powered by pre-trained models.
- 😊 Sentiment detection (Positive / Negative / Neutral).
- 🫂 Mood-based responses (comfort when sad, hype when happy).
- 🛠 Easily extendable with emotion detection, jokes, or motivational messages.
- 🖥 Works locally or via Hugging Face APIs.

## 🚀 Tech Stack
- **Python 3.8+**
- [Hugging Face Transformers](https://huggingface.co/transformers)
- **Models Used:**
  - Sentiment Analysis: `distilbert-base-uncased-finetuned-sst-2-english`
  - Conversational AI: `microsoft/DialoGPT-medium`

## 📦 Installation
```bash
# Clone the repo
git clone https://github.com/your-username/buddy-bot.git
cd buddy-bot

# Install dependencies
pip install transformers
