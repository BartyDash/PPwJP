# 4. Przetestuj, które z omówionych powyżej typow danych można użyc w roli klucza w słowniku. 
# Następnie porównaj swoje obserwacje z informacjami w [tym artykule](https://wiki.python.org/moin/DictionaryKeys).

test_dict = {}

test_dict[52] = 'test'
test_dict[52.0] = 'test'
test_dict['test'] = 'test'
test_dict[True] = 'test'
test_dict[complex(1, 2)] = 'test'
test_dict[(1, 2)] = 'test'
test_dict[None] = 'test'
test_dict[object()] = 'test'
test_dict[[1, 2]] = 'test'  #niet
test_dict[{1: 'test'}] = 'test'  #niet
test_dict[{1, 2, 3}] = 'test'   #niet