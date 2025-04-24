# Zadanie 6 
# Napisz funkcję, która będzie zwracała wartość True, jeżeli przekazany jej ciąg
# tekstowy będzie zawierał zrównoważoną liczbę nawiasów, tj. każdy otwarty nawias
# powinien być zamknięty. W przeciwnym wypadku funkcja powinna zwracać wartość
# False. Uwzględnij cztery rodzaje nawiasów: (), [], {} oraz <>. Wykorzystaj słowniki.

def is_balanced_brackets(text):
    bracket_pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    stack = []

    for char in text:
        if char in bracket_pairs:
            stack.append(char)
        elif char in bracket_pairs.values():
            if not stack or bracket_pairs[stack.pop()] != char:
                return False

    return not stack


print(is_balanced_brackets("({[]})"))
print(is_balanced_brackets("({[})"))
print(is_balanced_brackets("<{[()]}>"))
print(is_balanced_brackets("<<>>"))
print(is_balanced_brackets("<<>"))