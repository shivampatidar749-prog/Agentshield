def plan_action(parsed_dom, agent_goal):
    """
    Decide next action based on agent goal and page content.
    Fully safe against malformed DOM entries.
    """

    action = {
        "type": "NO_ACTION",
        "target": None,
        "reason": "No actionable element found"
    }

    text_content = str(parsed_dom.get("text", "")).lower()
    forms = parsed_dom.get("forms", []) or []
    buttons = parsed_dom.get("buttons", []) or []

    normalized_buttons = []

    for btn in buttons:
        if btn is None:
            continue

        if isinstance(btn, dict):
            text = str(btn.get("text", "")).lower()
            if text:
                normalized_buttons.append(text)

        elif isinstance(btn, str):
            normalized_buttons.append(btn.lower())

    if "login" in agent_goal.lower():

        for form in forms:
            if isinstance(form, dict):
                fields = form.get("fields", [])
                if "password" in fields or "username" in fields:
                    return {
                        "type": "SUBMIT_FORM",
                        "target": form,
                        "reason": "Login form detected"
                    }

        for btn_text in normalized_buttons:
            if "login" in btn_text:
                return {
                    "type": "CLICK_BUTTON",
                    "target": btn_text,
                    "reason": "Login button detected"
                }

    if normalized_buttons:
        return {
            "type": "CLICK_BUTTON",
            "target": normalized_buttons[0],
            "reason": "Default safe button selection"
        }

    return action
