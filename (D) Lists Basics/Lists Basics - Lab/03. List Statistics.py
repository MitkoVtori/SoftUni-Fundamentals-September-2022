lines = int(input())
list_positives = []
list_negatives = []

for number in range(lines):
    num = int(input())
    if num < 0:
        list_negatives.append(num)
    else:
        list_positives.append(num)

print(list_positives)
print(list_negatives)
print(f"Count of positives: {len(list_positives)}")
print(f"Sum of negatives: {sum(list_negatives)}")
