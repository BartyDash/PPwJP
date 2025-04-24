# Zadanie 2 
# Dana jest lista
# vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Utwórz listę, w której wszystkie elementy list zagnieżdżonych w vec występują na
# pierwszym poziomie, tj. [1, 2, 3, 4, 5, 6, 7, 8, 9]. Przedstaw dwa rozwiązania:
# z zagnieżdżonymi pętlami for oraz z wykorzystaniem listy składanej.

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# forem
list = []
for sublist in vec:
    for item in sublist:
        list.append(item)
print(list)

#lista składana
list = [item for sublist in vec for item in sublist]
print(list)