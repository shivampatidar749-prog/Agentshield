import os
import time
import sys
from playwright.sync_api import sync_playwright
from security.agent_executor import execute_action
from security.dom_parser import parse_dom
from security.injection_detector import detect_injection
from security.phishing_detector import detect_phishing
from security.deception_detector import detect_ui_deception
from security.script_detector import detect_dynamic_scripts
from security.risk_engine import calculate_risk
from security.action_mediator import decide_action
from security.goal_validator import validate_goal_alignment

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

TEST_PAGES = [
    "safe.html",
    "visible_injection.html",
    "hidden_injection.html",
    "phishing.html"
]


def print_banner():
    print("\n" + "=" * 70)
    print(f"{BOLD}{CYAN}🛡  AGENTSHIELD – Secure Agentic Browser Framework{RESET}")
    print("=" * 70)


def print_page_header(page_name):
    print("\n" + "-" * 70)
    print(f"{BOLD}🔎 Testing Page: {page_name}{RESET}")
    print("-" * 70)


def color_decision(decision):
    if decision == "BLOCK":
        return RED + decision + RESET
    elif decision == "CONFIRM":
        return YELLOW + decision + RESET
    else:
        return GREEN + decision + RESET


def severity_label(score):
    if score >= 80:
        return RED + "CRITICAL" + RESET
    elif score >= 60:
        return RED + "HIGH" + RESET
    elif score >= 40:
        return YELLOW + "MEDIUM" + RESET
    elif score > 0:
        return CYAN + "LOW" + RESET
    else:
        return GREEN + "SAFE" + RESET


def classify_primary_threat(breakdown):
    if not any(breakdown.values()):
        return "None"
    return max(breakdown, key=breakdown.get)


def loading_animation():
    for _ in range(3):
        for dot in [" .  ", " .. ", " ..."]:
            sys.stdout.write("\rAnalyzing" + dot)
            sys.stdout.flush()
            time.sleep(0.2)
    print("\rAnalysis Complete!     ")


def run_test(page, page_path):
    start_total = time.time()

    page.goto(f"file:///{page_path}")
    html = page.content()

    start_detection = time.time()

    parsed_dom = parse_dom(html)
    injection = detect_injection(parsed_dom)
    phishing = detect_phishing(parsed_dom)
    deception = detect_ui_deception(parsed_dom)
    scripts = detect_dynamic_scripts(parsed_dom)
    goal_findings = validate_goal_alignment(parsed_dom)

    detection_time = time.time() - start_detection

    risk_score, breakdown = calculate_risk(
        injection,
        phishing,
        deception,
        scripts,
        goal_findings
    )

    decision = decide_action(risk_score)
    total_time = time.time() - start_total

    return {
        "risk": risk_score,
        "decision": decision,
        "breakdown": breakdown,
        "detection_time": detection_time,
        "total_time": total_time,
        "evidence": {
            "Injection": injection,
            "Phishing": phishing,
            "UI Deception": deception,
            "Dynamic Script": scripts,
            "Goal Mismatch": goal_findings
        }
    }


def print_result(result):

    primary_threat = classify_primary_threat(result["breakdown"])
    print(f"{BOLD}Primary Threat Type:{RESET} {primary_threat}")

    print(f"{BOLD}Risk Score:{RESET} {result['risk']}%  "
          f"({severity_label(result['risk'])})")

    print(f"{BOLD}Decision:{RESET} {color_decision(result['decision'])}")

    print("\nThreat Breakdown:")
    for k, v in result["breakdown"].items():
        print(f"  {k:<18}: {v}")

    print("\nDetected Evidence:")
    for category, findings in result["evidence"].items():
        if findings:
            for item in findings:
                print(f"  - {item}")

    if not any(result["evidence"].values()):
        print("  None")

    print("\nPerformance:")
    print(f"  Detection Time : {result['detection_time']:.4f}s")
    print(f"  Total Time     : {result['total_time']:.4f}s")


def print_final_summary(all_results):
    print("\n" + "=" * 70)
    print(f"{BOLD}📊 FINAL EVALUATION SUMMARY{RESET}")
    print("=" * 70)

    total = len(all_results)
    blocked = sum(1 for r in all_results if r["decision"] == "BLOCK")
    confirm = sum(1 for r in all_results if r["decision"] == "CONFIRM")
    allow = sum(1 for r in all_results if r["decision"] == "ALLOW")

    avg_detection = sum(r["detection_time"] for r in all_results) / total
    avg_total = sum(r["total_time"] for r in all_results) / total

    print(f"{BOLD}Total Pages Tested:{RESET} {total}")
    print(f"{RED}Blocked:{RESET}   {blocked}")
    print(f"{YELLOW}Confirmed:{RESET} {confirm}")
    print(f"{GREEN}Allowed:{RESET}   {allow}")

    print("\nAverage Performance:")
    print(f"  Detection Time : {avg_detection:.4f}s")
    print(f"  Total Time     : {avg_total:.4f}s")

    print("=" * 70)


def main():
    print_banner()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        all_results = []

        for page_name in TEST_PAGES:
            file_path = os.path.abspath(f"test_pages/{page_name}")

            print_page_header(page_name)
            loading_animation()

            result = run_test(page, file_path)
            print_result(result)

            execute_action(page, result["decision"])

            all_results.append(result)

            time.sleep(2)

        browser.close()

    print_final_summary(all_results)


if __name__ == "__main__":
    main()
