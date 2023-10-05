MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def morse_encrypt(txt):
    morse_text = ""
    for char in text:
        if char != " ":
            coded = MORSE_CODE_DICT[char]
            morse_text += coded + " "
        else:
            morse_text += " "
    return f"Text in morse code is:  {morse_text}"


def morse_decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher


go_on = True
while go_on:
    mode = input("Mode (Decode | Encode | End): ").upper()

    if mode == "END":
        go_on = False
    elif mode == "ENCODE":
        text = input(f"Enter the text you want to {mode} in morse code: ")
        print(morse_encrypt(text))

    elif mode == "DECODE":
        text = input(f"Enter the text you want to {mode} in morse code: ")
        print(morse_decrypt(text))
