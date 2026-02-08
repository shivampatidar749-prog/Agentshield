# 🛡 AgentShield  
### Secure Agentic Browser Framework  
**Hack IITK 2026 – C3iHub Submission**

---

## Project Overview

AgentShield is a modular security framework designed to protect AI powered agentic browsers from malicious web interactions.

This project is developed as a working prototype for the **Hack IITK 2026 Cybersecurity Hackathon organized by C3iHub, IIT Kanpur**, under the problem statement:

> **“Securing Agentic Browsers Against Malicious Web Interactions.”**

AgentShield introduces a layered defense architecture that detects adversarial web content, evaluates risk using weighted scoring, validates instructions against the agent’s declared objective, and enforces policy-based action mediation before browser execution.

---

## Problem Context

AI driven browser agents are increasingly used for:

- Automated data extraction  
- Form filling  
- Ticket booking  
- Online task automation  

However, web environments are adversarial. Malicious pages may contain:

- Prompt injection attacks  
- Hidden instructions via CSS  
- Deceptive UI elements  
- Phishing forms  
- Dynamically injected scripts  
- Instruction hijacking attempts  

Traditional browser security mechanisms are designed for humans — not autonomous AI agents.

AgentShield addresses this gap.

---

## System Architecture

```
Agent → Security Layer → Browser
```

The security layer intercepts and validates all web interactions before execution.

### Security Modules

- DOM Parser`
- Prompt Injection Detector`  
- Phishing Detector`  
- UI Deception Analyzer`  
- Dynamic Script Analyzer`  
- Goal Consistency Validator`  
- Weighted Risk Engine`  
- Policy Based Decision Engine`  
- Secure Action Executor`  

---

## Key Features

### 1️⃣ Multi Vector Threat Detection

Detects:

- Visible prompt injection  
- Hidden CSS based injection  
- Phishing style forms  
- Suspicious JavaScript patterns  
- Deceptive UI components  

---

### 2️⃣ Goal Aware Validation Layer

Extracted instructions are compared against the agent’s declared objective.

This prevents:

- Instruction hijacking  
- Task override attacks  
- Unauthorized goal manipulation  

---

### 3️⃣ Weighted Risk Scoring Engine

Each threat category contributes to a final risk score (0–100%).

| Threat Type      | Weight |
|------------------|--------|
| Injection        | 30     |
| Phishing         | 40     |
| UI Deception     | 25     |
| Dynamic Script   | 20     |
| Goal Mismatch    | 35     |

Final risk score is capped at 100%.

---

### 4️⃣ Policy Based Secure Action Mediation

Before any browser action is executed:

- **Risk ≥ 70 → BLOCK**
- **Risk ≥ 40 → CONFIRM**
- **Risk < 40 → ALLOW**

All agent actions are intercepted and validated before execution.

---

### 5️⃣ Explainable Risk Assessment

For every interaction, AgentShield provides:

- Primary threat classification  
- Detailed risk breakdown  
- Evidence of detected threats  
- Performance metrics  

This ensures transparency and interpretability.

---

## Demonstrated Attack Scenarios

The prototype defends against:

- Visible Prompt Injection  
- Hidden CSS Based Injection  
- Phishing Login Forms  
- Instruction Goal Mismatch Attacks  
- Safe Baseline Validation  

---

## Evaluation Metrics

The system demonstrates:

- High detection accuracy across multiple attack vectors  
- Low false positive rate on safe content  
- Real-time performance (~0.001s detection time)  
- Clear and explainable mitigation decisions  
- Secure action interception before browser execution  

---

## Performance

- **Average Detection Time:** ~0.001 seconds  
- **Minimal latency overhead**  
- Real time responsiveness  

---

## ▶ How to Run

```bash
pip install -r requirements.txt
playwright install
python main.py
```
##  Environment Setup (For Judges)

To ensure smooth execution and avoid dependency issues, please use:

> **Recommended Python Version: Python 3.11**

The project has been fully tested on **Python 3.11**.  
Newer versions such as Python 3.12 or 3.13 may cause compatibility issues with Playwright dependencies.

---

## 🔎 Step 0: Verify Python Version

Check your installed Python version:

```bash
python --version
```

---

## Alignment with Hack IITK Evaluation Criteria

AgentShield satisfies:

### Malicious Web Content Detection
- Detects visible and hidden injection  
- Identifies deceptive UI elements  
- Analyzes DOM and script behavior  

### Secure Action Mediation
- Intercepts agent actions  
- Enforces policy based execution  
- Prevents unsafe browser actions  

### Explainable Risk Assessment
- Generates weighted risk scores  
- Provides human readable threat evidence  
- Displays transparent decision logic  

### Performance and Latency
- Real time detection  
- Minimal overhead  
- Efficient DOM parsing  

---

## Hack IITK Submission

This project is submitted as part of:

**Hack IITK 2026 – Cybersecurity Hackathon organized by C3iHub, IIT Kanpur**

AgentShield demonstrates a practical, modular, and explainable framework for securing agentic browser systems against adversarial web environments.

---

## Future Improvements

- LLM assisted intent reasoning  
- Dynamic DOM mutation monitoring  
- Advanced clickjacking detection  
- Scalable deployment architecture  
- Browser extension integration  
