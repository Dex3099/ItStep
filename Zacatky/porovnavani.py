#tento program porovnává 2 čísla
print("tento program porovnává 2 celé čísla")
vstup1 = int(input("Zadej celé číslo: "))
vstup2 = int(input("Zadej celé číslo: "))
print(f"{vstup1} > {vstup2}  {vstup1 > vstup2}")
print(f"{vstup1} < {vstup2}  {vstup1 < vstup2}")
print(f"{vstup1} = {vstup2}  {vstup1 == vstup2}")
if vstup1 < vstup2:
  print(f"{vstup1} je menší než {vstup2}")

if vstup1 > vstup2:
  print(f"{vstup1} je větší než {vstup2}")

if vstup1 == vstup2:
  print(f"{vstup1} se rovná {vstup2}")
