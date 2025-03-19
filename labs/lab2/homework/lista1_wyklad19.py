# Zadanie 19 
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