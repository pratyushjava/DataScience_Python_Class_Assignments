# Name- Pratyush Singh
# Programming Assignment #5


# This assignment focuses on while loops and random numbers.
# program allows the user to play a game in which the program thinks of a random integer
# And accepts guesses from the user until the user guesses the number correctly.
# After each incorrect guess,the user will be told whether the correct answer is higher or lower.

from random import*

MAXIMUM_NUMBER = 100
MAXIMUM_GUESS  = 1000000000


# This is the main fuction it contains all the sub fuction.
# The sub fuctions in this main function gives a small summary of the whole program.
# Hey see who is this. You came again to read. Damm I am awesome.
# Thanks, well I knew that but you just proved me right.

def main():
    into() # intoduces the function
    game() # main game which is played.

# This program prints an introduction in the form of a haiku poem.
# A haiku has 3 lines: one with 5 syllables, the second with 7 syllables, and the third with 5 syllables.
# The below thing is not as awesome as I am, but still I just didn't know what to say.
# huhh you know my qualities right. I don't have to prove it.

def into():
    print("Hey come and play.")
    print("Say what, yeah you heard right.")
    print("The game which is fun.")

# A series of guessing games is played.
# In each game, the computer chooses a random number between 1 and 100 inclusive.
# The game asks the user for guesses until the correct number is guessed.
# After each incorrect guess, the program gives a clue about whether the correct number is higher or lower than the guess.
# Once the user types the correct number, the game ends and the program reports how many guesses were needed.
# Yeah I know above was shit.
# But now what is going to come this is fun just like me.

def game():
    play_again = 'y'
    best_game = MAXIMUM_GUESS
    total_games = 0
    total_guess = 0
    while(play_again[0] == 'y'):
        total_games +=1
        current_guess = play()
        if(current_guess > 0): # This loop tells that if the current guess is greater than 0 or not
            if(current_guess < best_game): # if the above loop exectutes than it will come to this loop than it will compare with the best game.
                best_game = current_guess
            total_guess += current_guess
            
        play_again = str(input("Do you want to play again? ")).lower()
        print()
    
    show_stats(total_games, total_guess, best_game)

# A function to play one game with the user    
# This fuction contains the code to ask the user to play again.
# Neither it plays multiples times in one call.
# I can see you, yeah you are looking at my code.
# It's nice right.
# No claps please, I know it's fun.

def play():
    print("I'm thinking of a number between 1 and ", MAXIMUM_NUMBER)
    guess = int(input("Your guess? "))
    if(not (guess >=0 and guess <= MAXIMUM_NUMBER)):
        print("sorry it seem you entered value out of range")
        return -1
    count = 0
    rand  = randint(1,MAXIMUM_NUMBER)
    while(guess != rand): # This loop runs until the user input is not equal to the random number.
        count += 1
        if(guess > rand): # This loop tell whether the user's guess is greater than random number or not
            print("It's higher.")
        elif(guess < rand ): # This loop tell whether the user's guess is less than random number or not
            print("It's lower.")
        guess = int(input("Your guess? "))
    
    print("You got it right in " + str(count + 1) + " guesses!")  # This will print the number of user took to get the correct ans.
    return count + 1
    
# A function to report the overall statistics to the user.
# This function should print the statistics only.
# Neither this function contains the while loop nor the playing games.
# Hey buddy bad news it's the end.
# But worries, WE are awesome next time even better dude.
# Yeah high five.
# Yo now that was one hell of a high.
# See your neighbours don't say anything coz of our awesomeness.

def show_stats(total_games, total_guess, best_game):
    average = round((total_guess /  total_games),1) # This calculates the average that is to be displayed,i.e., that stats.
    print("Total games = " , total_games) # prints total games.
    print("Total guesses = ", total_guess) # prints total guess
    print("Guesses/game = ", average) # prints average
    print("Best game = ", best_game) # prints the best game.
    

main()
