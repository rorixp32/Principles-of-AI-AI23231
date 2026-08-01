# Discrete Environment

class DiscreteEnvironment:
    def __init__(self):
        self.rooms = ["A", "B", "C"]
        self.location = "A"

class Agent:
    def __init__(self, env):
        self.env = env

    def move(self):
        print("Current Location:", self.env.location)

        if self.env.location == "A":
            self.env.location = "B"
        elif self.env.location == "B":
            self.env.location = "C"
        else:
            print("Already at the last room.")

        print("New Location:", self.env.location)

# Main Program
env = DiscreteEnvironment()
agent = Agent(env)

agent.move()