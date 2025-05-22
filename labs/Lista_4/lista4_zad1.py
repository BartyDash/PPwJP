import random

def read_answers(file):
    try:
        with open(file, encoding="utf-8") as f:
            answers = [line.strip() for line in f if line.strip()]
        return answers
    except FileNotFoundError:
        print(f"File {file} not found.")

def ask_questions(answers):
    while True:
        question = input("Zadaj pytanie (lub wpisz 'koniec' aby zakończyć): ")
        if question.lower() == "koniec":
            print("Bye!")
            break
        elif question.endswith("?"):
            print(random.choice(answers))
        else:
            print("gdzie znak zapytania? to nie jest pytanie")
            continue

def main():
    file = "magiczna_kula.txt"
    answers = read_answers(file)
    if answers:
        ask_questions(answers)

if __name__ == "__main__":
    main()