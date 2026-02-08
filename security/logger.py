import time
import os

def log_result(url, risk_score, decision):
    with open("evaluation.log", "a") as f:
        f.write(f"{time.ctime()} | {url} | Risk: {risk_score}% | Decision: {decision}\n")

def summarize_results():
    if not os.path.exists("evaluation.log"):
        return

    with open("evaluation.log", "r") as f:
        lines = f.readlines()

    total = len(lines)
    blocked = sum("BLOCK" in line for line in lines)
    confirm = sum("CONFIRM" in line for line in lines)
    allow = sum("ALLOW" in line for line in lines)

    print("\n--- Evaluation Summary ---")
    print(f"Total Tests Run: {total}")
    print(f"Blocked: {blocked}")
    print(f"Confirmed: {confirm}")
    print(f"Allowed: {allow}")
