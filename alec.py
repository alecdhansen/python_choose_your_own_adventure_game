from colorama import Style, Fore, Back, init


def alec():
    Play = True

    def you_got_the_job():
        print()
        print(Fore.CYAN + "<>" * 73)
        print()
        print(Fore.GREEN + "<>" * 73)
        print(Fore.GREEN + "<>" * 73)
        return print(
            "\n NICE! You got the job! Congrats! Those 12 weeks of code school paid off.\n\n\n\n\n\n"
        )

    def dejected_walk_of_shame():
        print()
        print(Fore.CYAN + "<>" * 73)
        print()
        print(Fore.RED + "<>" * 73)
        print(Fore.RED + "<>" * 73)
        return print(
            "\n You can't believe this has happened. You really wanted this job, but you've come to realize coding must not be your thing. \n You head out the door into the rain and dejectedly walk home.\n\n\n\n\n\n"
        )

    def brick_question():
        print()
        print(Fore.CYAN + "<>" * 73)
        print(
            Fore.LIGHTYELLOW_EX
            + "\n You've made it to the final question. This might be the most important question you'll ever answer.\n"
        )
        print(
            """                 ________________________________________
                 |        |          |        |         |
                 |________|__________|________|_________|
                 |   |         |         |         |    |
                 |___|_________|_________|_________|____|
                 |       |          |         |         |
                 |_______|__________|_________|_________|"""
        )
        print(
            Fore.LIGHTYELLOW_EX
            + "\n See that brick wall? Which brick would you be, and why?\n"
        )
        initial_answer = input(
            "     a) A brick on the top, so I can see the whole world! \n     b) A brick on the bottom, so I could hold my team on my shoulders \n     c) A brick right in the middle, so I can be right in the action. I love teamwork!\n\n     Choose  A, B, C or enter your own answer!  "
        ).lower()
        if initial_answer == "a":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n Interesting answer! I like that. You're hired!"
            )
            return you_got_the_job()
        elif initial_answer == "b":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n You really can't let people walk all over you in life and be on top of you all the time. \n You're not the kind of person we want working here going forward."
            )
            return dejected_walk_of_shame()
        elif initial_answer == "c":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n Life isn't always about teamwork. Sometimes you need to learn to complete tasks all on your own. \n You can't always rely on others. I'm sorry, but this job isn't the right fit for you."
            )
            return dejected_walk_of_shame()
        elif initial_answer == "hatebricks":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n Wow! I hate bricks too! This is increcible! \n I'm going to love working with you. In fact, let's start you out at $100,000/month. \n Does that sound good? Great!"
            )
            return you_got_the_job()

    def super_hard_math_question():
        print()
        print(Fore.CYAN + "<>" * 73)
        print("\n Alec shuffles his papers and prepares his next question.\n")
        print(
            Fore.LIGHTYELLOW_EX
            + "   If a hen and a half lay an egg and a half in a day and a half, \n   how many eggs will half a dozen hens lay in half a dozen days?\n"
        )
        print(
            Fore.GREEN
            + " You're stunned, but are determined to get this right. Do you answer"
        )
        initial_answer = input(
            "\n     a) 1 dozen \n     b) 2 dozen \n     c) 3 dozen \n     d) A hen doesn't lay eggs!\n\n     Choose  A, B, C or D:  "
        ).lower()
        if initial_answer == "a":
            print(Fore.LIGHTYELLOW_EX + "\n Nope. Wrong. Not even close.")
            return brick_question()
        elif initial_answer == "b":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n That's correct! Wow you are VERY smart. I'll keep this in mind."
            )
            return brick_question()
        elif initial_answer == "c":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n That's incorrect. It doesn't even make sense for you to continue on at this point. \n Please leave the interview now."
            )
            return dejected_walk_of_shame()
        elif initial_answer == "d":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n Look, that's completely false. Remember the acronym 'AGHLE'. All good hens lay eggs. \n I like how you think outside of the box, though!"
            )
            return brick_question()

    def downstairs():
        print()
        print(Fore.CYAN + "<>" * 73)
        print(
            Fore.GREEN
            + "\n\n You made it downstairs. It's dark and quiet down here. \n In your haste to get down here you can't remember \n why you even came down to begin with. Do you:\n"
        )
        initial_answer = input(
            "     a) Sprint straight back up stairs as fast as you can \n     b) Head down the dark hallway toward a door to a room with a light on \n     c) Ask the fella walking by about his time here at the company\n\n     Choose  A, B or C:  "
        ).lower()
        if initial_answer == "a":
            print(
                Fore.GREEN
                    + "\n Okay great, back to the interview. Let's hope Alec doesn't notice you forgot why you came downstairs."
            )
            return super_hard_math_question()
        elif initial_answer == "b":
            print()
            print(Fore.CYAN + "<>" * 73)
            print(
                Fore.GREEN
                    + "\n Alright. Keep heading down the hall. Surely nothing bad could be behind this door, right? Do you:"
            )
            answer = input(
                "\n     a) Knock on the door \n     b) Try and look undernearth \n     c) Head straight in\n\n     Choose -  A, B, or C:  "
            ).lower()
            if answer == "a":
                print(
                    Fore.GREEN
                    + "\n *KNOCK KNOCK KNOCK* You wait... and don't hear anything. \n At this point you've been gone awhile and are starting to get a little spooked. Let's head back upstairs."
                )
                return super_hard_math_question()
            elif answer == "b":
                print()
                print(Fore.CYAN + "<>" * 73)
                print(
                    Fore.GREEN
                    + "\n You get down on all fours, peak underneath and *BOOM*. \n The door opens in your face. You take a second to collect yourself. \n Surely your nose is broken. There's no way you can carry on with the interview now"
                )
                return dejected_walk_of_shame()
            elif answer == "c":
                print(
                    Fore.GREEN
                    + "\n  You've just entered the room. You see a piece of paper on a table with the words \n", Fore.LIGHTCYAN_EX
                    + "   TELL THEM THAT YOU 'hatebricks' WHEN THEY ASK YOU ABOUT BRICKS!\n      This is VERY important.\n"
                )
                return super_hard_math_question()
        elif initial_answer == "c":
            print()
            print(Fore.CYAN + "<>" * 73)
            print(
                Fore.GREEN
                + "\n The guys name is Roger. 'Rog' for short. He's worked here for only 2 years and hardly knows anything about coding, but makes $100,000/month. \n He tells you that he got the job because of one very important piece of info."
            )
            print(
                Fore.GREEN
                + "\n Of course you want to know what this information might be. Do you:\n"
            )
            answer = input(
                "     a) Simply ask him what the info is \n     b) Pull out a $100 bill and offer it to him for the info \n     c) Get down on your knees and beg\n\n     Choose  A, B or C:  "
            ).lower()
            if answer == "a":
                print()
                print(Fore.RED + "<>" * 73)
                print("\n Rog yells at you...")
                print(
                    Fore.LIGHTRED_EX + "\n You think I would just give that info away??"
                )
                print(
                    "\n This isn't good. Rog punches you in the face so hard your nose breaks. \n There's no way you can complete this interview now.\n"
                )
                return dejected_walk_of_shame()
            elif answer == "b":
                print("\n  'Now we're talking' He says. 'TELL THEM THAT YOU 'hatebricks' WHEN THEY ASK YOU ABOUT BRICKS!'", Fore.GREEN + "\n   You thank him and head back upstairs!\n")
                return super_hard_math_question()
            elif answer == "c":
                print(
                    "\n  'Excellent. I was hoping you'd beg.' He said. 'Here's the secret: TELL THEM THAT YOU 'hatebricks' WHEN THEY ASK YOU ABOUT BRICKS! \n   This is VERY important."
                )
                print(Fore.GREEN + "\n   You thank him and head back upstairs!\n")
                return super_hard_math_question()

    def egg_question():
        print()
        print(Fore.CYAN + "<>" * 73)
        print(Fore.LIGHTYELLOW_EX + "\n\n First question! How do you like your eggs?\n")
        initial_answer = input(
            "     a) Scrambled \n     b) Fried \n     c) Raw\n\n     Choose  A, B or C:  "
        ).lower()
        if initial_answer == "a":
            print()
            print(Fore.CYAN + "<>" * 73)
            print()
            print(
                Fore.LIGHTYELLOW_EX
                + "\n Scrambled! Of course! So you're saying you like to conform to the rest of the population and there's nothing special about you?\n Do you at least put ketchup on your eggs? \n "
            )
            answer = input("     Enter -  Yes or No  ").lower()
            if answer == "yes":
                print(
                    Fore.LIGHTYELLOW_EX
                    + "\n Hmm, noted. That is disgusting! You really should rethink your egg dressing choices. \n In fact, that is making me quite nauseous thinking about it. \n Run downstairs and grab me a water bottle out of the vending machine."
                )
                return downstairs()
            elif answer == "no":
                print(
                    Fore.LIGHTYELLOW_EX
                    + "\n Okay good. I really can't get along with people who do that!"
                )
                return super_hard_math_question()
        elif initial_answer == "b":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n Fried huh? I like that. A good fried egg takes a little bit of skill. \n Do you leave them runny or cook them up good?\n"
            )
            answer = input(
                "     a) I like them wet \n     b) Gotta cook them up!\n\n     Choose  A or B:  "
            )
            if answer == "a":
                print(
                    Fore.LIGHTYELLOW_EX
                    + "\n Ah! A true artisan! Let me write that down. This is very impressive."
                )
                return super_hard_math_question()
            elif answer == "b":
                print(
                    Fore.LIGHTYELLOW_EX
                    + "\n OK, interesting. Not my cup of tea...but to each his own."
                )
                return super_hard_math_question()
        elif initial_answer == "c":
            print(
                Fore.LIGHTYELLOW_EX
                + "\n That's a little freaky. In fact, that is making me quite nauseous thinking about it. \n Run downstairs and grab me a bottle or water out of the vending machine."
            )
            return downstairs()

    while Play == True:
        egg_question()
        break


if __name__ == "__main__":
    alec()
