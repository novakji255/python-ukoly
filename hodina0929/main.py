# *************************
# Kalkulacka spropitneho
# 29.9.2026
# *************************

print("vitejte v kalkulacce spropitneho!")
celkova_castka = float(input("zadejcelkovou castku uctu"))
spropitne = int(input("zadejspropitne v %: "))
pocet_lidi = int(input("zadej pocet lidi u stolu: "))

spropitne_Kc = celkova_castka * spropitne / 100
celkova_castka += spropitne_Kc #slozene prirazeni
#celkova_castka = celkova_caastka + spropitne_Kc
zaplacena_castka = round (celkova_castka / pocet_lidi, 2)

print(f"zaplatit: 1/{pocet_lidi} z {celkova_castka} Kč ( {zaplacena_castka} Kč)")