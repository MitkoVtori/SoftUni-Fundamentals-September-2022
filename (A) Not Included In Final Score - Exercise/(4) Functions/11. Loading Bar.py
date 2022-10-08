def loading_bar(percent):
    if percent == 100:
        return f"100% Complete!\n[{'%' * 10}]"
    return f"{percent}% [{'%' * (percent // 10)}{'.' * (10 - percent // 10)}]\nStill loading..."


loading_percent = int(input())
print(loading_bar(loading_percent))
