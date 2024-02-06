import time
import random

def print_pause(text):
    print(text)
    time.sleep(1)

def labyrinth(path):
    if len(path)-1 >= 10:
        new_path = "c"
    elif len(path)-1 >= 5 and random.randint(1, 100) <= 25:
        new_path = "c"
    else:
        new_path = random.choice(["d", "d", "b", "b", "y", "y", "t"])
    path.append(new_path)

def n_v_input():
    print_pause("Invalid input.")
    print_pause("Enter only the number of the choice you want.")
    print_pause("Please try again.")

def ending_bad():
    print_pause("The minotaur turned out to be an adversay beyond your abilities.")
    print_pause("Who knows when a noble hero will be able to slay the beast...")
    print_pause("\nBad Ending\n")

def ending_secret():
    print_pause("You have vanquished the monstrous minotaur...")
    print_pause("...but the heroic endevour costed you your life.")
    print_pause("The princess will be saved by someone else...")
    print_pause("...and as they will find your remains intertwined with those of the minotaur...")
    print_pause("...they will thank you for your brave sacrifice!")
    print_pause("\nSecret Bad Ending\n")

def ending_good():
    print_pause("The princess Ariadne rushes to hug you!")
    print_pause("You truly are her hiro!")
    print_pause("Thanks to the magical thread that she gave you...")
    print_pause("...the two of you easily navigate the labyrinth back to the entrance.")
    print_pause("\nGood Ending\n")

def c_d_d_1():
    print_pause("You decide to charge the monster!")
    print_pause("The beast is not intimidated and charges as well.")
    print_pause("As the two of you collide, your sword penetrate deep into the minotaur's skull.")
    print_pause("But it is not enough!")
    print_pause("You are not strong enough to stop the massive body from slamming against you.")
    print_pause("One of the minotaur's massive horns has stabed you through the chest!")
    print_pause("You fall on your back and are crushed by the weigth of the beast's body.")
    print_pause("Your vision fades...")

def c_d_d_2():
    print_pause("You jump to the side!")
    print_pause("Your timing is wrong and you cannot dodge the minotaur's massive horns.")
    print_pause("One of the horns has stabed you through the heart!")
    print_pause("With a powerful flex of its muscular neck, the monster throws you against the wall.")
    print_pause("Your vision fades...")

def c_d_d_3():
    print_pause("You flex you legs and jump as high as you can.")
    print_pause("The minotaur is faster than you expected!")
    print_pause("One of the horns stabs through the lower leg!")
    print_pause("With a powerful flex of its muscular neck, the monster throws you down against the floor.")
    print_pause("Stunned and shocked, you cannot oppose the beast.")
    print_pause("The minotaur dismember you.")
    print_pause("Your vision fades...")

def c_d_d_4():
    print_pause("You brandish your sword with resolute bravery.")
    print_pause("As the minotaur is about to reach you, you swring the blade at his head.")
    print_pause("The sharp metal sever one of the minotaur's horns.")
    print_pause("But it is not enough...")
    print_pause("The other horn stabs you through the heart!")
    print_pause("With a powerful flex of its muscular neck, the monster throws you against the wall.")
    print_pause("Your vision fades...")

def c_d_d_5():
    print_pause("You turn and start running!")
    print_pause("You can hear the monster gaining on you!")
    print_pause("You make a sharp turn into a different corridor.")
    print_pause("The minotaur is not fooled by your quick thinking.")
    print_pause("It catches up with you.")
    print_pause("Both of its massive horns are protruding from your chest.")
    print_pause("With a powerful flex of its muscular neck, the monster throws you against the wall.")
    print_pause("Your vision fades...")

def c_d_v_1():
    print_pause("You flex you legs and jump as high as you can.")
    print_pause("The minotaur is not as fast as you expected!")
    print_pause("At the last moment you manage to grab onto one of its massive horns.")
    print_pause("You land on its broad, muscular back.")
    print_pause("The monster stops its charge.")
    print_pause("But before it can have the time to get you off, you stab your sword though its neck.")
    print_pause("The mighty minotaur is vanquished!")
    print_pause("With an horrid grawl it falls to the ground.")
    print_pause("And you fall with it, still clutching the hilt of your sword.")

