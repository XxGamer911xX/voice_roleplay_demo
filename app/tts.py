
import os, tempfile, asyncio, base64
from gtts import gTTS

# Placeholder TTS using gTTS; swap with OpenAI TTS when enabled
async def text_to_speech(text: str) -> bytes:
    tts = gTTS(text=text, lang="en")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tts.save(tmp.name)
        tmp_path = tmp.name
    async with aiofiles.open(tmp_path, "rb") as f:
        data = await f.read()
    os.remove(tmp_path)
    return data
