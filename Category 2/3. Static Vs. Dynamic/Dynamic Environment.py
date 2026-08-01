# Dynamic Environment

import random

class DynamicEnvironment:
    def __init__(self):
        self.room = "Dirty"

    def change_environment(self):
        # Environment changes automatically
        self.room = random.choice(["Dirty", "Clean"])

class Agent:
    def __init__(self, env):
        self.env = env

    def act(self):
        print("Initial Room Status:", self.env.room)

        # Environment changes before the agent acts
        self.env.change_environment()
        print("Room Status After Change:", self.env.room)

        if self.env.room == "Dirty":
            print("Action: Suck")
            self.env.room = "Clean"
        else:
            print("Action: No Operation")

        print("Final Room Status:", self.env.room)

# Main Program
env = DynamicEnvironment()
agent = Agent(env)

agent.act()