# Stwórz prostą grę polegającą na zgadywaniu losowej liczby z zakresu 1-100 wygenerowanej przez komputer.
# Uzyj modułu random. Użytkownik wprowadza liczbę, a program nakierowuje gracza przez podpowiedzi,
# np. "Podałeś za małą/za dużą liczbę" lub w przypadku trafienia informuje o wygranej.
# Możesz opcjonalnie dodać warunek maksymalnie n prób.
# Pytanie "przy okazji": jaka jest najlepsza strategia na wygraną?

import random

random_number = random.randint(1, 100)

while True:
    try:
        number = int(input("Zgadnij liczbe (1-100): "))
        if number > random_number:
            print("Podałeś za dużą liczbę")
        elif number < random_number:
            print("Podałeś za małą liczbę")
        else:
            print("Zgadłeś!")
            break
    except ValueError:
        print("Błędna wartość!")

# jak działa match - case ? - bo `number < random_number` nie działa sprawdzanie warunków logicznych
