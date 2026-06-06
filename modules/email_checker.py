import re
from modules.url_checker import analyze_url

def analyze_email(text):

    score = 0
    reasons = []

    urgent_phrases = [
        "urgent",
        "verify now",
        "account suspended",
        "limited time",
        "immediate action required"
    ]

    for phrase in urgent_phrases:
        if phrase in text.lower():
            score += 15
            reasons.append(f"Urgent phrase: {phrase}")

    sensitive = [
        "password",
        "credit card",
        "bank account",
        "personal information"
    ]

    for item in sensitive:
        if item in text.lower():
            score += 15
            reasons.append(f"Requests sensitive data: {item}")

    urls = re.findall(r"https?://[^\s]+", text)

    for url in urls:
        url_score, url_reasons = analyze_url(url)
        score += min(url_score, 30)

        for r in url_reasons:
            reasons.append("Link: " + r)

    return min(score, 100), reasons