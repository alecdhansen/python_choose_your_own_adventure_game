from colorama import Style, Fore, Back, init
from datetime import datetime, timedelta
from alec import Alec
from corey import Corey
from gregg import Gregg
from jonathan import Jonathan
import time

init(autoreset=True)

times = datetime(2022, 10, 10, 6, 30, 0)
answer = ""
qs_answer = ""
initial_answer = ""
hunger = 0
hygiene = 0
name = ""
play = True


# Interview Functions
def play_alec():
    alec = Alec()
    return alec.egg_question()


def play_corey():
    corey = Corey()
    return corey.penguin_question()


def play_gregg():
    gregg = Gregg()
    return gregg.falsy_values()


def play_jonathan():
    jonathan = Jonathan()
    return jonathan.cooked_steak()


# Time Functions
def detail():
    global times
    times += timedelta(minutes=30)


def quick_shower():
    global times
    times += timedelta(minutes=10)


def snooze():
    global times
    times += timedelta(minutes=60)


def play_cod():
    global times
    times += timedelta(minutes=20)


def cod_play_again():  # if we play multiple games
    global times
    times += timedelta(minutes=80)


def shave():
    global times
    times += timedelta(minutes=15)


def brush():
    global times
    times += timedelta(minutes=5)


def no_brush_lecture():
    global times
    times += timedelta(minutes=15)


def floss_brush():
    global times
    times += timedelta(minutes=10)


def no_brush():
    global times
    times += timedelta(minutes=0)


def banana_poptart_oatmeal():
    global times
    times += timedelta(minutes=5)


def toast():
    global times
    times += timedelta(minutes=30)


def bacon_eggs():
    global times
    times += timedelta(minutes=30)


def pancakes_french_toast():
    global times
    times += timedelta(minutes=20)


def sprinkler_went_off():
    global times
    times += timedelta(minutes=90)


def get_in():
    global times
    times += timedelta(minutes=45)


def another_uber():
    global times
    times += timedelta(minutes=25)


def missed_stop():
    global times
    times += timedelta(minutes=45)


def stand():
    global times
    times += timedelta(minutes=30)


def ride_bike():
    global times
    times += timedelta(minutes=45)


def walk_to_bus_stop():
    global times
    times += timedelta(minutes=10)


def missed_stop():
    global times
    times += timedelta(minutes=45)


def dry_inside():
    global times
    times += timedelta(minutes=20)


def dry_outside():
    global times
    times += timedelta(minutes=45)


class Interview:
    def interview():
        print()
        print(Fore.BLUE + "<>" * 73)
        print(Fore.BLUE + "<>" * 73)
        print(Fore.BLUE + "<>" * 73)
        print()
        print("\n    Current Time: ", times.time(), "AM")
        print(
            Fore.LIGHTCYAN_EX
            + "\n   We finally made it Really Important Company. Time for the interview!!!"
        )
        print()
        if times < datetime(2022, 10, 10, 8, 29, 0):
            print(
                "\n     Wow, you're early! Good thing Gregg is also an early bird. \n     Instead of Jonathan interviewing you today, Gregg is going to step in"
            )
            return play_gregg()
        elif times >= datetime(2022, 10, 10, 8, 30, 0) and times < datetime(
            2022, 10, 10, 9, 00, 0
        ):
            print(
                "\n     Nice! You've arrived a tad early. Jonathan isn't here yet so you'll be interviewing with Corey today. \n     Watch out though! He will ask some random questions"
            )
            return play_corey()
        elif times >= datetime(2022, 10, 10, 9, 00, 0) and times < datetime(
            2022, 10, 10, 9, 30, 0
        ):
            print(
                "\n     You made it! Jonathan has been expecting you. Head on inside!"
            )
            return play_jonathan()
        elif times >= datetime(2022, 10, 10, 9, 30, 0):
            print(
                "\n     Wow you're late. This is not good. Jonathan couldn't wait any longer and he's gone. \n     Thankfully Alec is here and he can step in and interview you even though YOU'RE VERY LATE."
            )
            return play_alec()


