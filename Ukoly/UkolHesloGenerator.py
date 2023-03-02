# importuje moduly
import string
import random


# uloží všechny charaktery do listů
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)


# Zeptá se na délku hesla
user_input = input("How many characters do you want in your password? ")
characters_number = int(user_input)

# zrandomizuje listy charakterů
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)


# kalkuluje 30% & 20% z čísel a charakterů
part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))


# vygeneruje heslo 60:40 ratio pismena:cisla
result = []

for x in range(part1):

	result.append(s1[x])
	result.append(s2[x])

for x in range(part2):

	result.append(s3[x])
	result.append(s4[x])


# zrandomizuje vásledek
random.shuffle(result)


# joinuje? vysledek
password = "".join(result)
print("Strong Password: ", password)
