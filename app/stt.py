from openai import AsyncOpenAI, RateLimitError

key = "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"
client = AsyncOpenAI(api_key=key)

async def transcribe(file_path: str) -> str:
    try:
        with open(file_path, "rb") as audio_file:
            transcript = await client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
            )
            return transcript.text
    except RateLimitError as e:
        print("Rate limit exceeded:", e)
        return "[OpenAI quota exceeded]"