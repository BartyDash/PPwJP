# Zadanie 7
# Napisz program, który pobierze od użytkownika napis. Program powinien
# wyświetlić informację, z ilu różnych znaków składa się dany wyraz. Zadanie powinna
# realizować funkcja.

def count_unique_characters(text):
    unique_characters = set(text)
    return len(unique_characters)


user_input = input("Podaj napis: ")

unique_count = count_unique_characters(user_input)
print(f"Napis składa się z {unique_count} różnych znaków.")