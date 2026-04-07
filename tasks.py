TASKS = {
    "easy": {
        "ticket": "My payment failed but money was deducted.",
        "expected": {
            "type": "classify",
            "keyword": "payment"
        }
    },
    "medium": {
        "ticket": "I want a refund for my damaged product.",
        "expected": {
            "type": "respond",
            "keyword": "refund"
        }
    },
    "hard": {
        "ticket": "I received the wrong item and need help.",
        "expected": {
            "type": "multi_step"
        }
    }
}