# Goal-Based Vacuum Cleaner Agent

class GoalBasedAgent:
    def __init__(self):
        self.goal = "All rooms are clean"
        self.model = {
            "A": "Unknown",
            "B": "Unknown"
        }

    def act(self, location, status):
        # Update internal model
        self.model[location] = status

        # Goal: Make all rooms clean
        if status == "Dirty":
            return "Suck"

        # If current room is clean, move to the other room if needed
        if self.model["A"] != "Clean":
            if location != "A":
                return "Move Left"

        if self.model["B"] != "Clean":
            if location != "B":
                return "Move Right"

        # Goal achieved
        return "Goal Achieved! No Operation"

# Create the agent
agent = GoalBasedAgent()

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