def bike():
    print()
    print(Fore.BLUE + "<>" * 73)
    print()
    print(
        Fore.GREEN
        + "Wow you're healthy! You show up to the interview (a little sweaty)"
    )
    return [ride_bike(), Interview.interview()]


def bus():
    print()
    print(Fore.BLUE + "<>" * 73)
    print()
    print(
        Fore.GREEN
        + "\n  You hop on the bus! Do you want to:\n \n    a) Sit down and relax your puppies? \n    b) Stand up near the front?  "
    )
    walk_to_bus_stop()
    print("\n    Current Time: ", times.time(), "AM")
    initial_answer = input("\n  Choose -  A or B:  ").lower()
    if initial_answer == "a":
        print()
        print(Fore.BLUE + "<>" * 73)
        print(Fore.RED + "<>" * 73)
        print(Fore.RED + "<>" * 73)
        print(
            Fore.LIGHTRED_EX
            + "\n      Oh no! You got too comfy and missed your stop. Now you have to get off and walk 2 blocks back to Really Important Company! \n"
        )
        print(Fore.RED + "<>" * 73)
        print(Fore.RED + "<>" * 73)
        return [missed_stop(), Interview.interview()]
    elif initial_answer == "b":
        print(
            Fore.GREEN
            + "The ride was a little shaky but you held on and finally made it to your interview!"
        )
        return [stand(), Interview.interview()]


def uber():
    print()
    print(Fore.BLUE + "<>" * 73)
    print()
    print(
        Fore.GREEN
        + "\n  WTF! You accidently hit uber pool! There are already two other passengers in the car. Do you want to:\n \n a) Still get in \n b) Order another Uber \n c) Hop on your bike \n d) Head to the bus stop.  "
    )
    print("\n    Current Time: ", times.time(), "AM")
    answer = input("\n  Choose  A, B, C or D:  ").lower()
    if answer == "a":
        return [get_in(), Interview.interview()]
    elif answer == "b":
        return [another_uber(), Interview.interview()]
    elif answer == "c":
        return bike()
    elif answer == "d":
        return bus()
    else:
        return uber()


def commute():
    print()
    print(Fore.BLUE + "<>" * 73)
    print()
    print(
        Fore.GREEN
        + "\n  You have to head to the interview! How are you going to get there?\n \n    a) Uber \n    b) Bike \n    c) Bus "
    )
    print("\n    Current Time: ", times.time(), "AM")
    initial_answer = input("\n  Choose  A, B, or C:  ").lower()
    if initial_answer == "a":
        return uber()
    elif initial_answer == "b":
        return bike()
    elif initial_answer == "c":
        return bus()
    else:
        return commute()


def roommate_brush():
    print()
    print(Fore.BLUE + "<>" * 73)
    print()
    print(
        Fore.GREEN
        + "\n  Ew, your mouth feels a little grungy. Do you want to brush your teeth? "
    )
    print("\n    Current Time: ", times.time(), "AM")
    initial_answer = input("\n     Enter - Yes or No:   ").lower()
    if initial_answer == "yes":
        return [brush(), commute()]
    elif initial_answer == "no":
        print()
        print(Fore.BLUE + "<>" * 73)
        print()
        print(Fore.RED + "<>" * 73)
        print(Fore.RED + "<>" * 73)
        print(
            Fore.LIGHTRED_EX
            + "\n     You decided to skip breakfast and head straight to your interview. However, your roommate stopped you because they noticed you didn't \n        brush your teeth. They are a dental hygienists and proceeds to explain to you how importnant it is to take care of your teeth! \n                   They will not let you leave the house without performing a proper teeth cleaning! \n"
        )
        no_brush_lecture()
        print(Fore.RED + "<>" * 73)
        print(Fore.RED + "<>" * 73)
        return commute()
    else:
        return roommate_brush()


def no_roommate_brush():
    print()
    print(Fore.BLUE + "<>" * 73)
    print()
    print(
        Fore.GREEN
        + "\n  Ew, your mouth feels a little grungy. Do you want to brush and floss your teeth? "
    )
    print("\n    Current Time: ", times.time(), "AM")
    initial_answer = input("\n     Enter - Yes or No:   ").lower()
    if initial_answer == "yes":
        return [floss_brush(), commute()]
    elif initial_answer == "no":
        return [no_brush(), commute()]
    else:
        return no_roommate_brush()


