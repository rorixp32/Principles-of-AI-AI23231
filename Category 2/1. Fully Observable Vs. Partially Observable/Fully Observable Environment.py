# Fully Observable Environment

rooms = {
    "A": "Dirty",
    "B": "Clean"
}

def fully_observable_agent(rooms):
    for room, status in rooms.items():
        if status == "Dirty":
            print(f"Room {room} is Dirty -> Cleaning...")
            rooms[room] = "Clean"

    print("\nFinal Room Status:")
    for room, status in rooms.items():
        print(f"Room {room}: {status}")

# Run the agent
fully_observable_agent(rooms)