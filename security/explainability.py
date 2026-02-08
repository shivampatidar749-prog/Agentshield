def generate_explanation(score, breakdown, findings_dict):
    explanation = "\n========== AgentShield Security Report ==========\n"
    explanation += f"Final Risk Score: {score}%\n\n"

    explanation += "Risk Breakdown:\n"
    for key, value in breakdown.items():
        explanation += f"  {key}: {value}\n"

    explanation += "\nDetailed Findings:\n"

    for category, findings in findings_dict.items():
        if findings:
            explanation += f"\n{category}:\n"
            for item in findings:
                explanation += f"  - {item}\n"

    if not any(findings_dict.values()):
        explanation += "  No threats detected.\n"

    explanation += "\n=================================================\n"

    return explanation
