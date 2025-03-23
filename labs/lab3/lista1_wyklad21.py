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