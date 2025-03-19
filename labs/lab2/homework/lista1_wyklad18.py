# Zadanie 18
# Napisz program, który symuluje 1000 - krotny rzut sześcienną kostką,
# a następnie podaje użytkownikowi ile razy wypadła dana ścianka kostki

import random

results = {i: 0 for i in range(1, 7)}

for _ in range(1000):   # _ jest to zmienna której nie używamy wgl
    results[random.randint(1, 6)] += 1  # losujemy klucz słownika

for key, value in results.items():
    print(f"{key}: {value}")