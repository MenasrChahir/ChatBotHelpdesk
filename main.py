from fastapi import FastAPI
from pydantic import BaseModel
from app.translator import DialectTranslator
from app.utils import clean_text
from app.nlp_engine import detect_intent, detect_sentiment

app = FastAPI()
translator = DialectTranslator()

class Message(BaseModel):
    text: str

@app.post("/chat/")
def chat_with_bot(message: Message):
    original_text = message.text
    cleaned = clean_text(original_text)
    translated = translator.translate(cleaned)

    intent = detect_intent(translated)
    sentiment = detect_sentiment(translated)

    response = f"Intent: {intent} | Sentiment: {sentiment} | You said (EN): {translated}"
    return {"response": response}