def combat_3():
    while True:
        print_pause("You have only a moment to decide what to do, as the minotaur turns to face you.")
        reaction = input("What do you do?\n1. Charge!\n2. Wait of the charge and dodge\n3. Wait of the charge and jump\n4. Wait of the charge and parry\n5. Run\n")
        if reaction == "1":
            c_d_d_1()
            ending_secret()
            break
        elif reaction == "2":
            c_d_d_2()
            ending_bad()
            break
        elif reaction == "3":
            c_d_d_3()
            ending_bad()
            break
        elif reaction == "4":
            c_d_d_4()
            ending_bad()
            break
        elif reaction == "5":
            c_d_d_5()
            ending_bad()
            break
        else:
            n_v_input()

def combat_cont_2(path):
    chance = random.randint(1, 100)
    if chance > 50:
        combat_3()
    else:
        print_pause("But the minotaur has not stopped and disappears in the darkness.")
        print_pause("The ferocious monster is now but an echo of hoofs on stone.")
        labyrinth(path)

def combat_2(path):
    while True:
        print_pause("You have only a moment to decide what to do, as the minotaur turns to face you.")
        reaction = input("What do you do?\n1. Charge!\n2. Wait of the charge and dodge\n3. Wait of the charge and jump\n4. Wait of the charge and parry\n5. Run\n")
        if "c" in path:
            if reaction == "1":
                c_d_d_1()
                ending_secret()
                break
            elif reaction == "2":
                c_d_d_2()
                ending_bad()
                break
            elif reaction == "3":
                c_d_v_1()
                ending_good()
                break
            elif reaction == "4":
                c_d_d_4()
                ending_bad()
                break
            elif reaction == "5":
                c_d_d_5()
                ending_bad()
                break
            else:
                n_v_input()
        else:
            if reaction == "1":
                c_d_d_1()
                ending_secret()
                break
            elif reaction == "2":
                print_pause("You jump to the side!")
                print_pause("Your timing is perfect and you managed to dodge the minotaur's massive horns.")
                print_pause("You pull yourself up and immediatly turn around ready to face the beast!")
                combat_cont_2(path)
                break
            elif reaction == "3":
                print_pause("You flex you legs and jump as high as you can.")
                print_pause("The minotaur rush past under you.")
                print_pause("As soon as you land you immediatly turn around ready to face the beast!")
                combat_cont_2(path)
                break
            elif reaction == "4":
                c_d_d_4()
                ending_bad()
                break
            elif reaction == "5":
                print_pause("You turn and start running!")
                print_pause("You can hear the monster gaining on you!")
                print_pause("You make a sharp turn into a different corridor.")
                print_pause("The sound is now different.")
                print_pause("The minotaur has not follower you.")
                print_pause("The ferocious monster is now but an echo of hoofs on stone.")
                labyrinth(path)
                break
            else:
                n_v_input()

def combat_cont_1(path):
    chance = random.randint(1, 100)
    if chance > 50:
        combat_2(path)
    else:
        print_pause("But the minotaur has not stopped and disappears in the darkness.")
        print_pause("The ferocious monster is now but an echo of hoofs on stone.")
        labyrinth(path)

def combat_1(path):
    print_pause("With a bestial howl the minotaur exits the shadows, horns trained at you, in a savage charge!")
    while True:
        print_pause("You have only a split second to react to the attack of the ferocious beast.")
        reaction = input("What do you do?\n1. Dodge\n2. Jump\n3. Parry\n4. Run\n")
        if "c" in path:
            if reaction == "1":
                print_pause("You jump to the side!")
                print_pause("Your timing is perfect and you managed to dodge the minotaur's massive horns.")
                print_pause("You pull yourself up and immediatly turn around ready to face the beast!")
                combat_2(path)
                break
            elif reaction == "2":
                c_d_v_1()
                ending_good()
                break
            elif reaction == "3":
                c_d_d_4()
                ending_bad()
                break
            elif reaction == "4":
                c_d_d_5()
                ending_bad()
                break
            else:
                n_v_input()
        else:
            if reaction == "1":
                print_pause("You jump to the side!")
                print_pause("Your timing is perfect and you managed to dodge the minotaur's massive horns.")
                print_pause("You pull yourself up and immediatly turn around ready to face the beast!")
                combat_cont_1(path)
                break
            elif reaction == "2":
                print_pause("You flex you legs and jump as high as you can.")
                print_pause("The minotaur rush past under you.")
                print_pause("As soon as you land you immediatly turn around ready to face the beast!")
                combat_cont_1(path)
                break
            elif reaction == "3":
                c_d_d_4()
                ending_bad()
                break
            elif reaction == "4":
                print_pause("You turn and start running!")
                print_pause("You can hear the monster gaining on you!")
                print_pause("You make a sharp turn into a different corridor.")
                print_pause("The sound is now different.")
                print_pause("The minotaur has not follower you.")
                print_pause("The ferocious monster is now but an echo of hoofs on stone.")
                labyrinth(path)
                break
            else:
                n_v_input()

