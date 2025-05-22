import statistics

def analyze_line(line, line_number):
    try:
        numbers = [float(x) for x in line.strip().split()]
        if not numbers:
            print(f"Linia {line_number} jest pusta.")
            return
        
        mean = statistics.mean(numbers)
        median = statistics.median(numbers)
        print(f"Wiersz {line_number:3d}: ilość = {len(numbers):2d} | suma = {sum(numbers):10.3f} | min = {min(numbers):6.3f} | max = {max(numbers):6.3f} | średnia = {mean:6.3f} | mediana = {median:6.3f}")
        
    except ValueError as e:
        print(f"Błąd w linii {line_number}: {e}")
    except statistics.StatisticsError as e:
        print(f"Błąd w linii {line_number}: {e}")


def read_file(file_name):
    try:
        with open(file_name, encoding="utf-8") as f:
            for number, line in enumerate(f, 1):
                analyze_line(line, number)
    except FileNotFoundError:
        print(f"Plik {file_name} nie został znaleziony.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    read_file("numbers.txt")