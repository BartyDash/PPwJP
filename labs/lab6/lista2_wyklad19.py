# Zadanie 19 
# Napisz program do przechowywania pięciu najlepszych wyników gracza.
# Program powinien wyświetlać menu umożliwiające wykonywanie operacji na liście
# wyników, takich jak:
# • dodawanie nowego wyniku;
# • usuwanie wyniku;
# • sortowanie wyników;
# • wyświetlanie listy wyników;
# • zakończenie pracy z programem.
# Na początku lista wyników powinna być pusta. W trakcie działania programu może
# przechowywać maksymalnie 5 najlepszych wyników. Jeśli zostanie dodany 6. wynik,
# to lista powinna automatycznie usunąć najniższy wynik, tak aby nadal zawierała tylko
# najlepsze osiągnięcia

def wyswietl_menu():
    print("\n===== MENU WYNIKÓW GRACZA =====")
    print("1. Dodaj nowy wynik")
    print("2. Usuń wynik")
    print("3. Sortuj wyniki")
    print("4. Wyświetl listę wyników")
    print("5. Zakończ program")
    print("===============================")

def dodaj_wynik(wyniki):
    try:
        nowy_wynik = int(input("Podaj nowy wynik: "))
        wyniki.append(nowy_wynik)
        wyniki.sort(reverse=True)
        if len(wyniki) > 5:
            usuniety = wyniki.pop()
            print(f"Usunięto najgorszy wynik: {usuniety}")
        print("Wynik został dodany.")
    except ValueError:
        print("Błąd: Proszę wprowadzić liczbę całkowitą.")

def usun_wynik(wyniki):
    if not wyniki:
        print("Lista wyników jest pusta.")
        return
    
    print("Aktualna lista wyników:")
    for i, wynik in enumerate(wyniki):
        print(f"{i+1}. {wynik}")
    
    try:
        indeks = int(input("Podaj numer wyniku do usunięcia (1-" + str(len(wyniki)) + "): ")) - 1
        if 0 <= indeks < len(wyniki):
            usuniety = wyniki.pop(indeks)
            print(f"Usunięto wynik: {usuniety}")
        else:
            print("Błąd: Nieprawidłowy numer wyniku.")
    except ValueError:
        print("Błąd: Proszę wprowadzić liczbę całkowitą.")

def sortuj_wyniki(wyniki):
    if not wyniki:
        print("Lista wyników jest pusta.")
        return
    
    print("Wybierz sposób sortowania:")
    print("1. Rosnąco")
    print("2. Malejąco")
    
    try:
        wybor = int(input("Twój wybór (1-2): "))
        if wybor == 1:
            wyniki.sort()
            print("Wyniki posortowane rosnąco.")
        elif wybor == 2:
            wyniki.sort(reverse=True)
            print("Wyniki posortowane malejąco.")
        else:
            print("Błąd: Nieprawidłowy wybór.")
    except ValueError:
        print("Błąd: Proszę wprowadzić liczbę całkowitą.")

def wyswietl_wyniki(wyniki):
    if not wyniki:
        print("Lista wyników jest pusta.")
        return
    
    print("\n===== LISTA WYNIKÓW =====")
    for i, wynik in enumerate(wyniki):  #można for i in range(len(wyniki)) - ale jest brzydsze
        print(f"{i+1}. {wynik}")
    print("========================")

def main():
    wyniki = []
    
    while True:
        wyswietl_menu()
        try:
            wybor = int(input("Wybierz opcję (1-5): "))
            
            if wybor == 1:
                dodaj_wynik(wyniki)
            elif wybor == 2:
                usun_wynik(wyniki)
            elif wybor == 3:
                sortuj_wyniki(wyniki)
            elif wybor == 4:
                wyswietl_wyniki(wyniki)
            elif wybor == 5:
                print("Koniec programu. Do widzenia!")
                break
            else:
                print("Błąd: Nieprawidłowy wybór. Wybierz opcję od 1 do 5.")
        except ValueError:
            print("Błąd: Proszę wprowadzić liczbę całkowitą.")

if __name__ == "__main__":
    print("Program do przechowywania pięciu najlepszych wyników gracza.")
    main()