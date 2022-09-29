bar_percentage = input()
loading_bar = []

for percent in range(int(bar_percentage[0])):
    if int(bar_percentage) >= 10:
        loading_bar.append('%')

for dots in range(10 - int(bar_percentage[0])):
    if int(bar_percentage) >= 10:
        loading_bar.append('.')

if int(bar_percentage) < 10:
    loading_bar.append('.' * 10)

loading_bar = ''.join(loading_bar)

if bar_percentage == '100':
    print("100% Complete!")
    print(f"[{'%' * 10}]")
else:
    print(f"{bar_percentage}% [{loading_bar}]")
    print("Still loading...")