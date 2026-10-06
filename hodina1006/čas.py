čas = int(input("Zadej čas: "))
if čas < 0 or čas > 24:
    print("není čas")
elif čas < 6:
    print("noc")
elif čas < 9:
    print("ráno")
elif čas < 12:
    print("dopoledne")
elif čas < 13:
    print("poledne")
elif čas < 18:
    print("odpoledne")
elif čas < 22:
    print("večer")
else:
    print("noc")