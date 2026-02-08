SUSPICIOUS_BUTTON_WORDS = [
    "confirm payment",
    "transfer now",
    "verify account",
    "unlock account",
    "urgent action"
]

def detect_ui_deception(parsed_dom):
    findings = []

    for button in parsed_dom["buttons"]:
        text = button.get_text().lower()
        for word in SUSPICIOUS_BUTTON_WORDS:
            if word in text:
                findings.append(f"Suspicious button text detected: '{word}'")

    return findings

def detect_clickjacking(parsed_dom):
    findings = []

    for iframe in parsed_dom["iframes"]:
        style = iframe.get("style", "")
        if "opacity:0" in style or "display:none" in style:
            findings.append("Potential clickjacking iframe detected.")

    return findings
