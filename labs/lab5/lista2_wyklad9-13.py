# Zadanie 9 
# Napisz program, który poprosi użytkownika o podanie dowolnego ciągu
# tekstowego, a następnie wypisze ten ciąg w odwrotnej kolejności.
print("------------------")

text = input("Podaj ciąg tekstowy: ")
print("Odwrotny ciąg:", text[::-1])

# Zadanie 10 
# Napisz funkcję is_palindrome(), która zwraca wartość true lub false
# w zależności od tego czy argument funkcji (ciąg tekstowy) jest palindromem1 czy nie.
print("------------------")

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]    #odwracamy sb

word = input("Podaj wyraz: ")
if is_palindrome(word):
    print("To jest palindrom.")
else:
    print("To nie jest palindrom.")

# Zadanie 11 
# Napisz program, który poprosi użytkownika o podanie ciągu tekstowego,
# a następnie wyświetli ten ciąg bez samogłosek. Wykorzystaj pętle for.
print("------------------")

text = input("Podaj ciąg tekstowy: ")
no_vowels = ""
vowels = "aeiouyąęóAEIOUYĄĘÓ"

for char in text:
    if char not in vowels:
        no_vowels += char

print("Bez samogłosek:", no_vowels)

# Zadanie 12 
# Napisz program, który zliczy ile razy dana litera pojawia się w podanym
# przez użytkownika ciągu tekstowym. Program powinien wypisać informacje o liczbie wystąpień każdej litery alfabetu. Program można napisać wykorzystując listy lub,
# jeszcze prościej, wykorzystując słowniki. Tu wykorzystaj metody ciągów tekstowych,
# a wyników nigdzie nie musisz zapamiętywać - wystarczy je wyświetlić.
print("------------------")

text = input("Podaj tekst: ").lower()
counts = {}

for char in text:
    if char.isalpha():
        counts[char] = counts.get(char, 0) + 1

for letter in sorted(counts):
    print(f"{letter}: {counts[letter]}")

# Zadanie 13 
# Napisz program, w którym zdefiniowane będą dwie krotki zawierające
# symbole pierwiastków chemicznych. Pierwsza krotka powinna zawierać symbole metali alkalicznych: Li, Na, K, a druga - symbole fluorowców: F, Cl, Br.
# Program powinien generować i wypisywać wzory związków chemicznych powsta-
# łych z połączenia każdego pierwiastka z pierwszej krotki z każdym pierwiastkiem z
# drugiej krotki (np. LiF, LiCl, itp.).
# Do realizacji zadania użyj dwóch zagnieżdżonych pętli for.
# Powstałe związki chemiczne są poprawne i należą do grupy halogenków, takich jak
# fluorki, chlorki i bromki
print("------------------")

metale_alkaliczne = ("Li", "Na", "K")
fluorowce = ("F", "Cl", "Br")

print("Związki chemiczne (halogenki):")
for metal in metale_alkaliczne:
    for halogen in fluorowce:
        print(metal + halogen)