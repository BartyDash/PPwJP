# Poczytaj o [listach składanych](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions). 
# Przepisz poniższe pętle tak, by używały składania list (tworzyły tę samą listę w jednej linii).
# values = []
# for i in range(10):
#     numbers.append(i**2)

# values = []
# for i in range(1, 6):
#     for j in range(1, 4):
#         values.append((i, j))

test = [i**2 for i in range(10)]
print(test)

two_loops = [(i, j) for i in range(1, 6) for j in range(1, 4)]
print(two_loops)