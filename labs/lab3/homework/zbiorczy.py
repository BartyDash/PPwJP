# Lista_1 moodle

# Zadanie 7 
# Napisz program, który wyświetli następujący wzór:
# *
# **
# ***
# ****
# *****
# Wykorzystaj pętlę while i operator * w kontekście ciagów tekstowych (replikacja).
x = 0
while x < 5:
    x += 1
    print("*" * x)


# Zadanie 15. 
# Napisz program, który będzie wyświetlał następujący wzór:
#         *
#        ***
#       *****
#      *******
#     *********
#    ***********
#   *************
#  ***************
# *****************
# Wykorzystaj pętle zagnieżdżone for i nie używaj replikacji ciągów tekstowych. 
# Liczba wierszy powinna być określona przez użytkownika.

rows = int(input("Podaj liczbę wierszy: "))
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))


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


# Zadanie 21 
# Korzystając z pętli while i for (tj. na dwa sposoby) wykonaj nastepujące
# zadania:
# a) wypisz n kolejnych liczb naturalnych począwszy od 1 (dla n > 1 podanego przez
# użytkownika);
# d) wypisz n kolejnych liczb nieparzystych począwszy od n (dla n > 1 podanego
# przez użytkownika);
# e) wypisz n kolejnych wyrazów ciągu arytmetycznego: 1, 4, 7, 10, 13, . . . (dla n > 1
# podanego przez użytkownika);
# f) wypisz 12 kolejnych silni liczb naturalnych tj. 12 początkowych wyrazów ciągu:
# 1, 1 · 2 , 1 · 2 · 3, 1 · 2 · 3 · 4, . . . ;
# g) wypisz n kolejnych wyrazów ciągu: an = 1/n (dla n > 1 podanego przez użytkownika);
# h) wypisz 17 kolejnych wyrazów ciągu zdefiniowanego rekurencyjnie: a1 = 3, an = 6 · an-1 - 13/2 ;

n = int(input("Podaj liczbę n: "))
# a)
print("a)")
i = 1
while i <= n:
    print(i, end=" ")
    i += 1
print()
for i in range(1, n + 1):
    print(i, end=" ")

print("\n===========================================")

# d)
print("d)")
i = n
while i < n + n * 2:
    if i % 2 != 0:
        print(i, end=" ")
        i += 1
    else:
        i += 1
print()

for i in range(n, n + n * 2):
    if i % 2 != 0:
        print(i, end=" ")

print("\n===========================================")

# e)
print("e)")
i = 1
while i <= n:
    print(3 * i - 2, end=" ")
    i += 1
print()

for i in range(1, n + 1):
    print(3 * i - 2, end=" ")

print("\n===========================================")

# f)
print("f)")
i = 1
silnia = 1
while i <= 12:
    silnia *= i
    print(silnia, end=" ")
    i += 1
print()

silnia = 1
for i in range(1, 13):
    silnia *= i
    print(silnia, end=" ")

print("\n===========================================")

# g)
print("g)")
i = n
while i > 0:
    print(1 / i, end=" ")
    i -= 1
print()

for i in range(n, 0, -1):
    print(1 / i, end=" ")

print("\n===========================================")

# h)
print("h)")
array_a = [0] * 17
array_a[0] = 3
i = 1
while i < 17:
    array_a[i] = 6 * array_a[i - 1] - 13/2
    i += 1
print(array_a)

for i in range(1, 17):
    array_a[i] = 6 * array_a[i - 1] - 13/2
print(array_a)


# Zadanie 22
# Profesor Popularny dołączył do serwisu społecznościowego. Początkowo miał pięciu znajomych. 
# Zauważył, że liczba znajomych zmienia się zgodnie z następującą regułą: 
# pierwszego dnia odpadł jeden znajomy, a liczba pozostałych znajomych podwoiła się. 
# W drugim tygodniu odeszło dwóch znajomych, a pozostali znów podwoili swoją liczbę. 
# Ogólnie w n-tym tygodniu odpadło n przyjaciół, pozostali "mnożyli się" dwukrotnie. 
# Napisz program, który obliczy i wypisze liczbę znajomych profesora po kolejnych tygodniach. 
# Program powinien przeliczać kolejne tygodnie dopóty, dopóki liczba znajomych nie przekracza 
# tzw. liczby Dunbara. Liczba Dunbara to szacunkowa liczba maksymalnej liczności spójnej grupy społecznej, 
# w której każdy ze znajomych zna wszystkich innych znajomych i zna relacje pomiędzy pozostałymi znajomymi 
# (w przybliżeniu jest to 150 osób).

n = 1
friends_counter = 5

while friends_counter <= 150:
    print(friends_counter)
    friends_counter = (friends_counter - n) * 2

    n += 1