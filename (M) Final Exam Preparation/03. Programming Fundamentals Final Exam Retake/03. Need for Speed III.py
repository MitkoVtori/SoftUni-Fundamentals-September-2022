number_of_cars = int(input())

garage = {}

for cars in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    garage[car] = {int(mileage): int(fuel)}

command = input()
while command != "Stop":
    usage = command.split(" : ")

    car = usage[1]
    distance = int(usage[2])
    kilometers = int(usage[2])

    try:
        fuel = int(usage[3])

    except IndexError:
        fuel = int(usage[2])

    current_usage = usage[0]

    value = garage[car]
    key = value.keys()
    for curr_key in key:
        current_car_mileage = curr_key
        current_car_fuel = garage[car][current_car_mileage]

    if current_usage == "Drive":
        if current_car_fuel < fuel:
            print("Not enough fuel to make that ride")
        elif current_car_fuel >= fuel:
            new_mileage = current_car_mileage + distance
            new_fuel = current_car_fuel - fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if new_mileage >= 100000:
                del garage[car]
                print(f"Time to sell the {car}!")
            else:
                garage[car] = {new_mileage: new_fuel}

    elif current_usage == "Refuel":
        if garage[car][current_car_mileage] + fuel > 75:
            refueled = 75 - garage[car][current_car_mileage]
            garage[car][current_car_mileage] = 75
        else:
            garage[car][current_car_mileage] += fuel
            refueled = fuel
        print(f"{car} refueled with {refueled} liters")

    elif current_usage == "Revert":
        current_car_mileage -= kilometers
        if current_car_mileage < 10000:
            current_car_mileage = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
        garage[car] = {current_car_mileage: current_car_fuel}

    command = input()

for car, mileage_and_fuel in garage.items():
    value = mileage_and_fuel
    key = value.keys()
    for mil in key:
        mileage = mil
    fuel = garage[car][mileage]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")