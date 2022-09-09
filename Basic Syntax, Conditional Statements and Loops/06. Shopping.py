curr_money = 0
budget = int(input())
money_spend = input()

while money_spend != "End":
    curr_money += int(money_spend)

    if curr_money > budget:
        print("You went in overdraft!")
        break
    money_spend = input()
else:
    print("You bought everything needed.")
