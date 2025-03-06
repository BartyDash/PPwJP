# Napisz program, który pyta użytkownika o dzień tygodnia i zwraca odpowiednio napis dzień roboczy, weekend lub nieprawidlowa wartosc.

day = input("Podaj dzień tygodnia: ")

if day.lower() in ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek']:
    print("Dzień roboczy")
elif day.lower() in ['sobota', 'niedziela']:
    print("Weekend")
else:
    print("Nieprawidłowa wartość")

# zrobić z match - case