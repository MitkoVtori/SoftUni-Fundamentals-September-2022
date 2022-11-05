contests_dictionary = {}
users_dictionary = {}


def contests():
    while True:
        command = input()

        if ':' not in command:
            break

        contest, password = command.split(':')

        contests_dictionary[contest] = password


def submissions():
    while True:
        command = input()

        if '=>' not in command:
            break

        contest, password, username, points = command.split('=>')
        points = int(points)

        if contest not in contests_dictionary.keys():
            continue

        if password != contests_dictionary[contest]:
            continue

        if username not in users_dictionary:
            users_dictionary[username] = {contest: points}

        elif contest not in users_dictionary[username]:
            users_dictionary[username][contest] = points

        elif contest in users_dictionary[username]:
            if points >= users_dictionary[username][contest]:
                users_dictionary[username][contest] = points


def best_score():
    list_values = {}
    for name, value in users_dictionary.items():
        list_values[name] = sum(value.values())
    best_candidate = max(list_values, key=list_values.get)
    total_score = max(list_values.values())
    print(f"Best candidate is {best_candidate} with total {total_score} points.")


def show_ranking_results():
    ordered_dictionary = dict(sorted(users_dictionary.items()))
    print('Ranking:')
    for username, contest in ordered_dictionary.items():
        print(username)
        values_dict = dict(sorted(contest.items(), key=lambda item: -item[1]))
        for key, value in values_dict.items():
            print('# ', key, '->', value)


contests()
submissions()
best_score()
show_ranking_results()