employee = list(map(int, input().split(' ')))
factor = int(input())
employee = [factor * employee[index] for index in range(len(employee))]
happy_office = list(filter(lambda x: x >= sum(employee) / len(employee), employee))

if len(happy_office) >= len(employee) / 2:
    print(f"Score: {len(happy_office)}/{len(employee)}. Employees are happy!")
else:
    print(f"Score: {len(happy_office)}/{len(employee)}. Employees are not happy!")