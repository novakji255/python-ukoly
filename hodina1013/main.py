počet_osob = int(input("Zadejte počet osob:  "))
if počet_osob >= 4:
     print( "Cena za skupinu je:", skupinova_vztupenka, "Kč" and "cena za jednu osobu je:", skupinova_vztupenka / počet_osob, "Kč")
věk = float(input("Zadejte věk: "))
if věk >= 65:
    print("Cena za jednoho seniora je:", senior_vztupenka, "Kč")
student = input("Jste student?: (ano/ne) ")


zaklad_vztupenka = 500
student_vztupenka = 500 * 0.7
senior_vztupenka = 500 * 0.8
skupinova_vztupenka = 500 * 0.75 * počet_osob

if počet_osob >= 4:
    print("Cena za skupinu je:", skupinova_vztupenka, "Kč" and "cena za jednu osobu je:", skupinova_vztupenka / počet_osob, "Kč")
elif věk <= 26 and student == "ano":
    print("Cena za jednoho studenta je:", student_vztupenka, "Kč")
elif věk >= 65:
    print("Cena za jednoho seniora je:", senior_vztupenka, "Kč")
else:
    print("Cena jedné vstupenky je:", zaklad_vztupenka, "Kč")