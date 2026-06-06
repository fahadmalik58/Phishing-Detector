import re
from urllib.parse import urlparse

def analyze_url(url):

    score = 0
    reasons = []

    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    # IP Address
    if re.match(r"^\d+\.\d+\.\d+\.\d+$", domain):
        score += 25
        reasons.append("Uses IP address")

    # Long URL
    if len(url) > 75:
        score += 15
        reasons.append("Long URL")

    # Many subdomains
    if len(domain.split(".")) > 3:
        score += 15
        reasons.append("Too many subdomains")

    # Suspicious words
    suspicious_words = [
        "login",
        "verify",
        "update",
        "secure",
        "account",
        "password",
        "bank"
    ]

    for word in suspicious_words:
        if word in url.lower():
            score += 10
            reasons.append(f"Contains '{word}'")

    return min(score, 100), reasons