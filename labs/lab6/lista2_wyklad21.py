# Zadanie 21 Napisz grę „Wisielec”. Komputer losowo wybiera ukryte słowo, a zadaniem
# gracza jest stopniowe odgadnięcie go, podając litery jedna po drugiej.
# Zasady gry:
# • Gracz wprowadza pojedyncze litery.
# • Jeśli podana litera znajduje się w słowie, jest ujawniana na odpowiednich pozycjach.
# • Jeśli litera nie występuje w słowie, komputer wyświetla kolejne etapy rysunku
# wisielca.
# • Gracz wygrywa, jeśli odgadnie całe słowo przed ukończeniem rysunku wisielca.
# • Jeśli rysunek zostanie ukończony, gracz przegrywa.

import random

def play():
    print("===== Gra w Wisielca =====")
    print("Odgadnij słowo, podając litery.")
    print("Masz 7 prób.")

def load_words():
    return ["python", "Ananas", "programowanie", "algorytm", "zmienna", 
            "funkcja", "nieznany", "zeszyt", "internet", "aplikacja", 
            "podkładka", "metoda", "dziedziczenie", "rekurencja"]

def choose_word(words):
    return random.choice(words).lower()