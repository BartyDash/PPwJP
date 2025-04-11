# Zadanie 8

import random

def throw():
    return random.randint(1, 6) + random.randint(1, 6)

def single_game():
    print("\n--- Nowa gra ---")
    result = throw()
    print(f"Pierwszy rzut: {result}")

    if result in [7, 11]:
        print("Wygrałeś!")
        return True
    elif result in [2, 3, 12]:
        print("Przegrałeś!")
        return False
    else:
        point = result
        print(f"Twój punkt to: {point}")
        while True:
            result = throw()
            print(f"Rzut: {result}")
            if result == point:
                print("Wygrałeś!")
                return True
            elif result == 7:
                print("Przegrałeś!")
                return False

def get_answer():
    while True:
        answer = input("Czy chcesz zagrać ponownie? (tak/nie): ").strip().lower()
        if answer in ['tak', 'nie']:
            return answer == 'tak'

def game():
    wins = 0
    losses = 0
    while True:
        if single_game():
            wins += 1
        else:
            losses += 1
        if not get_answer():
            break
    print(f"\nKoniec gry. Wygrane: {wins}, Przegrane: {losses}")

if __name__ == "__main__":
    game()