# """
# projekt2.py: druhý projekt do Engeto Online kurzu Tester s Pythonem

# author: Ivana Molnárová
# email: ivaryd@post.cz
# """

from random import randint

uvodni_text = """Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
Enter a number:
"""
upraveny_text = uvodni_text.split("\n")

delky_vet = [len(veta) for veta in upraveny_text]

print(f"""{upraveny_text[0]}
{"-" * (max(delky_vet))}
{upraveny_text[1]}
{upraveny_text[2]}
{"-" * (max(delky_vet))}""")

cislo = input(f"""{upraveny_text[3]:} """)
print(f"""{"-" * (max(delky_vet))}""")

def generator_cisel_hra(pocet_cisel):
    vybrana_cisla = set()
    while len(vybrana_cisla) < pocet_cisel:
        cislo = randint(0, 9)
        vybrana_cisla.add(cislo)
        cisla_ke_hre = str(vybrana_cisla).replace("{","").replace(".","").replace("}","").replace(",","").replace(" ","")
        if cisla_ke_hre[0] == "0":
            vybrana_cisla.remove(0)
    return cisla_ke_hre
    
