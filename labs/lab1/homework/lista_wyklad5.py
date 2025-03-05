# Zadanie 5
# Za pomocą instrukcji if...elif...else zamień ocenę wyrażoną w punktach na ocenę w stopniach.
# Przyjmij następująca skalę ocen: A = 90 - 100 punktów,
# B = 80 - 89 punktów, C = 70 - 79 punktów, D = 60 - 69 punktów, E = 0 - 59 punktów.
# Jeżeli liczba punktów jest większa niż 100 lub mniejsza od zera, program powinien
# wypisać komunikat o błędzie.

points = int(input("Podaj ocenę w punktach: "))

if 90 <= points <= 100:
    print("Ocena: A")
elif 80 <= points <= 89:
    print("Ocena: B")
elif 70 <= points <= 79:
    print("Ocena: C")
elif 60 <= points <= 69:
    print("Ocena: D")
elif 0 <= points <= 59:
    print("Ocena: E")
else:
    print("Error: niepoprawna liczba punktów.")