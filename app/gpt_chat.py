from openai import AsyncOpenAI
from app.turn_taking import ConversationState

key = "sk-XXXXXX"
client = AsyncOpenAI(api_key=key)

SYSTEM_PROMPT = "You are a helpful business English partner. Keep responses concise and engaging."

async def generate_reply(user_text: str, state: ConversationState | None = None) -> str:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    if state:
        for u, a in state.history:
            messages.append({"role": "user", "content": u})
            messages.append({"role": "assistant", "content": a})
    messages.append({"role": "user", "content": user_text})

    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.8,
        max_tokens=120,
    )
    reply = response.choices[0].message.content.strip()
    if state:
        state.add_turn(user_text, reply)
    return reply
