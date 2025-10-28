# """
# projekt2.py: druhý projekt do Engeto Online kurzu Tester s Pythonem
# author: Ivana Molnárová
# email: ivaryd@post.cz
# """

from random import randint
from datetime import datetime
     
def pocet_znaku_nejdelsi_vety(text: str) -> int:
    """
    Projde jednotlivé řádky, nalezne na jakém z nich je nejdelší text a vrátí počet jeho znaků
    """
    upraveny_text = text.split("\n")
    delky_vet = [len(veta) for veta in upraveny_text]
    return max(delky_vet)

def uprav_uvodni_text(text: str) -> str:
    """
    Naformátuje zadaný text
    """
    upraveny_text = text.split("\n")
    return (f"""{upraveny_text[0]}
{"-" * pocet_znaku_nejdelsi_vety(text)}
{upraveny_text[1]}
{upraveny_text[2]}
{"-" * pocet_znaku_nejdelsi_vety(text)}
{upraveny_text[3]:}
{"-" * pocet_znaku_nejdelsi_vety(text)}""")

def generator_cisel_hra(pocet_cisel: int) -> str:
    """
    Vygeneruje náhodná čísla - dle zadaného počtu
    """
    vybrana_cisla = set()
    while len(vybrana_cisla) < pocet_cisel:
        cislo = randint(0, 9)
        vybrana_cisla.add(cislo)
        cisla_ke_hre = str(vybrana_cisla).replace("{","").replace(".","").replace("}","").replace(",","").replace(" ","")
        if cisla_ke_hre[0] == "0":
            vybrana_cisla.remove(0)
    return cisla_ke_hre

def over_vstup_hrace(hracovo_hadani: str, pocet_cisel: int) -> str:
    """
    Ověří, zda hráč zadal číslo, se kterým může hra pokračovat, pokud ne, vrátí hráči upozornění, z jakého důvodu není možné daný vstup použít
    """
    if not hracovo_hadani.isdigit():
        return print("The input other than a number.")
    elif len(hracovo_hadani) != pocet_cisel:
        return print(f"The input does not contain exactly {pocet_cisel} numbers.")
    elif hracovo_hadani[0] == "0":
        return print("The number must not start with a zero.")
    elif len(hracovo_hadani) != len(set(hracovo_hadani)):
        return print("The number must not contain duplicates.")
    else:
         return "OK"
    
def jednotne_nebo_mnozne(number: int, objekt: str) -> str:
    """
    Jde o ropoznání, zda dát koncovku "s" u množného čísla nebo nuly
    """
    if number == 1:
        return objekt
    else:
        return objekt + "s"
    
def pocet_bull(hracovo_hadani: str, vygenerovane_cislo: str) -> str:
    """
    Vrátí kolik hádaných čísel je správně uhodnuto a se správným umístěním
    """
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
    return (f"{bull} {pocet}")

def pocet_cow(hracovo_hadani: str, vygenerovane_cislo: str):
    """
    Vrátí kolik hádaných čísel je správně uhodnuto, ale v nesprávném umístění
    """
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
    return (f"{cow} {pocet}")

def doba_hadani(start_time, end_time):
    celkove_vteriny = (end_time - start_time).total_seconds()
    minuty = int(celkove_vteriny / 60)
    vteřiny = int(celkove_vteriny % 60)
    return (f"Guess time: {minuty} min {vteřiny} s")
     
hra_cislo = 1
statistika = {}
while True:
    uvodni_text = """Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
Enter a number:
"""

    vygenerovane_cislo = generator_cisel_hra(4)
    print(vygenerovane_cislo)
    print(uprav_uvodni_text(uvodni_text))
    hrac_hada = input(">>> ")
    start_time = datetime.now()
    while over_vstup_hrace(hrac_hada, 4) != "OK":
        print(f"{"-" * pocet_znaku_nejdelsi_vety(uvodni_text)}")
        hrac_hada = input(">>> ")
    pokus = 1
    while hrac_hada != vygenerovane_cislo:
        pokus = pokus + 1
        print(pocet_bull(hrac_hada, vygenerovane_cislo))
        print(pocet_cow(hrac_hada, vygenerovane_cislo))
        print(f"{"-" * pocet_znaku_nejdelsi_vety(uvodni_text)}")
        hrac_hada = input(">>> ")
        while over_vstup_hrace(hrac_hada, 4) != "OK":
            print(f"{"-" * pocet_znaku_nejdelsi_vety(uvodni_text)}")
            hrac_hada = input(">>> ")
    else:
        end_time = datetime.now()
        print("Correct, you've guessed the right number\nin " + str(pokus) + " guesses!")
        print(f"{"-" * pocet_znaku_nejdelsi_vety(uvodni_text)}")
        print("That's amazing!")
        guess_time = doba_hadani(start_time, end_time)
        print(guess_time)
        print(f"{"-" * pocet_znaku_nejdelsi_vety(uvodni_text)}")
        statistika[hra_cislo] = pokus
    hra_cislo = hra_cislo + 1
    print(f"""Statistika her - číslo hry : počet pokusů {statistika}""")
    print(f"{"-" * pocet_znaku_nejdelsi_vety(uvodni_text)}")

