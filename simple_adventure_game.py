###############################
# Simple-adventure game
# author : Lasantha Wijewardhana
# Date   : 04.04.2025

print("Welcome to the Adventure Game!!!!!")

# game start
areplay = input("Are you wanna Play(yes/no)? ").lower()

if areplay != "yes":
    quit()


name = input("Please Enter your name: ")

print("Welcome " + name + " to this adventure!!")

print()

# story
print("You are on a quest to find a legendary artifact hidden deep within the Enchanted Forest. The forest is known for its beauty and danger. As you journey deeper, you come to your first big choice. \n")

# select option
answer = input("You reach a fork in the road. The path to the left leads to Darkwood, a mysterious and shadowy part of the forest. The path to the right is a Sunlit Path, bright and inviting but less traveled. Which way would you like to go?(left/ right) \n ").lower()

# first main option
if answer == "left":

    # select option
    answer = input("You enter Darkwood. The trees grow thicker, and the air feels colder. After a while, you reach a river with a wooden bridge crossing it. Which way would you like to go?(bridge/ swim) \n").lower()

    # option
    if answer == "bridge":

        # select option
        answer = input("You cross the bridge, but it suddenly collapses behind you! You’re stuck on the other side of the river. Up ahead, you see your house in the distance.What will you do?(house/ another) \n").lower()

        # option
        if answer == "house":
            print("You came to the home, and you won!")

        # option
        elif answer == "another":
            print("You took the wrong path and were killed by a bear!!")

        else:
            print("Not valid option, You lose!")

    # option
    elif answer == "swim":
        print("You killed by an aligator!")

    else:
        print("Not valid option, you lose!")


# second main option
elif answer == "right":

    # select option
    answer = input("You follow the Sunlit Path, and after walking for a while, you find a small cottage with smoke coming from the chimney. You Knock on the cottage door. An old woman answers the door and invites you inside. She offers you food and a place to stay for the night. But something feels off about her. What will you do?(accept/ refuse) \n").lower()

    # option
    if answer == "accept":
        print("You killed the old woman!")

    # option
    elif answer == "refuse":
        print("ou ignore the cottage and keep walking. Eventually, you suddenly encounter and kill the snake.")

    else:
        print("Not valid option, You lose!")


else:
    print("Not valid option, You lose!")

# end of the game
print("Thanks " + name + " for playing this game!")
