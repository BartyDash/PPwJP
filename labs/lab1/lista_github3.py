# Stwórz słownik przechowujący w kluczu imię i nazwisko osoby, a w wartości datę jej urodzin.
# Do słownika zapisz 3 różne osoby. Do przechowania daty użyj typu date z modułu datetime 
# ([dokumentacja](https://docs.python.org/3/library/datetime.html#examples-of-usage-date)).
# Następnie wypisz za pomoca pętli for wszystkie rekordy w słowniku w formacie 'Imie Nazwisko ur. dd-mm-rr'.

import datetime

birth = {
    'Tomek Kowalski': datetime.date(1995, 5, 17),
    'Sylwia Nowak': datetime.date(2000, 10, 25),
    'Ola Cośtam': datetime.date(2002, 1, 13)
}

for key, value in birth.items():
    print(f'{key} ur. {value.day}-{value.month}-{value.year}')