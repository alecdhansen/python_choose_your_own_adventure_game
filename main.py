from colorama import Style, Fore, Back, init
from random import choice
from alec import alec
from corey import corey
from gregg import gregg
from jonathan import jonathan

init(autoreset=True)

time = 0
detail = time + 30
quick_shower = time + 10
snooze = time + 60
answer = ""
qs_answer = ""
cod_play_again = time + 80  # if we play multiple games
cod_quit = time + 15  # if we only play one game
initial_answer = ""
shave = time + 15
brush = time + 5
no_brush_lecture = time + 15
floss_brush = time + 10
no_brush = time + 0
banana_poptart_oatmeal = time + 5
toast = time + 30
bacon_eggs = time + 30
pancakes_french_toast = time + 20
sprinkler_went_off = time + 90
hunger = 0
hygiene = 0
name = ""
get_in = time + 45
another_uber = time + 25
missed_stop = time + 45
stand = time + 30
ride_bike = time + 45
walk_to_bus_stop = time + 10
play = True
missed_stop = time + 45

# class Player():
#     def __init__(self, name,  hunger, hygiene):
#         self.name = name
#         self.hunger = hunger
#         self.hygiene = hygiene


# class Game():
#     super().__init__(name,  hunger, hygiene)


def interview():
    print("we are at the interview!!!")
    interviewers = ["alec", "corey", "gregg"]
    interviewer = choice(interviewers)
    print(interviewer)
    if interviewer == "alec":
        return alec()
    elif interviewer == "corey":
        return corey()
    elif interviewer == "gregg":
        return gregg()
    elif interviewer == "jonathan":
        return jonathan()


def bike():
    print(time)
    print(Fore.GREEN + "Wow you're healthy! You show up to the interview (a little sweaty)")
    return [ride_bike, interview()]


def bus():
    print(time)
    initial_answer = input(
        Fore.GREEN + "You hop on the bus! Do you want to sit down and relax your puppies or stand up near the front? Enter 'sit' or 'stand' "
    ).lower()
    if initial_answer == "sit":
        print(
            Fore.GREEN + "Oh no! You got too comfy and missed your stop. Now you have to get off and walk 2 blocks back up the street!"
        )
        return [walk_to_bus_stop, missed_stop, interview()]
    elif initial_answer == "stand":
        print(
            Fore.GREEN + "The ride was a little shaky but you held on and finally made it to your interview!"
        )
        return [walk_to_bus_stop, stand, interview()]


def uber():
    print()
    print(Fore.BLUE + "<>" * 45)
    print(Fore.GREEN + "Uh oh! You accidently hit uber pool! Do you want to \n a) Still get in \n b) Order another Uber \n c) Hop on your bike \n d) Head to the bus stop.  "
    ).lower()
    answer = input("\n Choose A, B, C or D:  ").lower()
    if answer == "a":
        return [get_in, interview()]
    elif answer == "b":
        return [another_uber, interview()]
    elif answer == "c":
        return bike()
    elif answer == "d":
        return bus()


def commute():
    print()
    print(Fore.BLUE + "<>" * 45)
    print(
        Fore.GREEN + "Now its time to head to the interview! How are you going to get there? \n a) Uber \n b) Bike \n c) Bus "
    )
    initial_answer = input("\n Choose A, B, or C:  ").lower()
    if initial_answer == "a":
        return uber()
    elif initial_answer == "b":
        return bike()
    elif initial_answer == "c":
        return bus()


def roommate_brush():
    print()
    print(Fore.BLUE + "<>" * 45)
    initial_answer = input("Brush your teeth? Enter 'Yes' or 'No' ").lower()
    if initial_answer == "yes":
        return [brush, commute()]
    elif initial_answer == "no":
        return [no_brush_lecture, commute()]


def no_roommate_brush():
    print()
    print(Fore.BLUE + "<>" * 45)
    initial_answer = input("Floss and brush your teeth? Enter 'Yes' or 'No' ").lower()
    if initial_answer == "yes":
        return [floss_brush, commute()]
    elif initial_answer == "no":
        return [no_brush, commute()]


