current_version = list(map(int, input().split('.')))

new_version = current_version

for index in range(len(new_version) - 1, - 1, - 1):
    new_version[index] += 1
    if new_version[index] > 9:
        new_version[index] = 0
        if index + 1 < 0:
            new_version[index + 1] += 1
        continue

    break

new_version = [str(new) for new in new_version]
print('.'.join(new_version))