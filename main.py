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