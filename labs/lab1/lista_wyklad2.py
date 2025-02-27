# Zadanie 2
# Napisz prosty program symulujący procedurę logowania do komputera.
# Wykorzystaj konstrukcję rozgałęziającą if ... else. Oto przykładowe sesje z programem:
# Witaj w systemie logowania komputera!
# Podaj hasło dostępu: programowanie
# Logowanie zakończyło się sukcesem!
# ———————————————————————————
# Witaj w systemie logowania komputera!
# Podaj hasło dostępu: hasło
# Błędne hasło! Odmowa dostępu!

print("Witaj w systemie logowania komputera!")
haslo = input("Podaj hasło dostępu: ")
if haslo == "programowanie":
    print("Logowanie zakończyło się sukcesem!")
else:
    print("Błędne hasło! Odmowa dostępu!")