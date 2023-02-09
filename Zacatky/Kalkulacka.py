#uložíme data do proměnných
print ("Napište první číslo a potom * nebo / nebo + nebo - a potom druhé číslo")
vstup1 = float(input("Zadej první číslo: "))
vstup2 = float(input("Zadej druhé číslo: "))
#vysledek udela 
vysledek = vstup1 + vstup2
#napíše výsledek
print(f"Vysledek je {vysledek}")
#napíše operaci kterou to vypočítalo a výsledek za =
print(f"{vstup1} + {vstup2} = {vstup1 + vstup2}")
print(f"{vstup1} - {vstup2} = {vstup1 - vstup2}")
print(f"{vstup1} * {vstup2} = {vstup1 * vstup2}")
print(f"{vstup1} ** {vstup2} = {vstup1 ** vstup2}")
print(f"{vstup1} / {vstup2} = {vstup1 / vstup2}")
print(f"{vstup1} // {vstup2} = {vstup1 // vstup2}")
print(f"{vstup1} % {vstup2} = {vstup1 % vstup2}")
