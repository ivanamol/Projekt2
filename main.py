# """
# projekt2.py: druhý projekt do Engeto Online kurzu Tester s Pythonem

# author: Ivana Molnárová
# email: ivaryd@post.cz
# """

from random import randint

def uprav_uvodni_text(text: str):
    upraveny_text = text.split("\n")
    delky_vet = [len(veta) for veta in upraveny_text]
    return print(f"""{upraveny_text[0]}
{"-" * (max(delky_vet))}
{upraveny_text[1]}
{upraveny_text[2]}
{"-" * (max(delky_vet))}""")


def generator_cisel_hra(pocet_cisel: int):
    vybrana_cisla = set()
    while len(vybrana_cisla) < pocet_cisel:
        cislo = randint(0, 9)
        vybrana_cisla.add(cislo)
        cisla_ke_hre = str(vybrana_cisla).replace("{","").replace(".","").replace("}","").replace(",","").replace(" ","")
        if cisla_ke_hre[0] == "0":
            vybrana_cisla.remove(0)
    return cisla_ke_hre

def over_zadany_vstup_hrace(vstup_hrace: str, pocet_cisel: int, ):
    if not hrac_hada.isdigit():
        return print("The input other than a number.")
    elif len(hrac_hada) != pocet_cisel:
        return print("The input does not contain exactly 4 numbers.")
    elif not hrac_hada.isdigit():
        return print("The input other than a number")
    elif hrac_hada[0] == "0":
        return print("The number must not start with a zero.")
    elif len(hrac_hada) != len(set(hrac_hada)):
        return print("The number must not contain duplicates")
    else:
        return print("bla")


uvodni_text = """Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
Enter a number:
"""

uprav_uvodni_text(uvodni_text)

hrac_hada = input("Enter a number: ")
print(f"{"-" * 47}")

over_zadany_vstup_hrace(hrac_hada, 4)



