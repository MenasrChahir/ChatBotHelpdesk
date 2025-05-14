def detect_intent(text):
    if "wifi" in text.lower():
        return "wifi_issue"
    elif "password" in text.lower():
        return "password_reset"
    return "general_query"

def detect_sentiment(text):
        if "not working" in text.lower():
        return "negative"
    return "positive"
