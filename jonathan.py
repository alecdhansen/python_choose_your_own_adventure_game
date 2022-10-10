from colorama import Style, Fore, Back, init
import time


class Jonathan:
    # print()
    # print(Fore.CYAN + "<>" * 73)
    # print(Fore.CYAN + "<>" * 73)
    # print(
    #     "\n  Welcome to the questionaire part of your interview. \n"
    #     "  This will help us get to know you based off a few scenarios."
    # )

    def next_time(self):
        print()
        print(Fore.CYAN + "<>" * 73)
        print()
        print(Fore.RED + "<>" * 73)
        print(Fore.RED + "<>" * 73)
        print(Fore.LIGHTRED_EX
                + "\n   Sorry! Better luck next time!\n\n")
        print("""\n 
 __   __     ______             __     ______     ______           ______     ______   ______   ______     ______    
/\ "-.\ \   /\  __ \           /\ \   /\  __ \   /\  == \         /\  __ \   /\  ___\ /\  ___\ /\  ___\   /\  == \   
\ \ \-.  \  \ \ \/\ \         _\_\ \  \ \ \/\ \  \ \  __<         \ \ \/\ \  \ \  __\ \ \  __\ \ \  __\   \ \  __<   
 \ \_\\  "\_\  \ \_____\       /\_____\  \ \_____\  \ \_____\        \ \_____\  \ \_\    \ \_\    \ \_____\  \ \_\ \_\ 
  \/_/ \/_/   \/_____/       \/_____/   \/_____/   \/_____/         \/_____/   \/_/     \/_/     \/_____/   \/_/ /_/ 
                                                                                                                    \n\n\n""")


    def best_answer(self):
        time.sleep(2)
        print()
        print(Fore.CYAN + "<>" * 73)
        print()
        print(Fore.RED + "<>" * 73)
        print(Fore.RED + "<>" * 73)
        print(Fore.LIGHTYELLOW_EX
                + "\n   Wow, was that really your best answer?\n\n")
        print("""\n 
 __   __     ______             __     ______     ______           ______     ______   ______   ______     ______    
/\ "-.\ \   /\  __ \           /\ \   /\  __ \   /\  == \         /\  __ \   /\  ___\ /\  ___\ /\  ___\   /\  == \   
\ \ \-.  \  \ \ \/\ \         _\_\ \  \ \ \/\ \  \ \  __<         \ \ \/\ \  \ \  __\ \ \  __\ \ \  __\   \ \  __<   
 \ \_\\ "\_\  \ \_____\       /\_____\  \ \_____\  \ \_____\        \ \_____\  \ \_\    \ \_\    \ \_____\  \ \_\ \_\ 
  \/_/ \/_/   \/_____/       \/_____/   \/_____/   \/_____/         \/_____/   \/_/     \/_/     \/_____/   \/_/ /_/ 
                                                                                                                    \n\n\n""")


    def hire_interviewer(self):
        time.sleep(2)
        print()
        print(Fore.CYAN + "<>" * 73)
        print()
        print(Fore.GREEN + "<>" * 73)
        print(Fore.GREEN + "<>" * 73)
        print(Fore.LIGHTYELLOW_EX
                + "\n   You would be a great fit! Would you consider this job offer?\n\n")
        print("""\n
 __  __     ______     __  __        ______     ______     ______        __  __     __     ______     ______     _____    
/\ \_\ \   /\  __ \   /\ \/\ \      /\  __ \   /\  == \   /\  ___\      /\ \_\ \   /\ \   /\  == \   /\  ___\   /\  __-.  
\ \____ \  \ \ \/\ \  \ \ \_\ \     \ \  __ \  \ \  __<   \ \  __\      \ \  __ \  \ \ \  \ \  __<   \ \  __\   \ \ \/\ \ 
 \/\_____\  \ \_____\  \ \_____\     \ \_\ \_\  \ \_\ \_\  \ \_____\     \ \_\ \_\  \ \_\  \ \_\ \_\  \ \_____\  \ \____- 
  \/_____/   \/_____/   \/_____/      \/_/\/_/   \/_/ /_/   \/_____/      \/_/\/_/   \/_/   \/_/ /_/   \/_____/   \/____/ 
                                                                                                                          \n\n\n""")

    def dead_or_alive(self):
        time.sleep(2)
        print()
        print(Fore.CYAN + "<>" * 73)
        print(
            Fore.LIGHTYELLOW_EX + "\n\n If you could bring back person or pet from the dead, who would it be?\n"
        )
        initial_answer = input("\n     a) A family memeber, I miss them so much! \n     b) Your favorite music artist, becuase music is not the same without them. \n     c) Your favorite pet, you miss having them around.\n\n     Choose  A, B or C:  ").lower()
        if initial_answer == "a":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n Family is forever! You had the chance to bring a love one back, and you did! We value family and you would fit right in! \n"
            )
            return self.hire_interviewer()
        elif initial_answer == "b":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n Music changes daily! You can still listen to your favorite artist without them being alive"
            )
            return self.best_answer()
        elif initial_answer == "c":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n Pets are just like family! We love our fur babies just like our own!"
            )
            return self.hire_interviewer()

    def plane_crash(self):
        time.sleep(2)
        print()
        print(Fore.CYAN + "<>" * 73)
        print(
            Fore.LIGHTYELLOW_EX + "\n\n If you were the only survivor from a plane crash that had an emergency landing near a desert island for 14 days what would you do?"
        )
        initial_answer = input(
            "\n     a) I'm scared of heights! I'm not boarding the plane, I didn't purchase a ticket! \n     b) I keep a extra parachute in my bag, I'm just jumping out, and skydiving the rest of way down! \n     c) I'll figure it out once I'm able to get to safe and secure spot.\n\n     Choose  A, B or C :  "
        ).lower()
        if initial_answer == "a":
            print(
                Fore.LIGHTYELLOW_EX + "\n C'mon man its 2022, everybody should have taken at least one flight by now!"
            )
            return self.dead_or_alive()
        elif initial_answer == "b":
            print(
                Fore.LIGHTYELLOW_EX + "\n That's smart! Do you typically go skydiving to readily have that avaliable? "
            )
            return self.dead_or_alive()
        elif initial_answer == "c":
            print(
                Fore.LIGHTYELLOW_EX + "\n That doesn't sound like you will survive long with that mindset. Hopefully you have some camping experience!"
            )
            return self.dead_or_alive()

    def titanic_ship(self):
        time.sleep(2)
        print()
        print(Fore.CYAN + "<>" * 73)
        print(
            Fore.LIGHTYELLOW_EX + "\n\n You're on the Titanic and you have enough time grab a few items before you're in freezing cold waters in the middle of the night. \n What are some of last minute items that you would grab?"
        )
        initial_answer = input(
            "\n     a) A water raft, becuase you don't know how to swim. \n     b) Joining the voilin players and playing music untill your demise! \n     c) I'm broke, I never could afford a ticket to get on!\n\n     Choose  A, B or C :  "
        ).lower()
        if initial_answer == "a":
            print(
                Fore.LIGHTYELLOW_EX + "\n Smart Answer! A water raft will more than likely will save the lives of many!"
            )
            return self.plane_crash()
        if initial_answer == "b":
            print(
                Fore.LIGHTYELLOW_EX + "\n Hey it is what it is! You have accpeted you fate, and maybe we will see you on the other side."
            )
            return self.plane_crash()

        if initial_answer == "c":
            print(
                Fore.LIGHTYELLOW_EX + "\n Well it looks like this is a time where being broke was a benefit! Are you now ready to be employed, and generate a steady income?"
            )
            return self.plane_crash()

    def cooked_steak(self):
        time.sleep(1)
        print()
        print(Fore.CYAN + "<>" * 73)
        print(
            Fore.LIGHTYELLOW_EX + "\n\n First questions. How do you like your steak cooked?\n\n","    a) The best way to have a steak is medium well, \n     b) I want to taste the flesh, make mine rare! \n     c) EWW! I hate meat, I'm a vegetarian!"
        )
        initial_answer = input("\n     Choose  A, B or C :  ").lower()
        if initial_answer == "a":
            print(Fore.LIGHTYELLOW_EX + "\n  Great answer! I can tell you have great taste in food!")
            return self.titanic_ship()
        elif initial_answer == "b":
            print(Fore.LIGHTYELLOW_EX + "\n  OMG! Are you even human! Who eats raw meat like that! ")
            return self.titanic_ship()
        elif initial_answer == "c":
            print(
                Fore.LIGHTYELLOW_EX + "\n  Oops! Well I hope I didn't offend you, but I love meat! Maybe we can get you a salad! "
            )
            return self.titanic_ship()

    def sink_or_swim(self):
        time.sleep(2)
        print()
        print(Fore.CYAN + "<>" * 73)
        print(
            Fore.LIGHTYELLOW_EX + "\n\n If you were thrown into the deep end of a 12 foot pool blindfolded, would you sink or would you swim? \n","     a) Dude! I can't swim!! I'm definitely going to sink! \n     b) Of course I can swim, I taught Michael Phelps!"
        )
        initial_answer = input("\n  Choose  A or B:  ").lower()
        if initial_answer == "a":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n  Hmmm Why are so afraid of the water? I thought everyone knows how to swim! \n"
            )
            return self.cooked_steak()
        elif initial_answer == "b":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n  Awesome! We love people who enjoy, and are not afraid of the water! Maybe you can join us at at the Water Park on our next company event. "
            )
            return self.cooked_steak()
