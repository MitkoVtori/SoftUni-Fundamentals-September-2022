def translator(dictionary, string):
    message = ''
    for letter in string:
        for ltr in letter.split(" "):
            if ltr != '':
                message += dictionary[ltr]
        message += " "

    return message


morse_code = {'..-.': 'F', '-..-': 'X',
              '.--.': 'P', '-': 'T', '..---': '2',
              '....-': '4', '-----': '0', '--...': '7',
              '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
              '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
              '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
              '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
              '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
              '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}

words = input().split(" | ")
print(translator(morse_code, words))