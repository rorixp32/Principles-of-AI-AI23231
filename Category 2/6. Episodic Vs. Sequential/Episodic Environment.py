# Episodic Environment

class EpisodicAgent:
    def __init__(self):
        pass

    def act(self, status):
        if status == "Dirty":
            return "Suck"
        else:
            return "No Operation"

# Main Program
agent = EpisodicAgent()

episodes = ["Dirty", "Clean", "Dirty", "Clean"]

for i, status in enumerate(episodes, start=1):
    action = agent.act(status)
    print(f"Episode {i}")
    print(f"Room Status : {status}")
    print(f"Action      : {action}")
    print()