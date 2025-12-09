import random 
subjects = [
    "Rajesh Hamal",
    "Kp Oli",
    "Bishal",
    "A group of monkeys",
    "Hello every one",
    "Auto rickshaw driver from butwal",
    "NPl"
]

actions = [
    "launches",
    "cancles",
    "dances with",
    "eats",
    "declares war on ",
    "orders",
    "celebrates",
    "playing cricket"
]

places_or_things = [
    "kathmandu",
    "Tu ground",
    "at lumbini",
    "mouse",
    "banbatika",
    "ashoka pillar",
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_things = random.choice(places_or_things)

    headline = f"Breaking News: {subject} {action} {places_or_things}"
    print(f"Headline news:\n{headline}")

    user_input = input("Do you want another headline (yes/no)?").strip().lower()
    if user_input == "no":
       break
print("\nThanks for using the fake news line generator Have a fun day")    