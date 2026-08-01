# Static Environment

class StaticEnvironment:
    def __init__(self):
        self.room = "Dirty"

class Agent:
    def __init__(self, env):
        self.env = env

    def act(self):
        print("Initial Room Status:", self.env.room)

        if self.env.room == "Dirty":
            print("Action: Suck")
            self.env.room = "Clean"
        else:
            print("Action: No Operation")

        print("Final Room Status:", self.env.room)

# Main Program
env = StaticEnvironment()
agent = Agent(env)

agent.act()