
from fastapi import FastAPI, WebSocket, UploadFile, File
from fastapi.responses import HTMLResponse
import asyncio
from app import gpt_chat, stt, tts, turn_taking
import base64, uuid, tempfile, os

app = FastAPI(title="Voice Roleplay Demo")

# Simple HTTP version (type text, get audio)
@app.post("/chat")
async def chat_endpoint(prompt: str):
    reply_text = await gpt_chat.generate_reply(prompt)
    audio_bytes = await tts.text_to_speech(reply_text)
    b64_audio = base64.b64encode(audio_bytes).decode()
    return {"reply": reply_text, "audio": b64_audio}

# WebSocket for real‑time audio exchange
@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    state = turn_taking.ConversationState()
    while True:
        data = await ws.receive_json()
        if data["type"] == "audio_chunk":
            # receive base64 wav chunk from client
            audio_b64 = data["payload"]
            audio_bytes = base64.b64decode(audio_b64)
            # simple: save temp file, transcribe whole thing
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(audio_bytes)
                tmp_path = tmp.name
            text = await stt.transcribe(tmp_path)
            os.remove(tmp_path)
            if text.strip():
                reply = await gpt_chat.generate_reply(text, state)
                audio_bytes = await tts.text_to_speech(reply)
                b64_audio = base64.b64encode(audio_bytes).decode()
                await ws.send_json({"type": "assistant", "text": reply, "audio": b64_audio})
        elif data["type"] == "ping":
            await ws.send_json({"type": "pong"})
