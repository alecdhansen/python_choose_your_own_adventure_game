from operator import truediv
from colorama import Style, Fore, Back, init


def jonathan():
    question = True
    print()
    print(Fore.CYAN + "<>" * 73)
    print("\n  Welcome to the questionaire part of your interview. \n" "This will help us get to know you based off a few scenarios.")

    def next_time():
        print()
        print(Fore.CYAN + "<>" * 73)
        print("\n Sorry! Better luck next time!")

    def best_answer():
        print()
        print(Fore.CYAN + "<>" * 73)
        print("Wow, was that really your best answer?")

    def hire_interviewer():
        print()
        print(Fore.CYAN + "<>" * 73)
        print("\n You would be a great fit! Would you consider this job offer?")

    def sink_or_swim():
        print()
        print(Fore.CYAN + "<>" * 73)
        print("\n If you were thrown into the deep end of a 12 foot pool blindfolded, would you sink or would you swim? ")
        initial_answer = input(
            "\n    a) Dude! I can't swim!! I'm definitely going to sink! \n    b) Of course I can swim, I taught Michael Phelps!").lower()
        if initial_answer == "a":
            print(Fore.LIGHTYELLOW_EX +
                  "Hmmm Why are so afraid of the water? I thought everyone knows how to swim!")
            return next_time()
        elif initial_answer == "b":
            print(Fore.LIGHTYELLOW_EX + "Awesome! We love people who enjoy, and are not affraid of the water! Maybe you can join us at at the Water Park on our next company event. ")
            return hire_interviewer

    def plane_crash():
        print()
        print(Fore.CYAN + "<>" * 73)
        print("\n If you were the only survivor from a plane crash that had an emergency landing near a desert island for 14 days what would you do?")
        initial_answer = input(
            "\n a) I'm scared of heights! I'm not boarding the plane, I didn't purchase a ticket! \n b) I keep a extra parachute in my bag, I'm just jumping out, and skydiving the rest of way down! \n c) I'll figure it out once I'm able to get to safe and secure spot.").lower()
        if initial_answer == "a":
            print(
                "C'mon man its 2022, everybody should have taken at least one flight by now!")
            return next_time()
        elif initial_answer == "b":
            print(
                "That's smart! Do you typically go skydiving to readily have that avaliable? ")
            return hire_interviewer
        elif initial_answer == "c":
            print("That doesn't sound like you will survive long with that mindset. Hopefully you have some camping experience!")
            return best_answer()

    def titanic_ship():
        print()
        print(Fore.CYAN + "<>" * 73)
        print("You're on the Titanic and you have enough time grab a few items before you're in freezing cold waters in the middle of the night. What are some of last minute items that you would grab?")
        initial_answer = input(
            "\n a) A water raft, becuase you don't know how to swim. \n b) Joining the voilin players and playing music untill your demise! \n c) I'm broke, I never could afford a ticket to get on!").lower()
        if initial_answer == "a":
            print(
                "Smart Answer! A water raft will more than likely will save the lives of many!")
            return (hire_interviewer)

        if initial_answer == "b":
            print(
                "Hey it is what it is! You have accpeted you fate, and maybe we will see you on the other side.")
            return (next_time)

        if initial_answer == "c":
            print("Well it looks like this is a time where being broke was a benefit! Are you now ready to be employed, and generate a steady income?")
            return (hire_interviewer)

        def cooked_steak():
            print()
            print(Fore.CYAN + "<>" * 73)
            print("How do you like your steak cooked?")
            initial_answer = input(
                "\n a) The best way to have a steak is medium well, \n b) I want to taste the flesh, make mine rare! \n c) EWW! I hate meat, I'm a vegetarian!").lower()
        if initial_answer == "a":
            print("Great answer! I Can tell you have great taste in food!")
            return (hire_interviewer)

        if initial_answer == "b":
            print("OMG! Are you even human! Who eats raw meat like that! ")
            return (next_time)

        if initial_answer == "c":
            print(
                "Oops! Well I hope I didn't offend you, but I love meat! Maybe we can get you a salad! ")
            return (best_answer)

        while question is True:
            jonathan()
            break


if __name__ == "__main__":
    jonathan()
