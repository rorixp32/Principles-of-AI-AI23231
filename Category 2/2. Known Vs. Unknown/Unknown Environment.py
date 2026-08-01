# Unknown Environment

rooms = {
    "A": "Dirty",
    "B": "Clean"
}

def unknown_environment_agent(room):
    print(f"Agent enters Room {room}")

    print("Trying action: SUCK")

    # Agent observes the result after performing the action
    if rooms[room] == "Dirty":
        rooms[room] = "Clean"
        print("Observation: Action worked. Room became Clean.")
    else:
        print("Observation: Room was already Clean.")

    print("\nCurrent Room Status:")
    print(f"Room {room}: {rooms[room]}")

# Run the agent
unknown_environment_agent("A")