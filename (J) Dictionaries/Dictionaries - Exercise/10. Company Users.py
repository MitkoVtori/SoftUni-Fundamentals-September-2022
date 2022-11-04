companies = {}
command = input()
while command != 'End':
    company, id = command.split(' -> ')

    if company not in companies:
        companies[company] = [id]

    elif company in companies and id not in companies[company]:
        companies[company].append(id)

    command = input()

for company, employee_ids in companies.items():
    print(company)
    print('--', '\n-- '.join(employee_ids))