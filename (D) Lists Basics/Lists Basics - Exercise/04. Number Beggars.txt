string = input().split(", ")
beggars = int(input())
final_list = []
counter = 0

my_list = []
for curr_index in string:
    my_list.append(int(curr_index))

while counter < beggars:
    beggars_sum = 0

    for curr_index in range(counter, len(string), beggars):
        beggars_sum += my_list[curr_index]
    counter += 1
    final_list.append(beggars_sum)

print(final_list)