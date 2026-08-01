# Partially Observable Environment

rooms = {
    "A": "Dirty",
    "B": "Clean"
}

current_room = "A"

def partially_observable_agent(current_room):
    print(f"Agent is in Room {current_room}")

    if rooms[current_room] == "Dirty":
        print("Room is Dirty -> Cleaning...")
        rooms[current_room] = "Clean"
    else:
        print("Room is already Clean.")

    print("\nCurrent Knowledge:")
    print(f"Room {current_room}: {rooms[current_room]}")
    print("Other room status is Unknown.")

# Run the agent
partially_observable_agent(current_room)