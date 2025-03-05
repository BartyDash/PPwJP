# Zadanie 10
# Zmodyfikuj program z zadania 2 tak aby użytkownik był proszony o podanie hasła aż do skutku.
# Wykorzystaj nieskończoną pętlę while przerywaną instrukcją break

print("Witaj w systemie logowania komputera!")

while True:
    password = input("Podaj hasło dostępu: ")
    if password == "programowanie":
        break
    else:
        print("Błędne hasło! Odmowa dostępu!")

print("Logowanie zakończyło się sukcesem!")
