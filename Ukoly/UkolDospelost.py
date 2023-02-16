#tento program porovnává 2 čísla
print("vám řekne jestli jste dospeli")
vstup1 = int(input("Zadejte vas věk: "))
dospelost = 18
if vstup1 < dospelost:
  print("Si nedospely takže nemusis platit daně a nemuzes lozit na stranky pro dospele")

if vstup1 > dospelost:
  print("Si dospěly takže musis platit daně ale muzes jit na stranky pro dospele")
  
if vstup1 == dospelost:
  print("Si dospěly takže musis platit daně")
