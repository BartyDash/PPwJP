L = list(range(1, 21))
text = "Ta kobieta była jak moneta , szła z ręki do ręki, ale nie straciła na wartości."

div_3_or_5 = {x for x in L if x % 3 == 0 or x % 5 == 0}

words = text.lower().replace(',', '').replace('.', '').split()
word_lengths = {len(word) for word in words}

common_set = div_3_or_5 & word_lengths

if 42 not in common_set:
    common_set.add(42)

reference_set = {1, 2, 3, 5, 10, 15, 20, 42}
is_subset = common_set.issubset(reference_set)

print("Zbiór liczb podzielnych przez 3 lub 5:", div_3_or_5)
print("Zbiór długości słów:", word_lengths)
print("Wspólny zbiór:", common_set)
print("Czy wspólny zbiór jest podzbiorem referencyjnego?:", is_subset)