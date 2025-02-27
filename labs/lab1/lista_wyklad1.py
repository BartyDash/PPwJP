# Zadanie 1 
# Pewien sklep prowadzi sprzedaż i wprowadził promocję. Klient dostaje 10%
# zniżki na zakupy o wartości 100 zł lub niższej i 20% zniżki na zakupy większe niż 100
# zł. Napisz program, który poprosi o cenę zakupów i wyświetli uzyskany rabat oraz
# ostateczną cenę za zakupy

cena_zakupow = float(input("Podaj cenę zakupów: "))
if cena_zakupow <= 100:
    rabat = 0.1
else:
    rabat = 0.2

uzysk_rabat = cena_zakupow * rabat
cena_zakupow_po_rabacie = cena_zakupow - uzysk_rabat
print(f"Rabat: {uzysk_rabat:.2f}zł")
print(f"Cena zakupów po rabacie: {cena_zakupow_po_rabacie:.2f}zł")