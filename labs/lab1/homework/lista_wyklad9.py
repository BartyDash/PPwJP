# Zadanie 9
# Napisz program który prosi o podanie liczby całkowitej n (n > 0) i oblicza
# sumę kwadratów pierwszych n liczb całkowitych. Wykorzystaj dwukrotnie pętle while
# - po raz pierwszy aby „wymusić” na użytkowniku podanie liczby dodatniej, po raz
# drugi aby wyznaczyć szukaną sumę.

while True:
    try:
        n = int(input("Podaj liczbę całkowitą n: "))
        if n > 0:
            break
        else:
            print("Liczba musi być większa od 0.")
    except ValueError:  # tak jak catch w JS
        print("To nie jest liczba całkowita!")
        
sum_sqr = 0
i = 1

while i <= n:
    sum_sqr += i ** 2   # pow() też da radę
    i += 1  # i++ nie działa... :(

print(f"Suma kwadratów pierwszych {n} liczb całkowitych wynosi: {sum_sqr}")