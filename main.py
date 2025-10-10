# """
# projekt2.py: druhý projekt do Engeto Online kurzu Tester s Pythonem

# author: Ivana Molnárová
# email: ivaryd@post.cz
# """

from random import randint

def uprav_uvodni_text(text: str):
    upraveny_text = text.split("\n")
    delky_vet = [len(veta) for veta in upraveny_text]
    print(f"""{upraveny_text[0]}
{"-" * (max(delky_vet))}
{upraveny_text[1]}
{upraveny_text[2]}
{"-" * (max(delky_vet))}""")
    hrac_hada = input(f"""{upraveny_text[3]:} """)
    return hrac_hada


def generator_cisel_hra(pocet_cisel: int):
    vybrana_cisla = set()
    while len(vybrana_cisla) < pocet_cisel:
        cislo = randint(0, 9)
        vybrana_cisla.add(cislo)
        cisla_ke_hre = str(vybrana_cisla).replace("{","").replace(".","").replace("}","").replace(",","").replace(" ","")
        if cisla_ke_hre[0] == "0":
            vybrana_cisla.remove(0)
    return cisla_ke_hre


def over_vstup_hrace(hracovo_hadani: str, pocet_cisel: int, ):
    if not hracovo_hadani.isdigit():
        return print("The input other than a number.")
    elif len(hracovo_hadani) != pocet_cisel:
        return print(f"The input does not contain exactly {pocet_cisel} numbers.")
    elif not hracovo_hadani.isdigit():
        return print("The input other than a number")
    elif hracovo_hadani[0] == "0":
        return print("The number must not start with a zero.")
    elif len(hracovo_hadani) != len(set(hracovo_hadani)):
        return print("The number must not contain duplicates")
    

def jednotne_nebo_mnozne(number: int, objekt: str):
    if number == 1:
        return objekt
    else:
        return objekt + "s"
    

def pocet_bull(hracovo_hadani: str, vygenerovane_cislo: str):
    bull = 0
    if (hracovo_hadani[0] == vygenerovane_cislo[0]):
        bull = bull + 1
    if (hracovo_hadani[1] == vygenerovane_cislo[1]):
        bull = bull + 1
    if (hracovo_hadani[2] == vygenerovane_cislo[2]):
        bull = bull + 1
    if (hracovo_hadani[3] == vygenerovane_cislo[3]):
        bull = bull + 1
    pocet = jednotne_nebo_mnozne(bull, "bull")
    return print(f"{bull} {pocet}")


def pocet_cow(hracovo_hadani: str, vygenerovane_cislo: str):
    cow = 0
    if (hracovo_hadani[0] != vygenerovane_cislo[0]) and (hracovo_hadani[0] in vygenerovane_cislo):
            cow = cow + 1
    if (hracovo_hadani[1] != vygenerovane_cislo[1]) and (hracovo_hadani[1] in vygenerovane_cislo):
            cow = cow + 1
    if (hracovo_hadani[2] != vygenerovane_cislo[2]) and (hracovo_hadani[2] in vygenerovane_cislo):
            cow = cow + 1
    if (hracovo_hadani[3] != vygenerovane_cislo[3]) and(hracovo_hadani[3] in vygenerovane_cislo):
            cow = cow + 1
    pocet = jednotne_nebo_mnozne(cow, "cow")
    return print(f"{cow} {pocet}")
    

# pocet_bull(str(1234), str(1324))
# pocet_cow(str(1234), str(6935))

uvodni_text = """Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
Enter a number:
"""

vygenerovane_cislo = generator_cisel_hra(4)
print(vygenerovane_cislo)

hrac_hada = uprav_uvodni_text(uvodni_text)
print(hrac_hada)

over_vstup_hrace(hrac_hada, 4)
print(f"{"-" * 47}")

pokus = 1



# while hrac_hada != vygenerovane_cislo:
#     cow = 0
#     if (hrac_hada[0] != vygenerovane_cislo[0]) and (hrac_hada[0] in vygenerovane_cislo):
#         cow = cow + 1
#     if (hrac_hada[1] != vygenerovane_cislo[1]) and (hrac_hada[1] in vygenerovane_cislo):
#         cow = cow + 1
#     if (hrac_hada[2] != vygenerovane_cislo[2]) and (hrac_hada[2] in vygenerovane_cislo):
#         cow = cow + 1
#     if (hrac_hada[3] != vygenerovane_cislo[3]) and (hrac_hada[3] in vygenerovane_cislo):
#         cow = cow + 1
#     pocet = jednotne_nebo_mnozne(cow, "cow")
#     print(f"{cow} {pocet}")
#     hrac_hada = input("Enter a number: ")
#     over_vstup_hrace(hrac_hada, 4)
# else:
#     print(f"Correct, you've guessed the right number in {pokus} guesses!")



# while hrac_hada != vygenerovane_cislo:
#     bull = 0
#     if (hrac_hada[0] == vygenerovane_cislo[0]):
#         bull = bull + 1
#     if (hrac_hada[1] == vygenerovane_cislo[1]):
#         bull = bull + 1
#     if (hrac_hada[2] == vygenerovane_cislo[2]):
#         bull = bull + 1
#     if (hrac_hada[3] == vygenerovane_cislo[3]):
#         bull = bull + 1
#     pocet = jednotne_nebo_mnozne(bull, "bull")
#     print(f"{bull} {pocet}")
#     hrac_hada = input("Enter a number: ")
#     if over_vstup_hrace(hrac_hada, 4) != "OK":
#             hrac_hada = input("Enter a number: ")
# else:
#     print(f"Correct, you've guessed the right number in {pokus} guesses!")
