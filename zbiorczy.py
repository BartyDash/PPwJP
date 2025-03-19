# Github/lab1

## zad 2
    # Napisz funkcję, ktora zwróci listę krotek. Każda krotka to para liczb naturalnych dająca sumę 2*n.
    # Wartosc n jest parametrem funkcji. Np. lista dla n=50: [(0, 100), (1, 99), (2, 98), ..., (99, 1), (100, 0)]

def krotka(n):
    lista = []
    for i in range(n+1):
        lista.append((i, 2*n-i))
    return lista

print(krotka(50))

## zad 3
    # Stwórz słownik przechowujący w kluczu imię i nazwisko osoby, a w wartości datę jej urodzin.
    # Do słownika zapisz 3 różne osoby. Do przechowania daty użyj typu date z modułu datetime 
    # ([dokumentacja](https://docs.python.org/3/library/datetime.html#examples-of-usage-date)).
    # Następnie wypisz za pomoca pętli for wszystkie rekordy w słowniku w formacie 'Imie Nazwisko ur. dd-mm-rr'.

import datetime

birth = {
    'Tomek Kowalski': datetime.date(1995, 5, 17),
    'Sylwia Nowak': datetime.date(2000, 10, 25),
    'Ola Cośtam': datetime.date(2002, 1, 13)
}

for key, value in birth.items():
    print(f'{key} ur. {value.day}-{value.month}-{value.year}')

## zad 4
    # Przetestuj, które z omówionych powyżej typow danych można użyc w roli klucza w słowniku. 
    # Następnie porównaj swoje obserwacje z informacjami w [tym artykule](https://wiki.python.org/moin/DictionaryKeys).

test_dict = {}

test_dict[52] = 'test'
test_dict[52.0] = 'test'
test_dict['test'] = 'test'
test_dict[True] = 'test'
test_dict[complex(1, 2)] = 'test'
test_dict[(1, 2)] = 'test'
test_dict[None] = 'test'
test_dict[object()] = 'test'
test_dict[[1, 2]] = 'test'  #niet
test_dict[{1: 'test'}] = 'test'  #niet
test_dict[{1, 2, 3}] = 'test'   #niet

## zad 5
    # Przepisz poniższe pętle tak, by używały składania list (tworzyły tę samą listę w jednej linii).
    # values = []
    # for i in range(10):
    #     numbers.append(i**2)

    # values = []
    # for i in range(1, 6):
    #     for j in range(1, 4):
    #         values.append((i, j))

test = [i**2 for i in range(10)]
print(test)

two_loops = [(i, j) for i in range(1, 6) for j in range(1, 4)]
print(two_loops)


# Github/lab2

## zad 1
    # Wypisz wszystkie liczby od 1 do 50, jednak jeżeli liczba jest podzielna przez: trzy – zamiast liczby wypisz „Fizz”,
    # pięć – wypisz „Buzz”, jeśli jest podzielna zarówno przez trzy i pięć - wypisz „FizzBuzz”.

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# for i in range(1, 51):
#     if i % 3 == 0:
#         if i % 5 == 0:
#             print('FizzBuzz')
#         else:
#             print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

## zad 2
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

## zad 3
    # Napisz program, który pyta użytkownika o dzień tygodnia i zwraca odpowiednio napis dzień roboczy, weekend lub nieprawidlowa wartosc.

day = input("Podaj dzień tygodnia: ")

if day.lower() in ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek']:
    print("Dzień roboczy")
elif day.lower() in ['sobota', 'niedziela']:
    print("Weekend")
else:
    print("Nieprawidłowa wartość")


# Lista_1 moodle

## zad 18
    # Napisz program, który symuluje 1000 - krotny rzut sześcienną kostką,
    # a następnie podaje użytkownikowi ile razy wypadła dana ścianka kostki

import random

results = {i: 0 for i in range(1, 7)}

for _ in range(1000):   # _ jest to zmienna której nie używamy wgl
    results[random.randint(1, 6)] += 1  # losujemy klucz słownika

for key, value in results.items():
    print(f"{key}: {value}")

## zad 19
    # Napisz program, który wyświetla miesięczny kalendarz. Użytkownik powinien podać liczbę dni w miesiącu i dzień tygodnia, 
    # od którego zaczyna się miesiąc.
    # Przykładowe wykonanie programu:
    # Podaj liczbę dni w miesiącu: 31
    # Podaj początkowy dzień miesiąca (1-Nie, 7-Sob): 4
    #              1 2 3 4
    #  5  6  7  8  9 10 11
    # 12 13 14 15 16 17 18
    # 19 20 21 22 23 24 25
    # 26 27 28 29 30 31
    # Aby zakończyć program , naciśnij klawisz Enter.

def generate_calendar(days, start_day):
    calendar = [[]]
    calendar[0] = ["  " for _ in range(start_day - 1)]
    for day in range(1, days + 1):  # tego coś nie umiem w jedną linijkę zrobić
        if len(calendar[-1]) == 7:
            calendar.append([])
        calendar[-1].append(f"{day:2}")

    return calendar
    

def print_calendar(calendar):
    print("\nPn Wt Śr Cz Pt So Nd")
    for week in calendar:
        print(" ".join(week))
    print("\n")


days = int(input("Podaj liczbę dni w miesiącu: "))
start_day = int(input("Podaj początkowy dzień miesiąca (1-Nie, 7-Sob): "))

print_calendar(generate_calendar(days, start_day))

input("Aby zakończyć program, naciśnij klawisz Enter.")