import random

def set_ships():
    ships = set()
    while len(ships) < 5:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        ships.add((x, y))
    return ships

def print_board(board):
    print("   " + " ".join(str(i) for i in range(10)))
    for i, row in enumerate(board):
        print(f"{i:2} " + " ".join(row))

def game():
    board = [['.' for _ in range(10)] for _ in range(10)]
    ships = set_ships()
    moves = 0
    hits = 0

    while hits < 5:
        print_board(board)
        row = int(input("Podaj wiersz (0-9): "))
        col = int(input("Podaj kolumnę (0-9): "))
        moves += 1

        if (row, col) in ships:
            if board[row][col] == 'X':
                print("Już trafileś tutaj.")
            else:
                print("Trafiony!")
                board[row][col] = 'X'
                hits += 1
        else:
            if board[row][col] in ['X', 'O']:
                print("Już sprawdzales to pole.")
            else:
                print("Pudło.")
                board[row][col] = 'O'

    print_board(board)
    print(f"Zatopiono wszystkie statki w {moves} ruchach!")

game()