def breakfast():
    print()
    print(Fore.BLUE + "<>" * 45)
    print(
        Fore.GREEN + "\n You walk into the kitchen. Your tummy growls and feels like it is twisting around. You need to decide if you're going to eat. \n a) Grab something quick? \n b) Just leave the house now? \n c) Make a nice big breakfast? "
    )
    initial_answer = input("\n Choose A, B or C  ").lower()
    if initial_answer == "a":  # Grab something quick?
        print()
        print(Fore.BLUE + "<>" * 45)
        print(
            Fore.GREEN + "\n You open up the cabinet to see what choices you have. \n a) There is one ripe yellow banana left. \n b) You see a box of strawberry poptarts. \n c) Brown sugar and cinnamon oatmeal. \n d) There is a couple slices of bread left to make toast.  "
        )
        answer = input("\n Choose A, B, C or D:  ").lower()
        if answer == "a":  # banana
            return [banana_poptart_oatmeal, roommate_brush()]
        elif answer == "b":  # poptart
            return [banana_poptart_oatmeal, roommate_brush()]
        elif answer == "c":  # oatmeal
            return [banana_poptart_oatmeal, roommate_brush()]
        elif answer == "d":  # toast
            print()
            print(Fore.BLUE + "<>" * 45)
            print(
                Fore.GREEN + "\n You start smelling something really bad while you are waiting for your toast to pop. All of a sudden the toaster catches on fire!! \n Fortunately you have a fire extinguisher under the sink to put it out. One last thing before you leave.  \n"
            )
            return [toast, roommate_brush()]
    elif initial_answer == "b":  # Just leave the house now?
        print()
        print(Fore.BLUE + "<>" * 45)
        print(Fore.GREEN + "\n You decided to skip breakfast and head straight to your interview!")
        return [sprinkler_went_off, commute()]
    elif initial_answer == "c":  # Make a nice big breakfast?
        print()
        print(Fore.BLUE + "<>" * 45)
        print(
            Fore.GREEN + "\n You decided to make a nice breakfast before you head to the interview. What will you eat? \n a) The american classic bacon and eggs? \n b) The standard pancakes and butter? \n c) Your ultimate favorite, french toast! "
        )
        answer = input("\n Choose A, B or C  ").lower()
        if answer == "a":  # Bacon & Eggs
            print()
            print(Fore.BLUE + "<>" * 45)
            print(
                Fore.GREEN + "\n Oh no! There was a grease fire. \n Fortunately you have a fire extinguisher under the sink to put it out. One last thing before you leave.  \n"
            )
            return [bacon_eggs, no_roommate_brush()]
        elif answer == "b":  # Pancakes
            return [pancakes_french_toast, no_roommate_brush()]
        elif answer == "c":  # French Toast?
            return [pancakes_french_toast, no_roommate_brush()]


def shower():
    initial_answer = input(
        Fore.GREEN + " You walk into the bathroom, smell your armpit and almost choke at the stench! You can either: \n a) Take a detailed shower cleaning every nook and cranny. \n b) Take a quick shower and get to the next task."
    )
    if initial_answer == "a":  # Detail shower
        answer = input(
            Fore.GREEN + "While wasking your face, you do think you feel a little scruffy. Would you like to shave? \n 'Yes' or 'No': "
        ).lower()
        if answer == "yes":
            return [shave, breakfast()]
        elif answer == "no":
            breakfast()
    elif initial_answer == "b":  # Quick shower
        qs_answer = input(
            Fore.GREEN + "You finish taking you shower and turn the water off. Do oyu want to dry off inside or outside the shower? \n a) Inside \n b) Outside"
        )
        if qs_answer == "b":  # Outside
            print(
                Fore.GREEN + "As you are stepping out, you didn't realize there was no mat on the floor. Your wet feet slip on the floor, and you smack your head on the edge of the tub! You wake up some time later with a massive headache."
            )
            return [(time + 45), breakfast()]
        elif qs_answer == "a":  # Inside
            print(
                Fore.GREEN + "As you're toweling off, you realize you need to throw some towels in the wash before you leave the house. You run to the laundry room and throw some towels in."
            )
            return [(time + 20), breakfast()]


