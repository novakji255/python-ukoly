pocet_mesicu = int(input("Zadejte počet měsíců simulace: "))

a = 1
b = 1
mesic = 1

print(f"Simulace růstu králíků pro {pocet_mesicu} měsíců:")

while mesic <= pocet_mesicu:
  kralici = "🐰" * a
  print(f"Měsíc {mesic}: {a} párů {kralici}")

  dopredu = a + b
  a = b
  b = dopredu

  mesic = mesic + 1