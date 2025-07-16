import json

def load_classes():
    with open("data/classes.json") as f:
        return json.load(f)

def save_classes(classes):
    with open("data/classes.json", "w") as f:
        json.dump(classes, f, indent=2)

def load_bookings():
    with open("data/bookings.json") as f:
        return json.load(f)

def save_bookings(bookings):
    with open("data/bookings.json", "w") as f:
        json.dump(bookings, f, indent=2)