def encounter(path):
    minotaur = random.randint(3, 10)
    if len(path) < 3:
        print_pause("You walk down the corridor undisturbed.")
        labyrinth(path)
    elif minotaur <= len(path):
        print_pause("As you walk down the corridor, a menacing roar stops you in your traks!")
        print_pause("Red glowing eyes are fixed upon you from the darkness in front of you.")
        combat_1(path)
    else:
        print_pause("As you walk down the corridor, an echo startles you.")
        print_pause("The weak sound is that of a feral roar, and hoofs hammering the stone.")
        labyrinth(path)

def go_straight(path):
    print_pause("You choose to continue straight.")
    encounter(path)

def turn_right(path):
    print_pause("You take the path to the right.")
    encounter(path)

def turn_left(path):
    print_pause("You take the path to the left.")
    encounter(path)

def next_d(path):
    print_pause("As you walk, from the shadows something appears.")
    print_pause("It is an archway that opens into a new corridor to your left.")
    while True:
        choice = input("\nWhich direction will you go?\n1: Continue straight\n2: Turn left\n")
        if choice == "1":
            go_straight(path)
            break
        elif choice == "2":
            turn_left(path)
            break
        else:
            n_v_input()

def next_b(path):
    print_pause("As you walk, from the shadows something appears.")
    print_pause("It is an archway that opens into a new corridor to your right.")
    while True:
        choice = input("\nWhich direction will you go?\n1: Continue straight\n2: Turn right\n")
        if choice == "1":
            go_straight(path)
            break
        elif choice == "2":
            turn_right(path)
            break
        else:
            n_v_input()

def next_y(path):
    print_pause("As you walk, from the shadows something appears.")
    print_pause("It is an archway that splits the corridor in half.")
    while True:
        choice = input("\nWhich direction will you go?\n1: Turn right\n2: Turn left\n")
        if choice == "1":
            turn_right(path)
            break
        elif choice == "2":
            turn_left(path)
            break
        else:
            n_v_input()

def next_t(path):
    print_pause("As you walk, from the shadows something appears.")
    print_pause("It is an archway that opens into two new corridors, one to the left and one to the right.")
    while True:
        choice = input("\nWhich direction will you go?\n1: Continue straight\n2: Turn right\n3: Turn left\n")
        if choice == "1":
            go_straight(path)
            break
        elif choice == "2":
            turn_right(path)
            break
        elif choice == "3":
            turn_left(path)
            break
        else:
            n_v_input()

def next_c(path):
    print_pause("After an unexpectedly short corridor, you reach a much bigger archway, and...")
    print_pause("You have finally reached the centre of the labyrinth!")
    print_pause("A cavernous opening extends in front of you...")
    print_pause("The minotaur stands proud between you and the princess.")
    combat_1(path)

def navigate(path):
    while True:
        if path[len(path)-1] == "d":
            next_d(path)
        elif path[len(path)-1] == "b":
            next_b(path)
        elif path[len(path)-1] == "y":
            next_y(path)
        elif path[len(path)-1] == "t":
            next_t(path)
        elif "c" in path:
            next_c(path)
            break
        else:
            next_y(path)

def intro():
    print_pause("\nHeavy iron doors slam behind you as you find yourself alone.")
    print_pause("You are Theseus, son of Poseidon.")
    print_pause("The dark and cold stones that surround you are the walls of the Labyrinth.")
    print_pause("You are here to find Ariadne, the princess, your beloved.")
    print_pause("You move forward, ready to face the labytinth!")
    path = ["t"]
    navigate(path)

def replay():
    print_pause("\nGAME OVER\n")
    print_pause("Thank you for playing!")
    while True:
        regame = input("Would you like to play again?\n1: Yes\n2: No\n")
        if regame == "1":
            print_pause("Great!")
            print_pause("Get ready!")
            intro()
        elif regame == "2":
            print_pause("Bye!")
            break
        else:
            n_v_input()

def adventure_game():
    intro()
    replay()

adventure_game()