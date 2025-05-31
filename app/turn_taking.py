
class ConversationState:
    """Very small history buffer for context"""

    def __init__(self, max_turns: int = 5):
        self.history: list[tuple[str, str]] = []
        self.max_turns = max_turns

    def add_turn(self, user: str, assistant: str):
        self.history.append((user, assistant))
        if len(self.history) > self.max_turns:
            self.history.pop(0)
