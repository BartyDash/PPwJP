# Zadanie 4
# Napisz funkcję, która dla podanego jej jako argument ciągu tekstowego zliczy liczbę wystąpień poszczególnych liter w tym ciągu 
# (inne znaki nie powinny być zliczane). Małe i duże litery powinny być traktowane jako te same litery.
# Wykorzystaj słownik, by przechowywać informację o liczbie wystąpień danych liter w podanym tekście.
# Następnie wykorzystaj typ Counter z modułu collections, aby wykonać to zadanie jeszcze prościej.
# Wyświetl informację o liczbie wystąpień danej litery zgodnie z porządkiem alfabetycznym.

def count_letters(text):
    text = text.lower()
    letter_count = {}
    for char in text:
        if char.isalpha():  # czy jest literą
            letter_count[char] = letter_count.get(char, 0) + 1
            # if char in letter_count:
            #     letter_count[char] += 1
            # else:
            #     letter_count[char] = 1
    for letter in sorted(letter_count):
        print(f"{letter}: {letter_count[letter]}")

count_letters("Testowy tekst na szybko! napisany.")
print("---------------------")

from collections import Counter

def count_letters_counter(text):
    letter_count = Counter(char.lower() for char in text if char.isalpha())
    for letter in sorted(letter_count):
        print(f"{letter}: {letter_count[letter]}")

count_letters_counter("Ala ma kota.")