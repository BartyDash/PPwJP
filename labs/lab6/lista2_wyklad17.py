# Zadanie 17 
# Sprawdź, jaka jest różnica między instrukcją L.insert(2, -1) a przypisaniem L[2] = -1 dla dowolnej listy L.
# Metoda append() pozwala dodawać elementy na koniec listy. W jaki sposób można
# dodawać elementy zarówno na początek, jak i na koniec listy, korzystając z metody
# insert()?
# Uwaga: Twoje rozwiązanie powinno działać dla listy o dowolnej długości.

def compare_insert_vs_assignment():
    print("Część 1: Różnica między L.insert(2, -1) a L[2] = -1")
    print("-" * 50)
    
    L1 = [10, 20, 30, 40, 50]
    print(f"Lista początkowa: {L1}")
    
    L_copy1 = L1.copy()
    L_copy1.insert(2, -1)
    print(f"Po L.insert(2, -1): {L_copy1}")
    
    L_copy2 = L1.copy()
    L_copy2[2] = -1
    print(f"Po L[2] = -1: {L_copy2}")
    print()
    
    L2 = [10, 20]
    print(f"Lista początkowa (krótka): {L2}")
    
    L_copy3 = L2.copy()
    L_copy3.insert(2, -1)
    print(f"Po L.insert(2, -1): {L_copy3}")
    
    L_copy4 = L2.copy()
    try:
        L_copy4[2] = -1
        print(f"Po L[2] = -1: {L_copy4}")
    except IndexError:
        print("L[2] = -1 generuje błąd IndexError dla krótkiej listy")
    print()
    

def add_elements_using_insert():
    print("Część 2: Dodawanie elementów na początek i koniec listy za pomocą insert()")
    print("-" * 50)
    
    L = [10, 20, 30]
    print(f"Lista początkowa: {L}")
    
    L.insert(0, 5)
    print(f"Po dodaniu 5 na początek: {L}")
    
    L.insert(len(L), 40)
    print(f"Po dodaniu 40 na koniec: {L}")
    
    print("\nFunkcja do dodawania elementów na początek i koniec listy:")
    
    def add_to_both_ends(lst, start_value, end_value):
        lst.insert(0, start_value)
        lst.insert(len(lst), end_value)
        return lst
    
    test_list = [100, 200, 300]
    print(f"Lista testowa: {test_list}")
    result = add_to_both_ends(test_list, 50, 400)
    print(f"Po dodaniu 50 na początek i 400 na koniec: {result}")
    
    empty_list = []
    print(f"\nPusta lista: {empty_list}")
    result = add_to_both_ends(empty_list, 1, 2)
    print(f"Po dodaniu 1 na początek i 2 na koniec: {result}")
    

if __name__ == "__main__":
    compare_insert_vs_assignment()
    add_elements_using_insert()