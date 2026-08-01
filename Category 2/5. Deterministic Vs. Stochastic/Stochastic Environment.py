# Stochastic Environment

import random

class StochasticEnvironment:
    def __init__(self):
        self.room = "Dirty"

class Agent:
    def __init__(self, env):
        self.env = env

    def act(self):
        print("Initial Room Status:", self.env.room)

        if self.env.room == "Dirty":
            print("Action: Suck")

            # Cleaning may or may not succeed
            success = random.choice([True, False])

            if success:
                self.env.room = "Clean"
                print("Cleaning Successful!")
            else:
                print("Cleaning Failed!")

        else:
            print("Action: No Operation")

        print("Final Room Status:", self.env.room)

# Main Program
env = StochasticEnvironment()
agent = Agent(env)

agent.act()