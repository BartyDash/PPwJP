# Zadanie 3
# Drużyna piłkarska szuka dziewczyn w wieku od 10 do 12 lat, aby grać w dru-
# żynie. Napisz program, który pyta o wiek użytkownika oraz o to czy jest to mężczyzna
# czy kobieta (używając "M" lub "K"). Program powinien wyświetlać komunikat
# wskazujący, czy dana osoba może grać w zespole. Program powinien pytać o wiek tylko
# w przypadku gdy użytkownik jest dziewczyną

print("Drużyna piłkarska szuka zawodniczek w wieku od 10 do 12 lat.")
plec = input("Podaj swoją płeć (M/K): ")
if plec == "K":
    wiek = int(input("Podaj swój wiek: "))
    if 10 <= wiek <= 12:
        print("Możesz grać w zespole!")
    else:
        print("Niestety, nie spełniasz wymagań wiekowych.")
elif plec == "M":
    print("Drużyna poszukuje tylko dziewczyn.")
else:
    print("Niepoprawna płeć.")