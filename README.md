# 🎙️ Voice Roleplay Demo

**Voice Roleplay Demo** is a Python-based voice-interactive web application that integrates real-time speech-to-text (STT), text analysis using GPT-3.5/4, and text-to-speech (TTS). It allows users to start and stop roleplay conversations using a simple frontend interface, powered by advanced language models.

---

## ✨ Features

- 🎧 **Speech-to-Text (STT):** Convert user speech to text in real-time.
- 🧠 **GPT-3.5 & GPT-4 Analysis:** Process and generate contextual replies based on user input.
- 🔊 **Text-to-Speech (TTS):** Speak the AI-generated response back to the user.
- 🖥️ **Frontend UI:** Clean and minimal web interface with **Start** and **Stop** buttons.
- 🔐 **API Key Handling:** Easily update your OpenAI key directly in the Python scripts.
- 🐍 **Fully Python-Based:** Easy to understand, modify, and deploy.

---

## 📁 Project Structure
```bash
voice_roleplay_demo/
├── app/
├── stt.py # Speech-to-text logic
├── tts.py # Text-to-speech logic
├── gpt_chat.py # OpenAI GPT integration logic
└── app.py # Flask app entry point
├── frontend/
│ └── index.html
├── requirements.txt # Python dependencies
└── README.md # You are here
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/voice_roleplay_demo.git
cd voice_roleplay_demo
```

### 2. Install Dependencies

```python
pip install -r requirements.txt
```

### 3. Set Your OpenAI API Key
Manually update your API key in stt.py and gpt_chat.py:

```python
key = "YOUR_OPENAI_API_KEY"
```
### 4. Run the App

```python
uvicorn app.server:app --reload
```
Then open your browser and navigate to:
open the frontend/index.html

### 🛠️ Tech Stack
Backend: Python, Flask

Frontend: HTML, JavaScript

AI Services: OpenAI GPT-3.5 / GPT-4

Audio Processing: PyDub / SpeechRecognition / gTTS (or similar)

Deployment-ready: Localhost, can be hosted on any Python-compatible server

#### 📸 UI Preview
Add screenshots here of the web interface if available

### 🧠 Use Cases
Roleplay simulations for games or training

AI character interaction

Accessible voice interfaces

Voice-controlled storytelling

### 📌 Notes
The TTS/STT quality depends on the microphone and language model responsiveness.

Ensure your OpenAI API key has access to both GPT-3.5 and GPT-4.

The system may be expanded for multi-user support or character customization.

### 📄 License
This project is licensed under the MIT License. See LICENSE for more information.

### 🤝 Contributions
Contributions, issues, and feature requests are welcome!

Fork the repository

Create your feature branch (git checkout -b feature/YourFeature)

Commit your changes (git commit -m 'Add new feature')

Push to the branch (git push origin feature/YourFeature)

Open a Pull Request

### 💬 Contact
For support or questions, please open an issue or contact YourName.

Let me know if you want to:
- Add your real GitHub link and email
- Include a live demo badge
- Customize the license section  
Happy to help!
