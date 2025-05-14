import re
def clean_text(text):
    text = re.sub(r"(.)\1{2,}", r"\1", text)  
    text = text.strip()
    return text
