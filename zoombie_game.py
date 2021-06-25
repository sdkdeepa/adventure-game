import random

import time


def displayText():
    print("It is the end of a long fighting with"
          "Woodland Zommbies :(^ ^): .")
    print("You come to overpass on your trip home,"
          "one path leads home")
    print("where you can relax and spend time"
          " with your family")
    print("and the other leads through a Zommbies :(^ ^): where "
          "they will not spare you.")
    print()


def selectPath():
    path = ""
    while path != "1" and path != "2":
        path = input("Select a path(1 or 2): ")

    return path


def verifyPath(chosen_Path):
    print("You walk down the path\n")
    time.sleep(2)
    print("There's something nearby that looks familiar, "
          "You think that must be a good sign...\n")
    time.sleep(2)
    print("But you sense something that begins to ...")
    print()
    time.sleep(2)

    correct_Path = random.randint(1, 2)

    if chosen_Path == str(correct_Path):
        print("\nThat was just the feeling of relief "
              "from the chorus from the Chruch!")
        time.sleep(2)
        print("You feel happy.\n")
        time.sleep(2)
        print("Yes, Welcome home!")
    else:
        print("A GIGANTIC Zoombie ::(^ ^):"
              "charges at you.\n")
        time.sleep(2)
        print("You start to run for your "
              "life..... until\n")
        time.sleep(2)
        print("A group of zoombies approach you.")
        time.sleep(2)
        print("You are no more :( ")


def game():
    displayText()
    while True:
        playAgain = input("Do you want to play?(y/n): ")
        if playAgain == "y":
            choice = selectPath()
            verifyPath(choice)
        elif playAgain == "n":
            print("\nCome back soon! \n")
            exit()
        else:
            game()


if __name__ == '__main__':
    game()
