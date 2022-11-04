users = int(input())
parking_lot = {}
for user in range(users):
    command = input().split(' ')
    if command[0] == 'register':
        name = command[1]
        license_plate_number = command[2]
        if name in parking_lot:
            print(f'ERROR: already registered with plate number {license_plate_number}')
            continue
        parking_lot[name] = license_plate_number
        print(f"{name} registered {license_plate_number} successfully")
    elif command[0] == 'unregister':
        username = command[1]
        if username not in parking_lot:
            print(f'ERROR: user {username} not found')
            continue
        del parking_lot[username]
        print(f"{username} unregistered successfully")

for user, license_plate in parking_lot.items():
    print(user, '=>', license_plate)