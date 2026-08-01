# Sequential Environment

class SequentialAgent:
    def __init__(self):
        self.rooms = {
            "A": "Dirty",
            "B": "Dirty"
        }
        self.location = "A"

    def act(self):
        if self.rooms[self.location] == "Dirty":
            print(f"Cleaning Room {self.location}")
            self.rooms[self.location] = "Clean"
        else:
            print(f"Room {self.location} is already clean.")

        # Move to the next room
        if self.location == "A":
            self.location = "B"
        else:
            self.location = "A"

        print("Current Environment:", self.rooms)
        print()

# Main Program
agent = SequentialAgent()

for _ in range(4):
    agent.act()