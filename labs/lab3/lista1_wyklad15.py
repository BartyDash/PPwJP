# Zadanie 15. 
# Napisz program, który będzie wyświetlał następujący wzór:
#         *
#        ***
#       *****
#      *******
#     *********
#    ***********
#   *************
#  ***************
# *****************
# Wykorzystaj pętle zagnieżdżone for i nie używaj replikacji ciągów tekstowych. 
# Liczba wierszy powinna być określona przez użytkownika.

rows = int(input("Podaj liczbę wierszy: "))
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))