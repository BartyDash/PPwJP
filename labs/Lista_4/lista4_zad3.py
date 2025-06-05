import sys

morse_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',   'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',  'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',  'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..'
}

text_dict = {
    '.-': 'A',    '-...': 'B',  '-.-.': 'C', '-..': 'D',   '.': 'E',     '..-.': 'F',
    '--.': 'G',   '....': 'H',  '..': 'I',   '.---': 'J',  '-.-': 'K',   '.-..': 'L',
    '--': 'M',    '-.': 'N',    '---': 'O',  '.--.': 'P',  '--.-': 'Q',  '.-.': 'R',
    '...': 'S',   '-': 'T',     '..-': 'U',  '...-': 'V',  '.--': 'W',   '-..-': 'X',
    '-.--': 'Y',  '--..': 'Z'
}


def text_to_morse(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                line = line.strip().upper()
                if not line:
                    outfile.write("\n")
                    continue
                words = line.split()
                for word in words:
                    morse_word = [morse_dict[char] for char in word if char in morse_dict]
                    outfile.write('\n'.join(morse_word) + '\n\n')
                outfile.write('\n')
        print(f"Zakończono tłumaczenie do pliku {output_file}")
    except FileNotFoundError:
        print("Nie znaleziono pliku wejściowego.")


def morse_to_text(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            word = []
            sentence = []
            empty_lines = 0
            for line in infile:
                code = line.strip()
                if not code:
                    empty_lines += 1
                    if empty_lines == 2:
                        if word:
                            sentence.append(''.join(word))
                            word = []
                        if sentence:
                            outfile.write(' '.join(sentence) + ".\n")
                            sentence = []
                        empty_lines = 0
                    elif empty_lines == 1:
                        if word:
                            sentence.append(''.join(word))
                            word = []
                else:
                    empty_lines = 0
                    letter = text_dict.get(code)
                    if letter:
                        word.append(letter)
            if word:
                sentence.append(''.join(word))
            if sentence:
                outfile.write(' '.join(sentence) + "\n")
        print(f"Zakończono tłumaczenie do pliku {output_file}")
    except FileNotFoundError:
        print("Nie znaleziono pliku wejściowego.")


def main():
    # print("Wybierz rodzaj tłumaczenia:")
    # print("1 - Tekst na kod Morse'a")
    # print("2 - Kod Morse'a na tekst")
    # choice = input("Wybór (1/2): ")

    # input_file = input("Podaj nazwę pliku wejściowego: ")
    # output_file = input("Podaj nazwę pliku wynikowego: ")
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    choice = sys.argv[3] 
    if int(sys.argv[3]) > 2:
        choice = '2'
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[3])
    print(len(sys.argv[3]))
    print(choice)

    if choice == '1':
        text_to_morse(input_file, output_file)
    elif choice == '2':
        morse_to_text(input_file, output_file)
    else:
        print("Nieprawidłowy wybór.")


if __name__ == "__main__":
    main()