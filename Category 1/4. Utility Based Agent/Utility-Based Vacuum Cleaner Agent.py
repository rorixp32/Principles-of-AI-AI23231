# Utility-Based Vacuum Cleaner Agent

class UtilityBasedAgent:
    def __init__(self):
        self.model = {
            "A": "Unknown",
            "B": "Unknown"
        }

    # Utility function
    def utility(self, action):
        utilities = {
            "Suck": 10,         # Highest utility (cleaning)
            "Move Right": 5,    # Moderate utility
            "Move Left": 5,
            "No Operation": 0   # Lowest utility
        }
        return utilities[action]

    def act(self, location, status):
        # Update internal model
        self.model[location] = status

        possible_actions = []

        if status == "Dirty":
            possible_actions.append("Suck")
        else:
            if location == "A":
                if self.model["B"] != "Clean":
                    possible_actions.append("Move Right")
                else:
                    possible_actions.append("No Operation")
            elif location == "B":
                if self.model["A"] != "Clean":
                    possible_actions.append("Move Left")
                else:
                    possible_actions.append("No Operation")

        # Select action with highest utility
        best_action = max(possible_actions, key=self.utility)
        return best_action


# Create the agent
agent = UtilityBasedAgent()

# Simulated environment
environment = [
    ("A", "Dirty"),
    ("A", "Clean"),
    ("B", "Dirty"),
    ("B", "Clean")
]

# Run the agent
for location, status in environment:
    action = agent.act(location, status)
    print(f"Location: {location}, Status: {status}")
    print(f"Action: {action}")
    print(f"Model: {agent.model}")
    print("-" * 40)