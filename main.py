# """
# projekt2.py: druhý projekt do Engeto Online kurzu Tester s Pythonem
# author: Ivana Molnárová
# email: ivaryd@post.cz
# """

from random import randint
from datetime import datetime
     
def pocet_znaku_nejdelsiho_radku(text: str) -> int:
    """
    Projde jednotlivé řádky textu, nalezne na jakém z nich je nejdelší text a vrátí počet jeho znaků.
    """
    upraveny_text = text.split("\n")
    delky_vet = [len(veta) for veta in upraveny_text]
    return max(delky_vet)

def uprav_uvodni_text(text: str) -> str:
    """
    Naformátuje zadaný text.
    """
    upraveny_text = text.split("\n")
    return (f"""{upraveny_text[0]}
{"-" * pocet_znaku_nejdelsiho_radku(text)}
{upraveny_text[1]}
{upraveny_text[2]}
{"-" * pocet_znaku_nejdelsiho_radku(text)}
{upraveny_text[3]:}
{"-" * pocet_znaku_nejdelsiho_radku(text)}""")

def generator_cisel(pocet_cisel: int) -> str:
    """
    Vygeneruje určitý počet náhodných čísel - dle zadaného počtu, číslo nesmí začínat nulou, číslice musí být unikátní
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
    K určenému slovu zadat koncovku "s" pokud se jedná o množné číslo nebo počet 0
    """
    if number == 1:
        return objekt
    else:
        return objekt + "s"
    
def pocet_bull(hracovo_hadani: str, vygenerovane_cislo: str) -> int:
    """
    Vrátí kolik hádaných čísel je správně uhodnuto se správným umístěním
    """
    bull = 0
    for i in range(0, len(vygenerovane_cislo)):
        if hracovo_hadani[i] == vygenerovane_cislo[i]:
            bull = bull + 1
    return bull

def pocet_cow(hracovo_hadani: str, vygenerovane_cislo: str) -> int:
    """
    Vrátí kolik hádaných čísel je správně uhodnuto, ale v nesprávném umístění
    """
    cow = 0
    for i in range(0, len(vygenerovane_cislo)):
        if (hracovo_hadani[i] != vygenerovane_cislo[i]) and (hracovo_hadani[i] in vygenerovane_cislo):
            cow = cow + 1
    return cow

def doba_hadani(start_time: datetime, end_time: datetime) -> str:
    """
    Doba trvání od začátku nějaké činnosti do jejího konce - časový údaj vrací v minutách a sekundách
    """
    celkove_vteriny = (end_time - start_time).total_seconds()
    minuty = int(celkove_vteriny / 60)
    vteriny = int(celkove_vteriny % 60)
    return minuty, vteriny
     
hra_cislo = 1
statistika = {}
while True:
    uvodni_text = """Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
Enter a number:
"""

    vygenerovane_cislo = generator_cisel(4)
    print(vygenerovane_cislo)
    print(uprav_uvodni_text(uvodni_text))
    hrac_hada = input(">>> ")

    start_time = datetime.now()

    while over_vstup_hrace(hrac_hada, len(vygenerovane_cislo)) != "OK":
        print(f"{"-" * pocet_znaku_nejdelsiho_radku(uvodni_text)}")
        hrac_hada = input(">>> ")
    #chci do pokusů započítat jen relevantní "správně" zadané inputy, nesprávně zadané budu ignorovat - nebudu je započítávat
    pokus = 1
    
    while hrac_hada != vygenerovane_cislo:
        pokus = pokus + 1
        bull_count = pocet_bull(hrac_hada, vygenerovane_cislo)
        regural_plural_bull = jednotne_nebo_mnozne(bull_count, "bull")
        cow_count = pocet_cow(hrac_hada, vygenerovane_cislo)
        regural_plural_cow = jednotne_nebo_mnozne(cow_count, "cow")
        print(f"{bull_count} {regural_plural_bull}, {cow_count} {regural_plural_cow}")
        print(f"{"-" * pocet_znaku_nejdelsiho_radku(uvodni_text)}")
        hrac_hada = input(">>> ")
        while over_vstup_hrace(hrac_hada, len(vygenerovane_cislo)) != "OK":
            print(f"{"-" * pocet_znaku_nejdelsiho_radku(uvodni_text)}")
            hrac_hada = input(">>> ")
    else:
        end_time = datetime.now()
        print("Correct, you've guessed the right number\nin " + str(pokus) + " guesses!")
        print(f"{"-" * pocet_znaku_nejdelsiho_radku(uvodni_text)}")
        print("That's amazing!")
        min, sec = doba_hadani(start_time, end_time)
        print(f"Guess time: {min} min {sec} s")
        print(f"{"-" * pocet_znaku_nejdelsiho_radku(uvodni_text)}")
        statistika[hra_cislo] = pokus
    hra_cislo = hra_cislo + 1
    print(f"""Statistika her - číslo hry: počet pokusů
{statistika}""")
    print(f"{"-" * pocet_znaku_nejdelsiho_radku(uvodni_text)}")

