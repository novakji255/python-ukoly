import random
tajne_cislo = random.randint(1, 20)
pocitadlo = 0
tip = 0
max_pokusy = 5

print(f"hádej číslo mezi 1 a 20, máš {max_pokusy} pokusů")

while tip!= tajne_cislo and pocitadlo < max_pokusy:
    tip = int(input("zadej svuj tip: "))
    if tip < 1 or tip > 20:
        print("tip musí být mezi 1 a 20")
        continue
    pocitadlo += 1
    if tip > tajne_cislo:
        print("tajne cislo je mensi")
    elif tip < tajne_cislo:
        print("tajne cislo je vetsi")
    
if tip == tajne_cislo:
    print(f"uhodl jsi cislo {tajne_cislo} na {pocitadlo} pokusy")
else:
    print(f"překročil jsi {max_pokusy} pokusů, číslo bylo {tajne_cislo}")