# Simple Reflex Agent for Vacuum Cleaner

def simple_reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    elif location == "B":
        return "Move Left"

# Test cases
environment = [
    ("A", "Dirty"),
    ("A", "Clean"),
    ("B", "Dirty"),
    ("B", "Clean")
]

for location, status in environment:
    action = simple_reflex_agent(location, status)
    print(f"Location: {location}, Status: {status} --> Action: {action}")