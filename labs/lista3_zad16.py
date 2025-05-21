import random

def generate_random_grid(n):
    return [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]

def find_fours(grid):
    n = len(grid)
    marked = set()

    def mark(i, j, di, dj):
        val = grid[i][j]
        coords = [(i + k * di, j + k * dj) for k in range(4)]
        print(coords)
        if all(0 <= x < n and 0 <= y < n and grid[x][y] == val for x, y in coords):
            marked.update(coords)

    for i in range(n):
        for j in range(n):
            if j <= n - 4:
                mark(i, j, 0, 1)  # poziomo prawo
            if i <= n - 4:
                mark(i, j, 1, 0)  # pionowo dół
            if i <= n - 4 and j <= n - 4:
                mark(i, j, 1, 1)  # ukośnie prawo
            if i <= n - 4 and j >= 3:
                mark(i, j, 1, -1) # ukośnie lewo

    return marked

def display_grid(grid, highlights=set()):
    for i, row in enumerate(grid):
        line = ""
        for j, val in enumerate(row):
            if (i, j) in highlights:
                line += f"[{val}] "
            else:
                line += f" {val}  "
        print(line)
    print()

def simulation():
    while True:
        while True:
            try:
                n = int(input("Podaj rozmiar tablicy (10-20): "))
                if 10 <= n <= 20:
                    break
                else:
                    print("Podaj liczbę z zakresu 10-20.")
            except ValueError:
                print("To nie jest liczba całkowita.")

        grid = generate_random_grid(n)
        highlights = find_fours(grid)

        print("\nWygenerowana tablica (czwórki oznaczone nawiasami []):")
        display_grid(grid, highlights)

        again = input("Czy chcesz uruchomić kolejną symulację? (t/n): ").strip().lower()
        if again != 't':
            break

if __name__ == "__main__":
    simulation()