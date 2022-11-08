import re
total_income = 0
pattern = re.compile(
    r"(%)(?P<customer>[A-Z][a-z]+)\1([^\|\$\%\.]*)"
    r"<(?P<product>[\w]+)>([^\|\$\%\.]*)"
    r"\|(?P<count>[\d]+)\|([^\|\$\%\.]*)"
    r"(?P<price>[1-9]+[.0-9]*)\$")


data_input = input()

while data_input != "end of shift":
    result = re.finditer(pattern, data_input)
    for show in result:
        current_price = float(show["count"]) * float(show["price"])
        print(f"{show['customer']}: {show['product']} - {current_price:.2f}")
        total_income += current_price
    data_input = input()

print(f"Total income: {total_income:.2f}")