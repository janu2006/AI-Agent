def compute_reward(action, expected, step_count):
    score = 0.0

    # Correct action type
    if action.action_type == expected.get("type"):
        score += 0.4

    # Keyword match
    if action.content and expected.get("keyword"):
        if expected["keyword"].lower() in action.content.lower():
            score += 0.4

    # Efficiency reward
    if step_count <= 3:
        score += 0.2

    # Penalty for invalid action
    if action.action_type not in ["classify", "respond", "escalate", "request_info"]:
        score -= 0.3

    # Penalty for too many steps
    if step_count > 4:
        score -= 0.2

    return max(0.0, min(score, 1.0))