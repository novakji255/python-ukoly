import math

#kontrola prvocisla
je_prvocislo = True

print(f"Kontrola prvocisla")
cislo = int(input("Zadej cislo: "))

if cislo < 2:
    je_prvocislo = False
elif cislo == 2:
    je_prvocislo = True
elif cislo % 2 == 0:
    je_prvocislo = False
else:
    delitel = 3
    while delitel < math.sqrt(cislo) + 1:
        if cislo % delitel == 0:
            je_prvocislo = False
            break
        delitel += 2

if je_prvocislo:
    print(f"Cislo {cislo} je prvocislo")
else:
    print(f"Cislo {cislo} neni prvocislo")