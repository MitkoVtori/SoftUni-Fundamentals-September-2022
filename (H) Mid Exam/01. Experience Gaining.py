experience_needed = float(input())
battles = int(input())
total_experience = 0
battles_count = 0
is_enough = False

for battle in range(1, battles + 1):
    experience = float(input())
    battles_count += 1

    if battle % 3 == 0:
        experience += experience * 0.15

    if battle % 5 == 0:
        experience *= 0.90

    if battle % 15 == 0:
        experience += experience * 0.05

    total_experience += experience

    if total_experience >= experience_needed:
        is_enough = True
        break

if is_enough:
    print(f"Player successfully collected his needed experience for {battles_count} battles.")
else:
    needed_experience = experience_needed - total_experience
    print(f"Player was not able to collect the needed experience, {needed_experience:.2f} more needed.")
