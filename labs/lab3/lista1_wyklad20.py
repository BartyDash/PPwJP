# Zadanie 20. 
# Napisz program, który oblicza sumę 1, 2, 3, 4 itd. (aż do pewnej granicy) wyrazów następujących ciągów:
# +1.0/2.0 + 1.0/3.0 + 1.0/4.0 + ...
# -1.0/2.0 + 1.0/3.0 - 1.0/4.0 + ...
# Maksymalna liczba wyrazów sumowania powinna być określana przez użytkownika. 
# Przyjrzyj się sumom dla 10, 100 i 1000 wyrazów. Czy coś zauważyłeś?
# Wskazówka: -1 pomnożone przez siebie nieparzystą ilość razy jest równe -1, natomiast parzystą ilość razy +1.

def my_sum(n):
    result = 0

    for i in range(1, n + 1):
        result += (-1) ** (i + 1) * 1 / (i + 1)

    return result


n = int(input("Podaj liczbę wyrazów: "))
print(my_sum(n))