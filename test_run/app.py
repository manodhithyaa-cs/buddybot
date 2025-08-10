# Install dependencies:
# pip install transformers

from transformers import pipeline

# 1. Sentiment Analysis
sentiment_analyzer = pipeline("sentiment-analysis")

# 2. DialoGPT Chatbot
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

# Conversation history
history = []

print("BuddyBot 🤖: Hi! I’m your buddy. Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("BuddyBot 🤖: Bye! Take care 💙")
        break

    # Step 1: Sentiment check
    sentiment = sentiment_analyzer(user_input)[0]
    if sentiment["label"] == "NEGATIVE":
        print("BuddyBot 🤖: I can sense you’re feeling low. Want to talk about it?")
    elif sentiment["label"] == "POSITIVE":
        print("BuddyBot 🤖: That’s awesome! 😄 Tell me more!")
    else:
        print("BuddyBot 🤖: Okay, I’m listening.")

    # Step 2: Build context from history
    history.append(f"You: {user_input}")
    prompt = "\n".join(history) + "\nBuddyBot:"

    # Step 3: Generate response
    response = chatbot(prompt, max_length=200, pad_token_id=50256)
    bot_reply = response[0]["generated_text"].split("BuddyBot:")[-1].strip()

    print("BuddyBot 🤖:", bot_reply)

    # Add bot reply to history
    history.append(f"BuddyBot: {bot_reply}")
