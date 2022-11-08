import re

number_of_messages = int(input())

planets_info = {"Attacked": [], "Destroyed": [], "A": "Attacked", "D": "Destroyed"}
pattern = re.compile(r"@(?P<planet_name>[A-Za-z]+)([^\@\-\!\:\>]*)"
                     r":(?P<population>[0-9]+)([^\@\-\!\:\>]*)"
                     r"(\!)(?P<attack_type>[AD])\5([^\@\-\!\:\>]*)"
                     r"->(?P<soldier>[0-9]+)")

for msg in range(number_of_messages):
    current_msg = input()
    code_decrypt = sum(current_msg.lower().count(char) for char in "star")
    decode_msg = "".join(chr(ord(char) - code_decrypt) for char in current_msg)
    result = re.finditer(pattern, decode_msg)
    for show in result:
        planets_info[planets_info[show["attack_type"]]].append(show["planet_name"])

for type_attack in list(planets_info.keys())[:2]:
    planet_count = len(planets_info[type_attack])
    print(f"{type_attack} planets: {planet_count}")
    if planet_count:
        for planet in sorted(planets_info[type_attack]):
            print(f"-> {planet}")