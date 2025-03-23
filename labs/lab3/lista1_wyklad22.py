# Zadanie 22
# Profesor Popularny dołączył do serwisu społecznościowego. Początkowo miał pięciu znajomych. 
# Zauważył, że liczba znajomych zmienia się zgodnie z następującą regułą: 
# pierwszego dnia odpadł jeden znajomy, a liczba pozostałych znajomych podwoiła się. 
# W drugim tygodniu odeszło dwóch znajomych, a pozostali znów podwoili swoją liczbę. 
# Ogólnie w n-tym tygodniu odpadło n przyjaciół, pozostali "mnożyli się" dwukrotnie. 
# Napisz program, który obliczy i wypisze liczbę znajomych profesora po kolejnych tygodniach. 
# Program powinien przeliczać kolejne tygodnie dopóty, dopóki liczba znajomych nie przekracza 
# tzw. liczby Dunbara. Liczba Dunbara to szacunkowa liczba maksymalnej liczności spójnej grupy społecznej, 
# w której każdy ze znajomych zna wszystkich innych znajomych i zna relacje pomiędzy pozostałymi znajomymi 
# (w przybliżeniu jest to 150 osób).

n = 1
friends_counter = 5

while friends_counter <= 150:
    print(friends_counter)
    friends_counter = (friends_counter - n) * 2

    n += 1