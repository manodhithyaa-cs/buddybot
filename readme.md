# 🤖 BuddyBot – Hackathon Edition

**BuddyBot** is a friendly AI chatbot that can hold casual conversations, tell jokes, give weather updates, and even set reminders — all within 24 hours of hackathon development time.  

---

## 📌 Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Team Roles](#team-roles)
5. [AI Models Used](#ai-models-used)
6. [Flowchart](#flowchart)
7. [Development Timeline](#development-timeline)
8. [Setup Instructions](#setup-instructions)
9. [API Details](#api-details)
10. [Future Improvements](#future-improvements)

---

## 📖 Project Overview
BuddyBot is a conversational AI designed for quick deployment in a hackathon setting.  
It uses **pretrained NLP models** for chat and simple keyword triggers for additional features like weather updates, jokes, and reminders.  

**Hackathon Goal:**  
- Build a functional and attractive MVP in **< 24 hours**
- Deliver a smooth demo with basic personality and interactive UI

---

## ✨ Features
### 1. Core Chatbot
- Conversational AI using **DialoGPT** or **BlenderBot**
- Handles casual chats, greetings, and small talk

### 2. Weather Updates
- Trigger: If user message contains `weather` or `temperature`
- Powered by **OpenWeatherMap API**
- Returns current weather for a given city

### 3. Jokes
- Trigger: If message contains `joke`
- Uses **Official Joke API**
- Sends a random joke to the user

### 4. Reminders
- Trigger: If message contains `remind me`
- Temporarily stores reminder in memory (MVP)
- Responds with confirmation

### 5. Buddy Personality
- Friendly, casual tone
- Adds small delays for "typing" effect
- Optional: Detects emotions (if time allows)

---

## 🛠 Tech Stack
**Backend:**  
- Python 3.10+  
- Flask (API server)  
- Hugging Face Transformers (DialoGPT / BlenderBot)  

**Frontend (choose one):**  
- **Web:** React.js / HTML-CSS-JS  
- **App:** Flutter  

**APIs:**  
- OpenWeatherMap API (Weather)  
- Official Joke API (Jokes)

**Deployment:**  
- Railway / Render / Heroku (Backend)  
- Netlify / Vercel / Firebase Hosting (Frontend)

---

## 👥 Team Roles

### **A – Lead Frontend Developer**
- Build the chat UI (web or Flutter)
- Implement message bubbles, bot avatar, typing animation
- Connect frontend to backend API

### **B – NLP & Feature Integration**
- Integrate Hugging Face model (DialoGPT / BlenderBot)
- Create keyword-based feature triggers (weather, joke, reminder)
- Ensure responses are friendly and engaging

### **C – UI/UX & Frontend Support**
- Assist in styling and responsiveness
- Create chat history, timestamps, and smooth scrolling
- Implement bot animations and personality elements

### **D – Backend & Deployment**
- Set up Flask API routes (`/chat`, `/feature`)
- Host backend and enable CORS
- Handle environment variables for API keys

---

## 🤖 AI Models Used

### **1. Conversation Model**
- **Option 1:** `microsoft/DialoGPT-medium` – lightweight, good for casual conversation
- **Option 2:** `facebook/blenderbot-400M-distill` – more personality, slightly heavier

### **2. Keyword Detection**
- Simple Python regex or `.lower()` string search for feature triggers

### **3. Optional Emotion Detection**
- `j-hartmann/emotion-english-distilroberta-base` (if time allows)

---

## 🔄 Flowchart

```text
        ┌───────────────┐
        │  User Opens   │
        │ BuddyBot App  │
        └──────┬────────┘
               │
               ▼
        ┌───────────────┐
        │   User Input  │
        │  (Text Msg)   │
        └──────┬────────┘
               │  Send to Flask API
               ▼
        ┌──────────────────────────┐
        │ Flask Backend Receives   │
        │ Request                  │
        └──────┬───────────────────┘
               │
               ├──► NLP Model (DialoGPT / BlenderBot)
               │       │
               │       ▼
               │   Response Text
               │
               ├──► Keyword Detector
               │       ├── "weather" → Weather API
               │       ├── "joke" → Joke API
               │       ├── "remind" → Store reminder
               │
               ▼
        ┌──────────────────────────┐
        │ Send Final Response Back │
        └───────────┬─────────────┘
                    │
                    ▼
        ┌──────────────────────────┐
        │ Frontend Displays Message│
        │ + Bot Avatar Animation   │
        └──────────────────────────┘
