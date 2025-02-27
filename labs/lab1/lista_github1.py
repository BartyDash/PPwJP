# Stwórz listę zawierającą liczby całkowite od 1 do 10 000, używajac range [(dokumentacja)](https://docs.python.org/3/library/stdtypes.html#range).
# Następnie użyj pętli, aby każdą liczbę w liście zwiększyć o 1.
# Użyj modułu timeit by sprawdzić, ile czasu zajmie wykonanie tej pętli.

import timeit

# for i in range(len(lista)):
#     lista[i] += 1

lista = list(range(1, 10001))
print(timeit.timeit('''
for i in range(len(lista)):
    lista[i] += 1
''', number=1, globals=globals()))
print(lista[1])