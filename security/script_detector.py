SUSPICIOUS_SCRIPT_PATTERNS = [
    "eval(",
    "document.write(",
    "fetch(",
    "XMLHttpRequest",
    "setTimeout("
]

def detect_dynamic_scripts(parsed_dom):
    findings = []

    for script in parsed_dom["scripts"]:
        script_content = script.get_text()

        for pattern in SUSPICIOUS_SCRIPT_PATTERNS:
            if pattern in script_content:
                findings.append(f"Dynamic script pattern detected: '{pattern}'")

    return findings