def breakfast():
    print()
    print(Fore.BLUE + "<>" * 73)
    print()
    print(
        Fore.GREEN
        + "\n  You walk into the kitchen. Your tummy growls and feels like it is twisting around. You need to decide if you're going to eat. Do you: \n \n    a) Grab something quick? \n    b) Just leave the house now? \n    c) Make a nice big breakfast? "
    )
    print("\n    Current Time: ", times.time(), "AM")
    initial_answer = input("\n  Choose  A, B or C:  ").lower()
    if initial_answer == "a":  # Grab something quick?
        print()
        print(Fore.BLUE + "<>" * 73)
        print()
        print(
            Fore.GREEN
            + "\n  You open up the cabinet to see what choices you have.\n \n    a) There is one ripe yellow banana left. \n    b) You see a box of strawberry poptarts. \n    c) Brown sugar and cinnamon oatmeal. \n    d) There is a couple slices of bread left to make toast.  "
        )
        print("\n    Current Time: ", times.time(), "AM")
        answer = input("\n  Choose  A, B, C or D:  ").lower()
        if answer == "a":  # banana
            return [banana_poptart_oatmeal(), roommate_brush()]
        elif answer == "b":  # poptart
            return [banana_poptart_oatmeal(), roommate_brush()]
        elif answer == "c":  # oatmeal
            return [banana_poptart_oatmeal(), roommate_brush()]
        elif answer == "d":  # toast
            print()
            print(Fore.BLUE + "<>" * 73)
            print()
            print(Fore.RED + "<>" * 73)
            print(Fore.RED + "<>" * 73)
            print(
                Fore.RED
                + "\n              You start smelling something really bad while you are waiting for your toast to pop. \n                                 All of a sudden the toaster catches on fire!! \n    Fortunately you have a fire extinguisher under the sink to put it out. One last thing before you leave.  \n"
            )
            print(Fore.RED + "<>" * 73)
            print(Fore.RED + "<>" * 73)
            return [toast(), roommate_brush()]
    elif initial_answer == "b":  # Just leave the house now?
        print()
        print(Fore.BLUE + "<>" * 73)
        print()
        print(Fore.RED + "<>" * 73)
        print(Fore.RED + "<>" * 73)
        print(
            Fore.RED
            + "\n         You decided to skip breakfast and head straight to your interview! Unfortunately on your way out the sprinklers turned on! \n                         YOU GOT SOAKED. You panic, rush back inside, and change. This is going to take a lot of time... \n                       Everything must be perfect! You clean off in the shower and throw you dirty clothes in the laundry. \n                                            Time is really ticking by! This isn't good..."
        )
        print()
        print(Fore.RED + "<>" * 73)
        print(Fore.RED + "<>" * 73)
        sprinkler_went_off()
        print("\n    Current Time: ", times.time(), "AM")
        return commute()
    elif initial_answer == "c":  # Make a nice big breakfast?
        print()
        print(Fore.BLUE + "<>" * 73)
        print()
        print(
            Fore.GREEN
            + "\n  Great! A home-cooked breakfast is just what you need before a tough interview. What will you eat?\n \n    a) The American classic: bacon and eggs \n    b) The standard pancakes, syrup, and butter. YUM! \n    c) Your ultimate favorite, french toast! "
        )
        print("\n    Current Time: ", times.time(), "AM")
        answer = input("\n  Choose  A, B or C:  ").lower()
        if answer == "a":  # Bacon & Eggs
            print()
            print(Fore.BLUE + "<>" * 73)
            print()
            print(Fore.RED + "<>" * 73)
            print(Fore.RED + "<>" * 73)
            print(
                Fore.RED
                + "\n                        Oh no!! There was a grease fire. \n     Fortunately you have a fire extinguisher under the sink to put it out.\n                        One last thing before you leave.  \n"
            )
            print()
            print(Fore.RED + "<>" * 73)
            print(Fore.RED + "<>" * 73)
            return [bacon_eggs(), no_roommate_brush()]
        elif answer == "b":  # Pancakes
            return [pancakes_french_toast(), no_roommate_brush()]
        elif answer == "c":  # French Toast?
            return [pancakes_french_toast(), no_roommate_brush()]


