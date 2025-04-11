# Zadanie 14
# Napisz grę „Przestawione litery”. Gra polega na tym, że komputer wybiera
# losowo słowo z określonej grupy słów, a następnie przestawia jego litery w losowej
# kolejności, tworząc anagram.
# Zadaniem gracza jest odgadnięcie oryginalnego słowa na podstawie pomieszanego
# ciągu liter.
# Program powinien składać się z następujących funkcji:
# • choose_word(word_list) - wybiera losowe słowo z podanej listy;
# • shuffle_letters(word) - generuje anagram poprzez losowe przemieszanie liter;
# • play_game() - przeprowadza rozgrywkę, wyświetlając anagram i pobierając odpowiedź od gracza.

import random

def choose_word(word_list):
    return random.choice(word_list)

def shuffle_letters(word):
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

def play_game():
    words = ["komputer", "drukarka", "python", "program", "grafika"]
    word = choose_word(words)
    anagram = shuffle_letters(word)
    print("Odgadnij słowo:", anagram)
    guess = input("Twoja odpowiedź: ").strip().lower()
    if guess == word:
        print("Brawo, odgadłeś!")
    else:
        print(f"Niestety, poprawne słowo to: {word}")

if __name__ == "__main__":
    play_game()