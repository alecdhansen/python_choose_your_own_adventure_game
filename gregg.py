from colorama import Style, Fore, Back, init


class Gregg:
    def __init__(self):
        pass

    def you_got_the_job(self):
        print()
        print(Fore.CYAN + "<>" * 73)
        print()
        print(Fore.GREEN + "<>" * 73)
        print(Fore.GREEN + "<>" * 73)
        print(
            "\n Time to get to work. Code school was a long 12 weeks. You're just happy to start making money!\n\n\n\n\n\n"
        )
        print("""\n
 __  __     ______     __  __        ______     ______     ______        __  __     __     ______     ______     _____    
/\ \_\ \   /\  __ \   /\ \/\ \      /\  __ \   /\  == \   /\  ___\      /\ \_\ \   /\ \   /\  == \   /\  ___\   /\  __-.  
\ \____ \  \ \ \/\ \  \ \ \_\ \     \ \  __ \  \ \  __<   \ \  __\      \ \  __ \  \ \ \  \ \  __<   \ \  __\   \ \ \/\ \ 
 \/\_____\  \ \_____\  \ \_____\     \ \_\ \_\  \ \_\ \_\  \ \_____\     \ \_\ \_\  \ \_\  \ \_\ \_\  \ \_____\  \ \____- 
  \/_____/   \/_____/   \/_____/      \/_/\/_/   \/_/ /_/   \/_____/      \/_/\/_/   \/_/   \/_/ /_/   \/_____/   \/____/ 
                                                                                                                          \n\n\n""")

    def dejected_walk_of_shame(self):
        print()
        print(Fore.CYAN + "<>" * 73)
        print()
        print(Fore.RED + "<>" * 73)
        print(Fore.RED + "<>" * 73)
        print(
            "\n This all happend so fast. You can't believe you didn't get the job. Is there even any hope for me? \n\n\n\n\n\n"
        )
        print("""\n 
 __   __     ______             __     ______     ______           ______     ______   ______   ______     ______    
/\ "-.\ \   /\  __ \           /\ \   /\  __ \   /\  == \         /\  __ \   /\  ___\ /\  ___\ /\  ___\   /\  == \   
\ \ \-.  \  \ \ \/\ \         _\_\ \  \ \ \/\ \  \ \  __<         \ \ \/\ \  \ \  __\ \ \  __\ \ \  __\   \ \  __<   
 \ \_\\  "\_\  \ \_____\       /\_____\  \ \_____\  \ \_____\        \ \_____\  \ \_\    \ \_\    \ \_____\  \ \_\ \_\ 
  \/_/ \/_/   \/_____/       \/_____/   \/_____/   \/_____/         \/_____/   \/_/     \/_/     \/_____/   \/_/ /_/ 
                                                                                                                    \n\n\n""")

    def sandwich_question(self):
        print()
        print(Fore.CYAN + "<>" * 73)
        print(
            Fore.LIGHTYELLOW_EX
            + "\n You've made it to the last question of the morning!. Are you ready?\n What does the perfect sandwich look like? \n"
        )
        initial_answer = input(
            "     a) Bread, lettuce, tofu, cinnamon, cilantro, then a peppered tomato. \n     b) PBNJNONN (Peanut Butter n Jelly n Oreo n Nutella) \n     c) A hot dog! \n\n     Choose  A, B, C or enter your own answer!  "
        ).lower()
        if initial_answer == "a":
            print()
            print(Fore.CYAN + "<>" * 73)
            print(
                Fore.LIGHTYELLOW_EX
                + "\n    Interesting answer! I like that. You're hired!...as our new chef!"
            )
            return self.you_got_the_job()
        elif initial_answer == "b":
            print()
            print(Fore.CYAN + "<>" * 73)
            print(
                Fore.LIGHTYELLOW_EX
                + "\n    That's amazing and sounds incredible? How would you like to start out as a senior dev on your first day? You're hired! "
            )
            return self.you_got_the_job()
        elif initial_answer == "c":
            print()
            print(Fore.CYAN + "<>" * 73)
            print(
                Fore.LIGHTYELLOW_EX
                + "\n    I won't even entertain the idea of a hot dog being a sandwich. Get a job somewhere else you loser!"
            )
            return self.dejected_walk_of_shame()
        elif initial_answer != "a" or "b" or "c":
            print()
            print(Fore.CYAN + "<>" * 73)
            print(
                Fore.LIGHTYELLOW_EX
                + "\n    I have never heard of that sandwich before!",
                Fore.LIGHTRED_EX + "    You know where the door is.",
            )
            return self.dejected_walk_of_shame()

    def star_trek_or_star_wars(self):
        print()
        print(Fore.CYAN + "<>" * 73)
        print(
            Fore.GREEN
            + "\nGregg looks at you and smiles. This is his favorite part of the interview process.\n"
        )
        print(
            Fore.LIGHTYELLOW_EX
            + "   You ready? OK. Next question. Star Trek, or Star Wars? \n"
        )
        print(
            Fore.GREEN
            + "This was definitely an unexpected question but you feel very prepared for this moment."
        )
        initial_answer = input(
            "\n     a) Star Trek, because I want to live long and prosper just like Spock. \n     b) Star Trek, because I don't like sand. It's coarse and rough and irritating and it gets everywhere. \n     c) Star Wars, because of Baby Yoda \n     d) Star Wars, because blasters > phasers \n\n     Choose  A, B, C or D:  "
        ).lower()
        if initial_answer == "a":
            print()
            print(Fore.CYAN + "<>" * 73)
            print(
                Fore.LIGHTGREEN_EX
                + "\n    Gregg likes this answer. Gregg has always vibed with Spock too."
            )
            return self.sandwich_question()
        elif initial_answer == "b":
            print()
            print(Fore.CYAN + "<>" * 73)
            print(
                Fore.LIGHTYELLOW_EX
                + "\n\n    You'll fit right in here. We don't ever let our employees take vacation. \n    You'll never have to see the beach again!\n"
            )
            return self.sandwich_question()
        elif initial_answer == "c":
            print()
            print(Fore.CYAN + "<>" * 73)
            print(
                Fore.LIGHTYELLOW_EX
                + "\n    You're such a bandwagon Star Wars fan! You can't just like someone because they're cute! \n    You need to leave immediately.\n",
                Fore.LIGHTRED_EX + "   You're fired from this interview!",
            )
            return self.dejected_walk_of_shame()
        elif initial_answer == "d":
            print()
            print(Fore.CYAN + "<>" * 73)
            print(
                Fore.LIGHTYELLOW_EX
                + "\n\n    Yes I agree with you here. There's something satisfying in yelling, 'blast 'em!'. \n    I do this daily when debugging my code.\n"
            )
            return self.sandwich_question()

    def type_some_code(self):
        print()
        print(Fore.CYAN + "<>" * 73)
        print(
            Fore.LIGHTYELLOW_EX
            + "\n Alright let's get our hands dirty. Let's open up my terminal on this nice company computer.",
            "\n\n     Do you:\n",
        )
        initial_answer = input(
            "     a) Panic because you definitely have forgotten how to open the terminal \n     b) Command + spacebar + 'terminal' that bad boy in no time at all \n     c) Shakily stumble over a few keys and accidently type 'Turtle'\n\n     Choose  A, B or C:  "
        ).lower()
        if initial_answer == "a":
            print()
            print(Fore.CYAN + "<>" * 73)
            print(
                Fore.LIGHTGREEN_EX
                + "\n  Gregg looks at you and smiles like a grandmother to her grandchild, and says.",
                Fore.LIGHTYELLOW_EX
                + " 'Bless your heart.' \n  You really have no idea what you're doing, do you? We can skip this portion of the interview.",
            )
            return self.star_trek_or_star_wars()
        elif initial_answer == "b":
            print()
            print(Fore.CYAN + "<>" * 73)
            print(
                Fore.LIGHTYELLOW_EX
                + "\n Okay speedy! Create a directory for me to keep files of our past Coronavirus policies."
            )
            answer = input(
                "\n     a) You type 'mkdir covid_19_policies' \n     b) You type 'mkdirn virus --all' \n     c) You panic and realize the only thing you know how to do on a computer is open the terminl. \n\n     Choose  A, B or C:  "
            ).lower()
            if answer == "a":
                print()
                print(Fore.CYAN + "<>" * 73)
                print(
                    Fore.LIGHTYELLOW_EX
                    + "\n   Wow great! You killed this! You'll do very well here."
                )
                return self.star_trek_or_star_wars()
            elif answer == "b":
                print()
                print(Fore.CYAN + "<>" * 73)
                print()
                print(Fore.RED + "<>" * 73)
                print(Fore.RED + "<>" * 73)
                print(
                    Fore.LIGHTRED_EX
                    + "\n    The computer begins to smoke. The screen flashes red, then green, then it turns blue. \n    It's nothing but blue. One big blue screen of death. \n    You've downloaded a virus so terrible it's completely wiped out the entire company. \n    Really Important Company ceases to exist because of you. \n    You hang your head and without even looking at Gregg, somberly walk out."
                )
                print()
                print(Fore.RED + "<>" * 73)
                print(Fore.RED + "<>" * 73)
                return self.dejected_walk_of_shame()
            elif answer == "c":
                print()
                print(Fore.CYAN + "<>" * 73)
                print(
                    Fore.LIGHTGREEN_EX
                    + "\n    Gregg sees right through you. He knew you were a fraud all along. \n    There's still a chance at this job, but you better be perfect from here on out."
                )
                return self.star_trek_or_star_wars()
        elif initial_answer == "c":
            print()
            print(Fore.CYAN + "<>" * 73)
            print(
                Fore.LIGHTGREEN_EX
                + "\n Gregg looks stunned. He can't believe his eyes.",
                Fore.LIGHTYELLOW_EX
                + "Did you just invent a new programming language? What is this?",
            )
            print(
                Fore.LIGHTGREEN_EX
                + "\n Of course 'Turtle' is not really a programming language nor did you actually just invent it. Do you:\n"
            )
            answer = input(
                "     a) Tell Gregg you like to write Turtle code in your spare time \n     b) Scold Gregg for his inability to write complex code in Turtle \n     c) Keep typing on the keyboard random Turtle-related words\n\n     Choose  A, B or C:  "
            ).lower()
            if answer == "a":
                print()
                print(Fore.CYAN + "<>" * 73)
                print(
                    Fore.LIGHTGREEN_EX
                    + "\n\n Gregg is impressed! He tells you the company is thinking of an overhaul and Turtle just might be what they're looking for.\n"
                )
                return self.star_trek_or_star_wars()
            elif answer == "b":
                print()
                print(Fore.CYAN + "<>" * 73)
                print(
                    Fore.LIGHTRED_EX
                    + "\n    You've made Gregg cry. Oh uh. This is not good. Gregg quietly asks you to leave and to never come back. \n"
                )
                print(
                    Fore.LIGHTRED_EX + "    Dang it! Why'd you have to be so mean? \n"
                )
                return self.dejected_walk_of_shame()
            elif answer == "c":
                print()
                print(Fore.CYAN + "<>" * 73)
                print(
                    "\n\n"
                    + Fore.LIGHTGREEN_EX
                    + "    Gregg can't believe his eyes. This language is incredibly fast! I love Turtle! \n    You smile to yourself and pretend like everything that's just happened is totally normal.\n"
                )
                return self.star_trek_or_star_wars()

    def falsy_values(self):
        print()
        print(Fore.CYAN + "<>" * 73)
        print(
            Fore.LIGHTYELLOW_EX
            + "\n\n Well I appreciate you getting here early! We love early birds around here! \n Let's get started. Which of the following is not a falsy value in JavaScript? \n "
        )
        initial_answer = input(
            "     a) False \n     b) NaM \n     c) An empty string \n\n     Choose  A, B or C:  "
        ).lower()
        if initial_answer == "a":
            print()
            print(Fore.CYAN + "<>" * 73)
            print(
                Fore.LIGHTYELLOW_EX
                + "\n\n Look pal, that's not right. These are basic concepts I'd expect you to know. I'll let you redeem yourself.",
                Fore.LIGHTYELLOW_EX
                + "\n How much wood could a woodchuck chuck if a woodchuck could chuck wood?",
                Fore.GREEN + "\n          < You start laughing >",
                Fore.LIGHTYELLOW_EX + "\n Do you think this is a silly question? \n",
            )
            answer = input("     Enter -  Yes or No  ").lower()
            if answer == "yes":
                print()
                print(Fore.CYAN + "<>" * 73)
                print(
                    Fore.RED
                    + "\n           Sometimes the silliest questions are the most enlightening. Never forget this!"
                )
                return self.type_some_code()
            elif answer == "no":
                print()
                print(Fore.CYAN + "<>" * 73)
                print(
                    Fore.LIGHTYELLOW_EX
                    + "\n\n Good, cause I agree. Woodchucks are serious creatures and so am I!\n"
                )
                return self.star_trek_or_star_wars()
        elif initial_answer == "b":
            print()
            print(Fore.CYAN + "<>" * 73)
            print(
                Fore.LIGHTYELLOW_EX
                + "\n You guessed it! Nicely done. I appreciate someone who gives attention to detail. I'm impressed! \n Are you enjoying this interview so far? \n "
            )
            answer = input(
                "     a) I'm having a blast! \n     b) It is what is it. \n\n     Choose  A or B:  "
            )
            if answer == "a":
                print()
                print(Fore.CYAN + "<>" * 73)
                print(
                    Fore.LIGHTYELLOW_EX
                    + "\n\n  Okay listen, no need to pretend. I can spot a liar a mile away. \n"
                )
                return self.type_some_code()
            elif answer == "b":
                print()
                print(Fore.CYAN + "<>" * 73)
                print(Fore.LIGHTYELLOW_EX + "\n\n  I appreciate the honesty... \n")
                return self.star_trek_or_star_wars()
        elif initial_answer == "c":
            print()
            print(Fore.CYAN + "<>" * 73)
            print(
                Fore.LIGHTYELLOW_EX
                + "\n\n  Nice! You're an idiot! That's incorrect. Look, I'm glad you got here early for this interview but you need to step it up.\n"
            )
            return self.type_some_code()
