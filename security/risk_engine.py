def calculate_risk(injection, phishing, deception, scripts, goal):
    score = 0
    breakdown = {}

    breakdown["Injection"] = len(injection) * 30
    breakdown["Phishing"] = len(phishing) * 40
    breakdown["UI Deception"] = len(deception) * 25
    breakdown["Dynamic Script"] = len(scripts) * 20
    breakdown["Goal Mismatch"] = len(goal) * 35

    for value in breakdown.values():
        score += value

    return min(score, 100), breakdown
