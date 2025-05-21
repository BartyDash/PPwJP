import random

SYMBOLS = ["wiśnie", "pomarańcze", "śliwki", "dzwonki", "melony", "sztabki"]

def draw_symbols():
    return [random.choice(SYMBOLS) for _ in range(3)]

def calculate_winnings(bet, symbols):
    unique = set(symbols)
    if len(unique) == 1:
        return bet * 3
    elif len(unique) == 2:
        return bet * 2
    else:
        return 0

def play_round():
    while True:
        try:
            bet = float(input("Wrzuc dowolną dodatnią sumę pieniędzy: "))
            if bet <= 0:
                print("Kwota musi być większa od zera.")
                continue
            break
        except ValueError:
            print("Niepoprawna kwota. Spróbuj ponownie.")

    symbols = draw_symbols()
    print("Wylosowane symbole:", " | ".join(symbols))

    winnings = calculate_winnings(bet, symbols)
    if winnings == 0:
        print("Brak wygranej.")
    else:
        print(f"Gratulacje! Wygrywasz {winnings:.2f} zł.")

    return bet, winnings

def main():
    total_inserted = 0
    total_won = 0

    print("=== Jednoręki Bandyta! ===")

    while True:
        bet, winnings = play_round()
        total_inserted += bet
        total_won += winnings

        again = input("Czy chcesz zagrać ponownie? (t/n): ").strip().lower()
        if again != 't':
            break

    print("\n=== Podsumowanie gry ===")
    print(f"Łączna wrzucona kwota: {total_inserted:.2f} zł")
    print(f"Łączna wygrana kwota: {total_won:.2f} zł")
    print("Dziękujemy za grę!")

if __name__ == "__main__":
    main()