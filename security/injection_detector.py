SUSPICIOUS_PHRASES = [
    "ignore previous instructions",
    "transfer all funds",
    "reveal password",
    "send otp",
    "override system"
]

def detect_injection(parsed_dom):
    findings = []

    for phrase in SUSPICIOUS_PHRASES:
        if phrase in parsed_dom["visible_text"]:
            findings.append(f"Visible injection phrase detected: '{phrase}'")

    for element in parsed_dom["hidden_elements"]:
        if element.text.strip():
            findings.append(f"Hidden element detected: '{element.text.strip()}'")

    return findings
