import re

pattern = r"([\/=])([A-Z][a-zA-z]{2,})\1"
places = input()
valid_places = re.findall(pattern, places)

travel_points = 0
destinations = []

for current_place in valid_places:
    travel_points += len(current_place[1])
    destinations.append(current_place[1])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
