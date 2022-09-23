string = input().split()
number = int(input())

for shuffle in range(number):
    final_list = []
    middle_of_string = len(string) // 2
    left_part = string[0:middle_of_string]
    right_part = string[middle_of_string::]

    for index in range(len(left_part)):
        final_list.append(left_part[index])
        final_list.append(right_part[index])
    string = final_list

print(string)