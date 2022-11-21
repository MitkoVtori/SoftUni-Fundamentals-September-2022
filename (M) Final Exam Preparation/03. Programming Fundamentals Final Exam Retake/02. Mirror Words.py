import re

pattern = r"([@#])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"
string = input()
pairs = re.findall(pattern, string)

if not len(pairs):
    print("No word pairs found!")
else:
    print(f"{len(pairs)} word pairs found!")

mirror_words = {}

for words in pairs:
    if words[1] == words[2][::-1]:
       word = words[1]
       mirror_word = words[2]
       mirror_words[word] = mirror_word

if len(mirror_words):
    print("The mirror words are:")

    words_list = [] # I need this list, to store the output strings in it, so I can print all mirror matches with join()

    for word, mirror in mirror_words.items():
        words_list.append(f"{word} <=> {mirror}") # I append the string in list instead of printing it with end=", " because the end() command will paste a comma "," at the end of the sentence
        # for example, if we use:
        # print(f"{word} <=> {miror}", end=", ") 
        # The output will be: word <=> drow, was <=> saw, test <=> tset, 
     # You can see that, there's a comma at the end that we don't want ^
        
    print(', '.join(words_list))

else:
    print("No mirror words!")