def shower():
    print()
    print(Fore.BLUE + "<>" * 73)
    print()
    print(
        Fore.GREEN
        + "\n You walk into the bathroom, smell your armpit and almost faint at the stench! You can either:\n \n    a) Take a detailed shower cleaning every nook and cranny \n    b) Take a quick shower and get to the next task"
    )
    print("\n    Current Time: ", times.time(), "AM")
    initial_answer = input("\n Choose -  A or B:  ").lower()
    if initial_answer == "a":  # Detail shower
        print()
        print(Fore.BLUE + "<>" * 73)
        print()
        print(
            Fore.GREEN
            + "\n  While washing your face, you notice it feels a little scruffy. Would you like to shave?"
        )
        detail()
        print("\n    Current Time: ", times.time(), "AM")
        answer = input("\n  Enter -  Yes or No:  ").lower()
        if answer == "yes":
            return [shave(), breakfast()]
        elif answer == "no":
            breakfast()
    elif initial_answer == "b":  # Quick shower
        print()
        print(Fore.BLUE + "<>" * 73)
        print()
        print(
            Fore.GREEN
            + "\n You finish taking you shower and turn the water off. Do you want to dry off inside or outside the shower?\n \n    a) Inside \n    b) Outside"
        )
        quick_shower()
        print("\n    Current Time: ", times.time(), "AM")
        qs_answer = input("\n Choose -  A or B:  ").lower()
        if qs_answer == "a":  # Inside
            print()
            print(Fore.BLUE + "<>" * 73)
            print()
            print(
                Fore.YELLOW
                + "\n             As you're toweling off, you realize you need to throw some towels in the wash before\n                 you leave the house. You run to the laundry room and throw some towels in."
            )
            print()
            return [dry_inside(), breakfast()]
        elif qs_answer == "b":  # Outside
            print()
            print(Fore.BLUE + "<>" * 73)
            print()
            print(Fore.RED + "<>" * 73)
            print(Fore.RED + "<>" * 73)
            print(
                Fore.LIGHTRED_EX
                + "\n       As you are stepping out, you didn't realize there was no mat on the floor. Your wet feet slip on the floor, \n          and you smack your head on the edge of the tub! You wake up some time later with a massive headache."
            )
            print()
            print(Fore.RED + "<>" * 73)
            print(Fore.RED + "<>" * 73)
            return [dry_outside(), breakfast()]


def cod():
    print()
    print(Fore.BLUE + "<>" * 73)
    print()
    print(
        Fore.GREEN
        + "\n  You decide to play COD but you end the first game in a loss. Do you:\n \n    a) Quit and move onto getting ready? \n    b) Run it back to redeem yourself?"
    )
    play_cod()
    print("\n    Current Time: ", times.time(), "AM")
    initial_answer = input("\n  Choose -  A or B:  ").lower()
    if initial_answer == "a":  # Quit and move onto getting ready?
        print()
        print(Fore.BLUE + "<>" * 73)
        print()
        print(
            Fore.GREEN
            + "  You decided to play just one game and be responsible and get ready for your interview! Will you:\n \n    a) Go to the kitchen to eat breakfast? \n    b) Take a shower?  "
        )
        print("\n    Current Time: ", times.time(), "AM")
        answer = input("\n  Choose -  A or B:  ").lower()
        if answer == "a":  # Go to the kitchen to eat breakfast?
            return breakfast()
        elif answer == "b":  # Take a shower?
            return shower()
    elif initial_answer == "b":  # Run it back to redeem yourself?
        print()
        print(Fore.BLUE + "<>" * 73)
        print()
        print(
            Fore.GREEN
            + "\n  You just couldn't end on a loss, 4 games later here you are. Got to get to the interview! Will you:\n \n    a) Go to the kitchen to eat breakfast? \n    b) Take a shower?"
        )
        cod_play_again()
        print("\n    Current Time: ", times.time(), "AM")
        answer = input("\n  Choose -  A or B:  ").lower()
        if answer == "a":  # Go to the kitchen to eat breakfast?
            return breakfast()
        elif answer == "b":  # Take a shower?
            return shower()
    else:
        return cod()


