# Model-Based Vacuum Cleaner Agent

class ModelBasedAgent:
    def __init__(self):
        # Internal model of the environment
        self.model = {
            "A": "Unknown",
            "B": "Unknown"
        }

    def act(self, location, status):
        # Update internal model
        self.model[location] = status

        # Decide action
        if status == "Dirty":
            return "Suck"

        # If current location is clean, check the other room
        if location == "A":
            if self.model["B"] != "Clean":
                return "Move Right"
            else:
                return "No Operation"
        else:  # location == "B"
            if self.model["A"] != "Clean":
                return "Move Left"
            else:
                return "No Operation"

# Create the agent
agent = ModelBasedAgent()

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
    print(f"Internal Model: {agent.model}")
    print("-" * 40)