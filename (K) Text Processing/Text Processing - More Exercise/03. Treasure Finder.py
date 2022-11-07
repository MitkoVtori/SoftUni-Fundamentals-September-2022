secret_key = [int(x) for x in input().split()]
secret_msg = input()

how_long = len(secret_key)
while secret_msg != "find":
    secret_text = "".join([chr(ord(secret_msg[i]) - secret_key[i % how_long]) for i in range(len(secret_msg))])
    item = secret_text.split("&")[-2]
    location = secret_text.split("<")[-1][:-1]
    print(f"Found {item} at {location}")
    secret_msg = input()