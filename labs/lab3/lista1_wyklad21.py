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
# g) wypisz n kolejnych wyrazów ciągu: an = n1 (dla n > 1 podanego przez użytkownika);

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
while i < n * 2 - 1:
    if i % 2 != 0:
        print(i, end=" ")
        i += 1
    i += 1

print("\n===========================================")