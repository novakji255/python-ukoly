
print("mysli si cislo a pocitac ho uhodne")
print("odpovidej takhle:")
print("v - VĚTŠÍ")
print("m - MENŠÍ")
print("s - SPRÁVNĚ")

dole = 1
nahore = 100
pokusy = 0
odpoved = ""

while odpoved != "s":
    tip = (dole + nahore) // 2
    pokusy += 1
    
    print(f"pokus č. {pokusy}: {tip}")
    odpoved = input("(v / m / s): ")
    
    if odpoved == "v":
        dole = tip + 1
    elif odpoved == "m":
        nahore = tip - 1
    elif odpoved == "s":
        print(f"tvoje číslo je {tip} - {pokusy} pokusů.")
    else:
        print("zadej pouze v, m nebo s")
        pokusy -= 1  
    