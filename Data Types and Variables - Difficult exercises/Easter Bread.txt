budget = float(input())
flour_1kg = float(input())
one_pack_eggs = flour_1kg * 0.75
milk = ((flour_1kg * 0.25) + flour_1kg) * 0.25
total = flour_1kg + one_pack_eggs + milk
curr_bread_cnt = 0
colored_eggs = 0

while budget >= total:
    curr_bread_cnt += 1
    budget -= total
    colored_eggs += 3
    if curr_bread_cnt % 3 == 0:
        colored_eggs -= (curr_bread_cnt - 2)

print(f"You made {curr_bread_cnt} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")