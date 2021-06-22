import time
import random

# pause after each text message is printed


def print_pause(message):
    print(message)
    time.sleep(1.5)

# Beginning of the game


def start_adventure_game(item, option):
    print_pause("You find yourself standing in an open prairie, filled "
                "with snow.")
    print_pause("People say that the " + option + " is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a barn.")
    print_pause("To your right is a dark hut.")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) knief.\n")

# user input to play the game


def prairie(item, option):
    print_pause("Enter 1 to knock on the door of the barn.")
    print_pause("Enter 2 to peer into the hut.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("Enter number 1 or 2 using your keyboard: ")
        if choice1 == "1":
            barn(item, option)
            break
        elif choice1 == "2":
            hut_choice(item, option)
            break

# troll attacks function


def barn(item, option):
    print_pause("You approach the door of the barn.")
    print_pause("You are about to knock when the door "
                "opens and out steps a " + option + ".")
    print_pause("phew! This is the " + option + "'s barn!")
    print_pause("The " + option + " attacks you!")
    if "knief" not in item:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a small knief.")
    while True:
        choice2 = input("Enter 1 to fight or 2 "
                        "escape from the place?")
        if choice2 == "1":
            if "knief" in item:
                print_pause("As the " + option + " moves to attack, "
                            "you unsheath your new weapon.")
                print_pause("The magic wand shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                print_pause("But the " + option + " takes one look at "
                            "your magic wand and runs away!")
                print_pause("You have rid the town of the " + option +
                            ". You are victorious!")
            else:
                print_pause("You do your best...")
                print_pause("but your knief is no match for the " +
                            option + ".")
                print_pause("You have been defeated!")
            play_again()
            break
        if choice2 == "2":
            print_pause("You run back into the prairie. "
                        "Luckily, you don't seem to have been "
                        "followed.")
            prairie(item, option)
            break

# After selected user input


def hut_choice(item, option):
    if "wand" in item:
        print_pause("You get into the hut cautiously.")
        print_pause("You've been here before, and gotten all"
                    " the good stuff. It's just an empty hut"
                    " now.")
        print_pause("You walk back to the prairie.")
    else:
        print_pause("You peer cautiously into the hut.")
        print_pause("It turns out to be only a very small hut.")
        print_pause("Your eye catches a glint of metal behind a "
                    "rock.")
        print_pause("You have found the magical wand!")
        print_pause("You discard your silly old knief and take "
                    "the wand with you.")
        print_pause("You walk back out to the prairie.")
        item.append("wand")
    prairie(item, option)


# Function for playing the game again


def play_again():
    again = input("\n Wanna play again? (y/n) \n ").lower()
    if again == "y":
        print_pause("\n Lets's start the game again ...\n")
        play_game()
    elif again == "n":
        print_pause("\n Thanks for playing, See you soon!.")
    else:
        play_again()

# Function to play the game


def play_game():
    item = []
    enemies = ["Wicked Queen ", "Pirate ", "Wolves "]
    option = random.choice(enemies)
    start_adventure_game(item, option)
    prairie(item, option)


if __name__ == '__main__':
    play_game()
