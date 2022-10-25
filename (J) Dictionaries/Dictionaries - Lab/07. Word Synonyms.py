word_synonyms = {}
words = int(input())

for synonyms in range(words):
    word = input()
    synonym = input()
    if word not in word_synonyms:
        word_synonyms[word] = []
        word_synonyms[word].append(synonym)
    else:
        word_synonyms[word].append(synonym)

for word, synonym in word_synonyms.items():
    print(f"{word} - ", end="")
    print(*synonym, sep=", ")