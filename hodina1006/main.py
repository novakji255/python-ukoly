#polarita proměnné

cislo = float(input("Zadej číslo: "))

if cislo>0:
    print("Kladné číslo")
elif cislo==0:
    print("Nula")
elif cislo<0:
    print("Záporné číslo")  
cislo = -cislo   
   
print(f"Absolutní hodnota je {cislo}")