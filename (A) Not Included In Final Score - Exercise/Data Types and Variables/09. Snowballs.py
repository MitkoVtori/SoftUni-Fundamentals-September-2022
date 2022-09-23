# First we check how many snowballs we have.
snowballs = int(input())
max_snowball_weight = 0
max_snowball_time = 0
max_value = 0
max_quality = 0

# After that we check which is better.
for snowball in range(snowballs):
    # Here we check the weight of the snowball.
    snowball_weight = int(input())
    # Here we check the time needed for the snowball to get to its target.
    snowball_time = int(input())
    # Here we check the quality of the snowball.
    quality = int(input())
    # Here we calculate its value by the following formula.
    value = (snowball_weight / snowball_time) ** quality
    # Here we record the weight, speed, quality and value of the best snowball.
    if value > max_value:
        max_snowball_weight = snowball_weight
        max_snowball_time = snowball_time
        max_value = value
        max_quality = quality
# And finally, we print the record of the best snowball.
print(f"{max_snowball_weight} : {max_snowball_time} = {max_value:.0f} ({max_quality})")
