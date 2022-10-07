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

print(" Lets Play Adventure! ")


def commute():
    pass


def roommate_brush():
    initial_answer = input("Brush your teeth? Enter 'Yes' or 'No' ").lower()
    if initial_answer == "yes":
        return [brush, commute()]
    elif initial_answer == "no":
        return [no_brush_lecture, commute()]


def no_roommate_brush():
    initial_answer = input("Floss and brush your teeth? Enter 'Yes' or 'No' ")
    if initial_answer == "yes":
        return [floss_brush, commute()]
    elif initial_answer == "no":
        return [no_brush, commute()]


def breakfast():
    initial_answer = input("You walk into 'Quick', 'Leave', 'Long' ").lower()
    if initial_answer == "quick":
        answer = input("'banana', 'poptart', 'oatmeal', 'toast': ")
        if answer == "banana":
            return [banana_poptart_oatmeal, roommate_brush()]
        elif answer == "poptart":
            return [banana_poptart_oatmeal, roommate_brush()]
        elif answer == "oatmeal":
            return [banana_poptart_oatmeal, roommate_brush()]
        elif answer == "toast":
            print("*Insert story about burnt toast here*")
            return [toast, roommate_brush()]
    elif initial_answer == "leave":
        print("You decided to skip breakfast and head straight to your interview!")
        return [sprinkler_went_off, commute()]
    elif initial_answer == "long":
        answer = input(
            "Since you saved so much time, you decided to make a nice breakfast. What will you eat? 'Bacon & Eggs', 'Pancakes', 'French Toast?':  "
        ).lower()
        if initial_answer == "Bacon & Eggs":
            print("Oh no! There was a grease fire. Now you got to put it out!")
            return [bacon_eggs, no_roommate_brush()]
        elif initial_answer == "Pancakes":
            return [pancakes_french_toast, no_roommate_brush()]
        elif initial_answer == "French Toast":
            return [pancakes_french_toast, no_roommate_brush()]


def shower():
    initial_answer = input(
        " You walk into the bathroom, smell your armpit and almost choke at the stench! You can either: \n a) Take a detailed shower cleaning every nook and cranny. \n b) Take a quick shower and get to the next task.")
    if initial_answer == "a":  # Detail shower
        answer = input(
            "While wasking your face, you do think you feel a little scruffy. Would you like to shave? \n 'Yes' or 'No': ").lower()
        if answer == "yes":
            return [shave, breakfast()]
        elif answer == "no":
            breakfast()
    elif initial_answer == "b":  # Quick shower
        qs_answer = input(
            "You finish taking you shower and turn the water off. Do oyu want to dry off inside or outside the shower? \n a) Inside \n b) Outside")
        if qs_answer == "b":  # Outside
            print("As you are stepping out, you didn't realize there was no mat on the floor. Your wet feet slip on the floor, and you smack your head on the edge of the tub! You wake up some time later with a massive headache.")
            return [(time + 45), breakfast()]
        elif qs_answer == "a":  # Inside
            print("As you're toweling off, you realize you need to throw some towels in the wash before you leave the house. You run to the laundry room and throw some towels in.")
            return [(time + 20), breakfast()]


def cod():
    initial_answer = input(
        "You decide to play COD but you end the game in a loss. Do you: \n a) Quit and move onto getting ready? \n b) Run it back to redeem yourself?")
    if initial_answer == "b":  # Run it back to redeem yourself?
        answer = input("You just couldn't end on a loss, 4 games later here you are. Got to get to the interview! Will you: \n a) Go to the kitchen to eat breakfast? \n b) Take a shower?  ")
        if answer == "a":  # Go to the kitchen to eat breakfast?
            return [(cod_play_again), breakfast()]
        elif answer == "b":  # Take a shower?
            return [(cod_play_again), shower()]
    if initial_answer == "a":  # Quit and move onto getting ready?
        answer = input("You decide to play just one game and be responsible and get ready for your interview! Will you: \n a) Go to the kitchen to eat breakfast? \n b) Take a shower?  ")
        if answer == "a":  # Go to the kitchen to eat breakfast?
            return [(cod_quit), breakfast()]
        elif answer == "b":  # Take a shower?
            return [(cod_quit), shower()]


def wake_up():
    print('Your alarm goes off at 6:30AM. You can either?  \n a) Hit the snooze button \n b) Hop out of bed.')
    answer = input('Choose A or B').lower()
    if answer == 'a':  # Hit the snooze button
        print('You slept through the snooze and glance at the time. It is now 7:35! You quickly get up and decide what to do. \n a) Run to the kitchen to get some breakfast? \n b) Run to the bathroom to take a shower?')
        answer = input('Choose A or B').lower()
        if answer == 'a':  # Run to the kitchen to get some breakfast?
            return [(snooze), breakfast()]
        elif answer == 'b':  # Run to the bathroom to take a shower?
            return [(snooze), shower()]
    elif answer == 'b':  # Hop out of bed
        print('You excitedly roll out of bed eager to get going. You think about what you should do and what you want to do. \n a) Run to the bathroom to take a shower? \n b) Rush to your gaming room to play a quick game of the new Call of Duty that you just downloaded.')
        answer = input('Choose A or B').lower()
        if answer == 'a':  # Run to the bathroom to take a shower?
            return shower()
        elif answer == 'b':  # Run to play COD?
            return cod()


def adventure_game():
    print('You have a big job interview at ABC Company tomorrow at 10:00, with person. You went to bed early to make sure to make it there on time. (Be careful of the choices you make. Everything you choose will determine when you make it there).')
    start_game = input('Ready to play? Enter Yes or No.  ').lower()
    if start_game == "yes":
        return wake_up()
    else:
        print("Have a nice day!")
