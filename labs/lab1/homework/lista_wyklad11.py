# Zadanie 11
# Napisz program, który pobiera dwie liczby n (n > 2) i k (k < n). Program
# powinien wyświetlić wszystkie liczby od 1 do n z pominięciem liczb podzielnych przez
# k. Wykorzystaj instrukcję continue

n = int(input("Podaj liczbę n (n > 2): "))
k = int(input("Podaj liczbę k (k < n): "))

if n <= 2 or k >= n:
    print("Podano niepoprawne liczby!")
else:
    for i in range(1, n+1):
        if i%k == 0:
            continue
        print(i)