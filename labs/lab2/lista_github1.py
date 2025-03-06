# Wypisz wszystkie liczby od 1 do 50, jednak jeżeli liczba jest podzielna przez: trzy – zamiast liczby wypisz „Fizz”,
# pięć – wypisz „Buzz”, jeśli jest podzielna zarówno przez trzy i pięć - wypisz „FizzBuzz”.

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# for i in range(1, 51):
#     if i % 3 == 0:
#         if i % 5 == 0:
#             print('FizzBuzz')
#         else:
#             print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)