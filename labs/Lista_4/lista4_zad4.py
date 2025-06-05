import os

def get_numbers():
    while True:
        try:
            numbers = input("Podaj 6 unikalnych liczb 1-49. Oddziel spacjami: ").split()
            numbers = list(map(int, numbers))

            if len(numbers) != 6:
                print("Musisz podać dokładnie 6 liczb.")
                continue
            if len(set(numbers)) != 6:
                print("Muszą być unikalne!")
                continue

            return set(numbers)
        except ValueError as e:
            print(e)

def main():
    my_numbers = get_numbers()

if __name__ == "__main__":
    main()