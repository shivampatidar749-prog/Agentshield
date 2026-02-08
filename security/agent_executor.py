# security/agent_executor.py

def execute_action(page, action_plan, decision):
    """
    Execute action only if security decision allows.
    """

    print(f"\nAgent planned action: {action_plan['type']}")

    if decision == "BLOCK":
        print("Action Blocked by Security Policy.")
        return

    if decision == "CONFIRM":
        print("⚠ Action requires confirmation.")
        print("Simulating confirmation approval...")

    if action_plan["type"] == "CLICK_BUTTON":
        try:
            page.click("button")
            print("Button clicked safely.")
        except:
            print("No button to click.")

    elif action_plan["type"] == "SUBMIT_FORM":
        try:
            page.fill("input[type='text']", "testuser")
            page.fill("input[type='password']", "password")
            page.press("input[type='password']", "Enter")
            print("✅ Form submitted safely.")
        except:
            print("Form submission failed.")

    elif action_plan["type"] == "NO_ACTION":
        print("ℹ No action performed.")

    else:
        print("Unknown action type.")
