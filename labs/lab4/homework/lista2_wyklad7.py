# Zadanie 7 
# Napisz funkcję o nazwie collatz, która pobiera tylko jeden argument o nazwie number. 
# Jeżeli argument funkcji jest parzysty, funkcja powinna wyświetlić i zwrócić wartość number // 2. 
# Jeżeli argument funkcji będzie nieparzysty wtedy funkcja
# collatz powinna wyświetlić i zwrócić wartość 3 * number + 1. Napisz program,
# w którym użytkownik podaje pewną liczbę całkowitą n, a program oblicza wartość
# funkcji collatz(n) oraz wartości tej funkcji z kolejnych wartości zwracanych przez
# uprzednie wywołania funkcji collatz, aż do momentu, gdy wartością zwróconą
# będzie liczba 1.


def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)

    return result


n = int(input("Podaj liczbę całkowitą n: "))
while n != 1:
    n = collatz(n)