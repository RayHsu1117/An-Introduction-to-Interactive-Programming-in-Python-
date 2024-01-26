import simplegui
import random
import math
secret_number = 0
low_bound = 0
high_bound = 100
quess_time = 0
def new_game():
    global secret_number 
    global low_bound 
    global high_bound
    global guess_time
    secret_number = random.randrange(low_bound,high_bound)    
    guess_time =int(math.ceil(math.log(high_bound,2)))
    print "new game"
    print "Range is [" +str(low_bound)+","+str(high_bound)+")"
    print "Number of remaining guesses is "+str(guess_time) +"\n"
def range100():
    global high_bound
    high_bound = 100
    new_game()
def range1000():
    global high_bound
    high_bound = 1000
    new_game()
def input_guess(guess):
    print "Guess was "+ guess
    guess_int = int(guess)
    global secret_number
    global low_bound 
    global high_bound
    global guess_time    
    if secret_number > guess_int:        
        guess_time = guess_time - 1
        if guess_time == 0:
            print "You ran out of guesses.  The number is "+str(secret_number)
            print "Lose"
            low_bound = 0
            high_bound = 100
            new_game()
            return
        print "Number of remaining guesses is "+str(guess_time)
        print "Higher!"+"\n"
    elif secret_number < guess_int:        
        guess_time = guess_time - 1
        if guess_time == 0:
            print "You ran out of guesses.  The number is "+str(secret_number)
            print "Lose"
            low_bound = 0
            high_bound = 100
            new_game()
            return
        print "Number of remaining guesses is "+str(guess_time)
        print "Lower!"+"\n"
    else:
        print "Correct!\n"
        new_game()
        return  
    
# create frame
frame = simplegui.create_frame('Testing', 200, 200)
inp = frame.add_input('input guess', input_guess, 50)
button1 = frame.add_button("Range is [0,100)", range100)
button2 = frame.add_button("Range is [0,1000)", range1000) 
new_game()
secret_number = 74	
input_guess("50")
input_guess("75")
input_guess("62")
input_guess("68")
input_guess("71")
input_guess("73")
input_guess("74")
range100()
secret_number = 28	
input_guess("50")
input_guess("50")
input_guess("50")
input_guess("50")
input_guess("50")
input_guess("50")
input_guess("50")
# always remember to check your completed program against the grading rubric