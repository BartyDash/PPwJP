# Napisz funkcję, ktora zwróci listę krotek. Każda krotka to para liczb naturalnych dająca sumę 2*n.
# Wartosc n jest parametrem funkcji. Np. lista dla n=50: [(0, 100), (1, 99), (2, 98), ..., (99, 1), (100, 0)]

def krotka(n):
    lista = []
    for i in range(n+1):
        lista.append((i, 2*n-i))
    return lista

print(krotka(50))