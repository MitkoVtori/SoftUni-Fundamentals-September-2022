words = input().split(' ')
palindrome = input()
palindromes_list = []

for index in range(len(words)):
    if words[index] == words[index][::-1]:
        palindromes_list.append(words[index])

palindromes_count = palindromes_list.count(palindrome)

print(palindromes_list)
print(f"Found palindrome {palindromes_count} times")