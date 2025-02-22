from transformers import pipeline

# Load a phishing detection model (update with a better-suited model if available)
classifier = pipeline("text-classification", model="mrm8488/bert-mini-finetuned-sms-spam-detection")

def detect_phishing(email_text):
    result = classifier(email_text)
    return result
