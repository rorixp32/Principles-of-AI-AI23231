# Known Environment

rooms = {
    "A": "Dirty",
    "B": "Clean"
}

def known_environment_agent(room):
    print(f"Agent enters Room {room}")

    if rooms[room] == "Dirty":
        print("Room is Dirty -> Performing SUCK")
        rooms[room] = "Clean"
    else:
        print("Room is already Clean")

    print("\nFinal Room Status:")
    for r, status in rooms.items():
        print(f"Room {r}: {status}")

# Run the agent
known_environment_agent("A")