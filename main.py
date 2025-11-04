# """
# projekt2.py: druhý projekt do Engeto Online kurzu Tester s Pythonem

# author: Ivana Molnárová
# email: ivaryd@post.cz
# """

from random import randint
from datetime import datetime
     
def count_characters_longest_line(text: str) -> int:
    """
    It goes through each line of text, finds which one has the longest text, and returns the number of characters in it.
    """
    edited_text = text.split("\n")
    sentence_length = [len(sentence) for sentence in edited_text]
    return max(sentence_length)

def edit_introductory_text(text: str) -> str:
    """
    Formats the introductory text. (Necessary use of the function
    "count_characters_longest_line").
    """
    edited_text = text.split("\n")
    return (f"""{edited_text[0]}
{"-" * count_characters_longest_line(text)}
{edited_text[1]}
{edited_text[2]}
{"-" * count_characters_longest_line(text)}
{edited_text[3]:}
{"-" * count_characters_longest_line(text)}""")

def number_generator(number_of_numbers: int) -> str:
    """
    Generates the selected number of random numbers - according to the specified number, the number must not start with zero, the digits must be unique.
    """
    selected_numbers = set()
    while len(selected_numbers) < number_of_numbers:
        number = randint(0, 9)
        selected_numbers.add(number)
        numbers_play = str(selected_numbers).replace("{","").replace(".","").replace("}","").replace(",","").replace(" ","")
        if numbers_play[0] == "0":
            selected_numbers.remove(0)
    return numbers_play

def verify_player_input(player_guess: str, number_of_numbers: int) -> str:
    """
    It verifies whether the player has entered a number with which the game can continue, if not, it returns a notification to the player explaining why the input cannot be used.
    """
    if not player_guess.isdigit():
        return print("The input other than a number.")
    elif len(player_guess) != number_of_numbers:
        return print(f"The input does not contain exactly {number_of_numbers} numbers.")
    elif player_guess[0] == "0":
        return print("The number must not start with a zero.")
    elif len(player_guess) != len(set(player_guess)):
        return print("The number must not contain duplicates.")
    else:
         return "OK"
    
def singular_or_plural(number: int, noun: str) -> str:
    """
    Adds the ending "s" to the entered noun if it is plural (number > 1 or number is 0.
    """
    if number == 1:
        return noun
    else:
        return noun + "s"
    
def count_bull(player_guess: str, generated_number: str) -> int:
    """
    Returns how many guessed numbers are correctly guessed with the correct placement.
    """
    bull = 0
    for i in range(0, len(generated_number)):
        if player_guess[i] == generated_number[i]:
            bull = bull + 1
    return bull

def count_cow(player_guess: str, generated_number: str) -> int:
    """
    Returns how many guessed numbers are guessed correctly but in the wrong location
    """
    cow = 0
    for i in range(0, len(generated_number)):
        if (player_guess[i] != generated_number[i]) and (player_guess[i] in generated_number):
            cow = cow + 1
    return cow

def guess_time(start_time: datetime, end_time: datetime) -> str:
    """
    Duration from the start of an activity to its end - returns the time in minutes and seconds
    """
    total_seconds = (end_time - start_time).total_seconds()
    minutes = int(total_seconds / 60)
    seconds = int(total_seconds % 60)
    return minutes, seconds

if __name__ == "__main__":    

    game_number = 1
    statistics = {}
    while True:
        introductory_text = """Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
Enter a number:
"""

        generated_number = number_generator(4)
        print(edit_introductory_text(introductory_text))
        number_of_dashes = count_characters_longest_line(introductory_text)
        player_guess = input(">>> ")

        start_time = datetime.now()

        while verify_player_input(player_guess, len(generated_number)) != "OK":
            print(f"{"-" * number_of_dashes}")
            player_guess = input(">>> ")

        # I want to count only relevant "correctly" entered inputs in the attempts, I will ignore incorrectly entered inputs.
        number_of_guess = 1
    
        while player_guess != generated_number:
            number_of_guess = number_of_guess + 1
            bull = count_bull(player_guess, generated_number)
            regural_plural_bull = singular_or_plural(bull, "bull")
            cow = count_cow(player_guess, generated_number)
            regural_plural_cow = singular_or_plural(cow, "cow")
            print(f"{bull} {regural_plural_bull}, {cow} {regural_plural_cow}")
            print(f"{"-" * number_of_dashes}")
            player_guess = input(">>> ")
            while verify_player_input(player_guess, len(generated_number)) != "OK":
                print(f"{"-" * number_of_dashes}")
                player_guess = input(">>> ")
        else:
            end_time = datetime.now()
            print("Correct, you've guessed the right number\nin " + str(number_of_guess) + " guesses!")
            print(f"{"-" * number_of_dashes}")
            print("That's amazing!")
            minutes, seconds = guess_time(start_time, end_time)
            print(f"Guess time: {minutes} min {seconds} s")
            print(f"{"-" * number_of_dashes}")
            statistics[game_number] = number_of_guess
        game_number = game_number + 1
        print(f"""Game statistics - game number: number of guess
{statistics}""")
        print(f"{"-" * number_of_dashes}")
        print(f"{"-" * number_of_dashes}")