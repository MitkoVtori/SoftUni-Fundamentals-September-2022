import re
string = input()
pattern = r"([|#])(\w+(\s\w+|\S))\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
food = re.findall(pattern, string)

needed_calories_per_day = 2000
total_calories = 0

for element in food:
    total_calories += int(element[-1])

days_to_last = total_calories // needed_calories_per_day
print(f"You have food to last you for: {days_to_last} days!")

for elements in food:
    item = elements[1]
    date = elements[3]
    calories = elements[4]
    print(f"Item: {item}, Best before: {date}, Nutrition: {calories}")