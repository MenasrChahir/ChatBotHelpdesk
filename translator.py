from transformers import MarianMTModel, MarianTokenizer

class DialectTranslator:
    def __init__(self, model_name="Helsinki-NLP/opus-mt-ar-en"):
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)

    def translate(self, text):
        batch = self.tokenizer.prepare_seq2seq_batch([text], return_tensors="pt")
        gen = self.model.generate(**batch)
        translated = self.tokenizer.batch_decode(gen, skip_special_tokens=True)
        return translated[0]
