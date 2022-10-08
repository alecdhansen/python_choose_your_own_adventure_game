
def next_time():
    print("Sorry! Better luck next time!")


def hire_interviewer():
    print("You would be a great fit! Would you consider this job offer?")


def jonathan():
    print(" Welcome to the intensified questionaire part of your interview. \n" "This will help us identify if you would be a nice fit for our team.")


def sink_or_swim():
    print("If you were thrown into the deep end of a 12 foot pool blindfolded, would you sink or would you swim? ")
    initial_answer = input(
        "\n a) Dude! I can't swim!! I'm definitely going to sink! \n b) Of course I can swim, I taught Michael Phelps!").lower()
    if initial_answer == "a":
        print("Hmmm Why are so afraid of the water? I thought everyone knows how to swim!")
        return next_time()
    elif initial_answer == "b":
        print("Awesome! We love people who enjoy, and are not affraid of the water! Maybe you can join us at at the Water Park on our next company event. ")
        return hire_interviewer


def deserted_island():
    print("If you were standed on a desert island for 7 days what would you do?")


if __name__ == "__main__":
    jonathan()
