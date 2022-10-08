
    
def corey():
    question = True
    penguin_question()
    def you_got_the_job():
        print("Congrats! You got the job! Now its time to call all of your friends and celebrate!")
        print(""" 

     .-""""""-.
   .'          '.
  /   O      O   \
 :                :
 |                |    
 : ',          ,' :
  \  '-......-'  /
   '.          .'
     '-......-'


          """)

    def ur_fired():
        print("You did not get the job. You walk away feeling sad")
        print("""  
        
        
        
     .-""""""-.
   .'          '.
  /   O      O   \
 :           `    :
 |                |   
 :    .------.    :
  \  '        '  /
   '.          .'
     '-......-' 


          """)
        
    
    def final_question():
        answer = input("Alright final question. Green or Blue? \n a) green \n b) red")
        if answer == 'a':
            print("My Mom's third-cousin's uncle's nephew's son does not like the color green. So we're not hiring you!")
            return ur_fired()
        elif answer == 'b':
            print("Thats my favorite color! We might have a potential new employee.")
            return you_got_the_job()
    
    def pool_question():
        answer = input("Fourth question, its getting crazy! If a tiger did a triple-twisted-backflip into a pool, what would you rate it? \n a) What?! Im definetely rating that a 10  \n b) Why would a tiger do that ")
        if answer == 'a':
            print("See thats what Im saying! That'll be crazy!")
            return final_question()
        elif answer == 'b':
            print("You lack imagination and creativity! That is something you need to have to work at this company!")
            return final_question()
    
    def biscuit_question():
        answer = input("Third question, get ready. What company would you want to be a biscuit from?  a) Chic-fil-a  b) Popeyes")
        if answer == 'a':
            print("Good choice. A biscuit with some quality")
            return pool_question()
        elif answer == 'b':
            print("You want to be a dry biscuit?! A dry biscuit means a dry personality and we cannot have that at this company.")
            return pool_question()

    def video_game_question():
        answer = input("Alright second question: What video games do you play? \n a) Rocket League \n b) COD \n c) Dance Dance Revolution  \n d) Overcooked" )
        if answer == 'a':
            print("Oh you play rocket league?! We just might have to hire you then.")
            return biscuit_question()
        elif answer == 'b':
            print("Okay I mess with COD too! Lets run sometime")
            return biscuit_question()
        elif answer == 'c':
            print("Huh..Dance Dance Revolution? I had no idea that game still existed")
            return biscuit_question()
        elif answer == 'd':
            print('Overcooked goes crazy. Maybe you could be the chef at the company')
            return biscuit_question()

    def penguin_question():
        print("You finally made it to your interview! Your interviewer will be Corey. Watch out though! He will ask some random questions")
    answer = input("Welcome to your first interview! What you do if you found a penguin in a freezer? \n a) Close the freezer and act like I never saw it  \n b) Call the animal shelter and let them figure it out ")
    if answer == 'a':
        print("Wow..So you're not going to do anything for the penguin")
        return video_game_question()
    elif answer == 'b':
        print("Look at you being a decent human being")
        return video_game_question()

        

    while question == True:
        corey()
        break