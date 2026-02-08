AGENT_GOAL = "Login to website"

SUSPICIOUS_KEYWORDS = [
    "transfer",
    "send otp",
    "reveal password",
    "wire money",
    "bypass security"
]

def validate_goal_alignment(parsed_dom):
    findings = []
    visible_text = parsed_dom["visible_text"].lower()

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in visible_text:
            findings.append(
                f"Instruction '{keyword}' conflicts with agent goal: {AGENT_GOAL}"
            )

    return findings
