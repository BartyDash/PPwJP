# Zadanie 3 
# Dana jest lista reprezentująca macierz:
# matrix = [
# [1, 2, 3, 4],
# [5, 6, 7, 8],
# [9, 10, 11, 12],
# ]
# Napisz program, który utworzy na jej podstawie listę reprezentującą macierz
# transponowaną:
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# Wykorzystaj zarówno listy składane, jak i zagnieżdżone pętle (napisz co najmniej dwa
# różne programy). Napisz funkcję, która wyświetla macierz jak tablicę (podobnie jak
# robimy to na matematyce) - argumentem wywołania powinna być lista reprezentująca
# macierz

def print_matrix(matrix):
    for row in matrix:
        print("\t".join(map(str, row)))

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = []
for i in range(len(matrix[0])):
    new_row = []
    for row in matrix:
        new_row.append(row[i])
    transposed.append(new_row)
print(transposed)

transposed2 = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print_matrix(transposed2)