def cod():
    initial_answer = input(
        Fore.GREEN + "You decide to play COD but you end the game in a loss. Do you: \n a) Quit and move onto getting ready? \n b) Run it back to redeem yourself?"
    ).lower()
    if initial_answer == "b":  # Run it back to redeem yourself?
        answer = input(
            Fore.GREEN + "You just couldn't end on a loss, 4 games later here you are. Got to get to the interview! Will you: \n a) Go to the kitchen to eat breakfast? \n b) Take a shower?  "
        ).lower()
        if answer == "a":  # Go to the kitchen to eat breakfast?
            return [(cod_play_again), breakfast()]
        elif answer == "b":  # Take a shower?
            return [(cod_play_again), shower()]
    if initial_answer == "a":  # Quit and move onto getting ready?
        answer = input(
            Fore.GREEN + "You decide to play just one game and be responsible and get ready for your interview! Will you: \n a) Go to the kitchen to eat breakfast? \n b) Take a shower?  "
        ).lower()
        if answer == "a":  # Go to the kitchen to eat breakfast?
            return [(cod_quit), breakfast()]
        elif answer == "b":  # Take a shower?
            return [(cod_quit), shower()]


def wake_up():
    print()
    print(Fore.BLUE + "<>" * 45)
    print(
        Fore.GREEN + "\n Your alarm goes off at 6:30AM. You can either?  \n a) Hit the snooze button \n b) Hop out of bed."
    )
    answer = input("\n Choose A or B:  ").lower()
    if answer == "a":  # Hit the snooze button
        print()
        print(Fore.BLUE + "<>" * 45)
        print(
            Fore.GREEN + "\n You slept through the snooze and glance at the time. It is now 7:35! You quickly get up and decide what to do. \n a) Run to the kitchen to get some breakfast? \n b) Run to the bathroom to take a shower?"
        )
        answer = input("\n Choose A or B  ").lower()
        if answer == "a":  # Run to the kitchen to get some breakfast?
            return [breakfast()]
        elif answer == "b":  # Run to the bathroom to take a shower?
            return [shower()]
    elif answer == "b":  # Hop out of bed
        print()
        print(Fore.BLUE + "<>" * 45)
        print(
            Fore.GREEN + "\n You excitedly roll out of bed eager to get going. You think about what you should do and what you want to do. \n a) Run to the bathroom to take a shower? \n b) Rush to your gaming room to play a quick game of the new Call of Duty that you just downloaded."
        )
        answer = input("\n Choose A or B  ").lower()
        if answer == "a":  # Run to the bathroom to take a shower?
            return shower()
        elif answer == "b":  # Run to play COD?
            return cod()


def adventure_game():
    print("\n ")
    print(Fore.BLUE + "<>" * 45)
    print(Fore.BLUE + "<>" * 45)
    print("\n Lets Play Adventure! \n ")
    print(Fore.BLUE + "<>" * 45)
    print(Fore.BLUE + "<>" * 45)
    print(
        "\nYou have a big job interview at Really Important Company tomorrow at 10:00, with Jonathan. \n You went to bed early to make sure to make it there on time. Be careful of the choices you make. \n (Everything you choose will determine when you make it there).\n"
    )
    start_game = input("Ready to play? Enter Yes or No.  ").lower()
    # if start_game != "yes" or "i":
    if start_game == "yes":
        return wake_up()
    elif start_game == "i":
        return interview()  # add shortcut to interview!
    elif start_game == "no":
        print("Have a nice day!")
    elif start_game != "yes" or "i" or "no":
        print("That aint right!")
        return adventure_game()


while play == True:
    adventure_game()
    break
