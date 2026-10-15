zaklad_vztupenka = 500
student_vztupenka = 500 * 0.7
den_v_týdnu = input("Zadejte den v týdnu: ")
priplatek = 50 if den_v_týdnu == "sobota" or den_v_týdnu == "neděle" else 0

počet_osob = int(input("Zadejte počet osob:  "))
skupinova_vztupenka = 500 * 0.75 * počet_osob
if počet_osob >= 4:
    print("Cena za skupinu je:", skupinova_vztupenka + (priplatek * počet_osob), "Kč" and "cena za jednu osobu je:", (skupinova_vztupenka / počet_osob) + priplatek, "Kč")
elif počet_osob < 4:
    věk = float(input("Zadejte věk: "))
    senior_vztupenka = 500 * 0.8
    if věk >= 65:
        print("Cena za jednoho seniora je:", senior_vztupenka + priplatek, "Kč")
    elif věk >= 26 and věk < 65:
        print("Cena za jednoho dospělého je:", zaklad_vztupenka + priplatek, "Kč")
    else:
        student = input("Jste student?: (ano/ne) ")
        if věk <= 26 and student == "ano":
            print("Cena za jednoho studenta je:", student_vztupenka + priplatek, "Kč")