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