def wake_up():
    print()
    print(Fore.BLUE + "<>" * 73)
    print()
    print(
        Fore.GREEN
        + "\n  Your alarm goes off at 6:30AM. You can either: \n  \n    a) Hit the snooze button \n    b) Hop out of bed"
    )
    print("\n    Current Time: ", times.time(), "AM")

    answer = input("\n  Choose -  A or B:  ").lower()
    if not answer in ("a", "b"):
        return wake_up()
    elif answer == "a":  # Hit the snooze button
        print()
        print(Fore.BLUE + "<>" * 73)
        print()
        print(
            Fore.GREEN
            + "\n  You slept through the snooze and glance at the time. It is now 7:30! You quickly get up and decide what to do.\n \n    a) Run to the kitchen to get some breakfast? \n    b) Run to the bathroom to take a shower?"
        )
        snooze()
        print("\n    Current Time: ", times.time(), "AM")
        answer = input("\n  Choose -  A or B:  ").lower()
        if answer == "a":  # Run to the kitchen to get some breakfast?
            return breakfast()
        elif answer == "b":  # Run to the bathroom to take a shower?
            return shower()
    elif answer == "b":  # Hop out of bed
        print()
        print(Fore.BLUE + "<>" * 73)
        print()
        print(
            Fore.GREEN
            + "\n  You excitedly roll out of bed eager to get going. You think about what you should do and what you want to do.\n \n    a) Run to the bathroom to take a shower? \n    b) Rush to your gaming room to play a quick game of the new Call of Duty that you just downloaded."
        )
        print("\n    Current Time: ", times.time(), "AM")
        answer = input("\n  Choose -  A or B:  ").lower()
        if answer == "a":  # Run to the bathroom to take a shower?
            return shower()
        elif answer == "b":  # Run to play COD?
            return cod()


def adventure_game():
    print("\n ")
    print(Fore.BLUE + "<>" * 73)
    print(Fore.BLUE + "<>" * 73)
    print(
        """\n 
 
 ______     _____     __   __   ______     __   __     ______   __  __     ______     ______        ______     ______     __    __     ______    
/\  __ \   /\  __-.  /\ \ / /  /\  ___\   /\ "-.\ \   /\__  _\ /\ \/\ \   /\  == \   /\  ___\      /\  ___\   /\  __ \   /\ "-./  \   /\  ___\   
\ \  __ \  \ \ \/\ \ \ \ \'/   \ \  __\   \ \ \-.  \  \/_/\ \/ \ \ \_\ \  \ \  __<   \ \  __\      \ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\   
 \ \_\ \_\  \ \____-  \ \__|    \ \_____\  \ \_\\"\_\    \ \_\  \ \_____\  \ \_\ \_\  \ \_____\     \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\ 
  \/_/\/_/   \/____/   \/_/      \/_____/   \/_/ \/_/     \/_/   \/_____/   \/_/ /_/   \/_____/      \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/ 
                                                                                                                                                 

 \n """
    )
    print(Fore.BLUE + "<>" * 73)
    print(Fore.BLUE + "<>" * 73)
    print(
        Fore.YELLOW
        + "\n***                        You have a big job interview at Really Important Company tomorrow at 9:30AM with Jonathan.                          ***\n***                     You went to bed early to make sure that you get there on time. Be careful of the choices you make.                     ***\n***                                     (Everything you choose will determine when you make it there).                                         ***\n"
    )
    time.sleep(6)
    start_game = input("  Ready to play? \n  Enter -  Yes or No:  ").lower()
    if start_game == "yes":
        return wake_up()
    elif start_game == "alec":  # Interview shortcut to Alec
        return play_alec()
    elif start_game == "corey":  # Interview shortcut to Corey
        return play_corey()
    elif start_game == "gregg":  # Interview shortcut to Gregg
        return play_gregg()
    elif start_game == "jonathan":  # Interview shortcut to Jonathan
        return play_jonathan()
    elif start_game == "no":
        print("Have a nice day!")
    else:
        print("That aint right!")
        return adventure_game()


while play == True:
    adventure_game()
    break
