import random 

subjects = [
    "Rajesh Hamal",
    "KP Oli",
    "Bishal",
    "A group of monkeys",
    "Hello everyone",
    "Auto rickshaw driver from Butwal",
    "NPL"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates",
    "playing cricket"
]

places_or_things = [
    "Kathmandu",
    "TU ground",
    "at Lumbini",
    "mouse",
    "Banbatika",
    "Ashoka pillar",
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"Breaking News: {subject} {action} {place_or_thing}"
    print(f"\nHeadline news:\n{headline}")

    user_input = input("Do you want another headline (yes/no)? ").strip().lower()
    if user_input == "no":
       break

print("\nThanks for using the fake news headline generator. Have fun!")
