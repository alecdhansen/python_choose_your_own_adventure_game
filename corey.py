from colorama import Style, Fore, Back, init


class Corey:
    def you_got_the_job(self):
        print()
        print(Fore.CYAN + "<>" * 73)
        print()
        print(Fore.GREEN + "<>" * 73)
        print(Fore.GREEN + "<>" * 73)
        print(
            Fore.LIGHTYELLOW_EX
            + "\n        Congrats! You got the job! Now its time to call all of your friends and celebrate!"
        )
        print("""\n
 __  __     ______     __  __        ______     ______     ______        __  __     __     ______     ______     _____    
/\ \_\ \   /\  __ \   /\ \/\ \      /\  __ \   /\  == \   /\  ___\      /\ \_\ \   /\ \   /\  == \   /\  ___\   /\  __-.  
\ \____ \  \ \ \/\ \  \ \ \_\ \     \ \  __ \  \ \  __<   \ \  __\      \ \  __ \  \ \ \  \ \  __<   \ \  __\   \ \ \/\ \ 
 \/\_____\  \ \_____\  \ \_____\     \ \_\ \_\  \ \_\ \_\  \ \_____\     \ \_\ \_\  \ \_\  \ \_\ \_\  \ \_____\  \ \____- 
  \/_____/   \/_____/   \/_____/      \/_/\/_/   \/_/ /_/   \/_____/      \/_/\/_/   \/_/   \/_/ /_/   \/_____/   \/____/ 
                                                                                                                          \n\n\n""")

    def ur_fired(self):
        print()
        print(Fore.CYAN + "<>" * 73)
        print()
        print(Fore.RED + "<>" * 73)
        print(Fore.RED + "<>" * 73)
        print(
            Fore.LIGHTYELLOW_EX
            + "\n        You did not get the job. You walk away feeling sad"
        )
        print("""\n 
 __   __     ______             __     ______     ______           ______     ______   ______   ______     ______    
/\ "-.\ \   /\  __ \           /\ \   /\  __ \   /\  == \         /\  __ \   /\  ___\ /\  ___\ /\  ___\   /\  == \   
\ \ \-.  \  \ \ \/\ \         _\_\ \  \ \ \/\ \  \ \  __<         \ \ \/\ \  \ \  __\ \ \  __\ \ \  __\   \ \  __<   
 \ \_\\ "\_\  \ \_____\       /\_____\  \ \_____\  \ \_____\        \ \_____\  \ \_\    \ \_\    \ \_____\  \ \_\ \_\ 
  \/_/ \/_/   \/_____/       \/_____/   \/_____/   \/_____/         \/_____/   \/_/     \/_/     \/_____/   \/_/ /_/ 
                                                                                                                    \n\n\n""")

    def final_question(self):
        print()
        print(Fore.CYAN + "<>" * 73)
        print(Fore.LIGHTYELLOW_EX + "\n\n Alright final question. Green or Blue?\n")
        answer = input("     a) Green \n     b) Blue\n\n     Choose -  A or B:  ")
        if answer == "a":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n My Mom's third-cousin's uncle's nephew's son does not like the color green. So we're not hiring you!"
            )
            return self.ur_fired()
        elif answer == "b":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n Thats my favorite color! We might have a potential new employee."
            )
            return self.you_got_the_job()

    def pool_question(self):
        print()
        print(Fore.CYAN + "<>" * 73)
        print(
            Fore.LIGHTYELLOW_EX
            + "\n\n Fourth question, its getting crazy! If a tiger did a triple-twisted-backflip into a pool, what would you rate it? \n"
        )
        answer = input(
            "     a) What?! Im definetely rating that a 10  \n     b) Why would a tiger do that\n\n     Choose -  A or B:  "
        )
        if answer == "a":
            print(
                Fore.LIGHTYELLOW_EX + "\n See thats what Im saying! That'll be crazy!"
            )
            return self.final_question()
        elif answer == "b":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n You lack imagination and creativity! That is something you need to have to work at this company!"
            )
            return self.final_question()

    def biscuit_question(self):
        print()
        print(Fore.CYAN + "<>" * 73)
        print(
            Fore.LIGHTYELLOW_EX
            + "\n\n Third question, get ready. What company would you want to be a biscuit from?\n"
        )
        answer = input(
            "     a) Chic-fil-a  \n     b) Popeyes\n\n     Choose -  A or B:  "
        )
        if answer == "a":
            print(Fore.LIGHTYELLOW_EX + "\n Good choice. A biscuit with some quality")
            return self.pool_question()
        elif answer == "b":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n You want to be a dry biscuit?! A dry biscuit means a dry personality and we cannot have that at this company."
            )
            return self.pool_question()

    def video_game_question(self):
        print()
        print(Fore.CYAN + "<>" * 73)
        print(
            Fore.LIGHTYELLOW_EX
            + "\n\n Alright second question: What video games do you play?\n "
        )
        answer = input(
            "     a) Rocket League \n     b) COD \n     c) Dance Dance Revolution  \n     d) Overcooked\n\n     Choose -  A, B, C or D:  "
        )
        if answer == "a":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n Oh you play rocket league?! We just might have to hire you then."
            )
            return self.biscuit_question()
        elif answer == "b":
            print(
                Fore.LIGHTYELLOW_EX + "\n Okay I mess with COD too! Lets run sometime"
            )
            return self.biscuit_question()
        elif answer == "c":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n Huh..Dance Dance Revolution? I had no idea that game still existed"
            )
            return self.biscuit_question()
        elif answer == "d":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n Overcooked goes crazy. Maybe you could be the chef at the company"
            )
            return self.biscuit_question()

    def penguin_question(self):
        print()
        print(Fore.CYAN + "<>" * 73)
        print(
            Fore.LIGHTYELLOW_EX
            + "\n\n Welcome to your interview! What you do if you found a penguin in a freezer? \n "
        )
        answer = input(
            "     a) Close the freezer and act like I never saw it  \n     b) Call the animal shelter and let them figure it out\n\n     Choose -  A or B:  "
        )
        if answer == "a":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n Wow.. So you're not going to do anything for the penguin"
            )
            return self.video_game_question()
        elif answer == "b":
            print(Fore.LIGHTYELLOW_EX + "\n Look at you being a decent human being")
            return self.video_game_question()
