# Continuous Environment

class ContinuousEnvironment:
    def __init__(self):
        self.position = 0.0

class Agent:
    def __init__(self, env):
        self.env = env

    def move(self, distance):
        print("Current Position:", self.env.position)

        self.env.position += distance

        print("Moved by:", distance)
        print("New Position:", self.env.position)

# Main Program
env = ContinuousEnvironment()
agent = Agent(env)

agent.move(2.5)