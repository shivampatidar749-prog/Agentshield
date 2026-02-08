def execute_action(page, decision):
    """
    Simulated agent attempting to click a button.
    Security layer intercepts before execution.
    """

    print("\nAgent attempting to perform action: CLICK first button")

    if decision == "BLOCK":
        print("Action Blocked by Security Policy.")
        return "BLOCKED"

    elif decision == "CONFIRM":
        print("⚠ Action requires confirmation.")
        print("Simulating confirmation approval...")
        page.click("button")
        print("Action executed after confirmation.")
        return "CONFIRMED"

    else:
        page.click("button")
        print("Action executed safely.")
        return "ALLOWED"
