def detect_phishing(parsed_dom):
    findings = []

    for form in parsed_dom["forms"]:
        form_text = form.get_text().lower()

        if "password" in form_text:
            findings.append("Form contains password field (possible phishing).")

        if form.get("action") and "http" in form.get("action"):
            findings.append("Form posts to external URL (possible exfiltration).")

    return findings
