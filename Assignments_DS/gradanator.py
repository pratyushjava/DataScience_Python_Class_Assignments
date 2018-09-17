# Pratyush Singh
# Programming Assignment #2, Part B


# This interactive program focuses on if/else statements, input, and returning values.
# The program reads as input a student's grades on homework and three exams and uses them to compute the student's course grade.
# The program begins with an introduction message that briefly explains the program. The program then reads scores in four categories: midterm 1, midterm 2, homework and final.
# Each category is weighted: its points are scaled up to a fraction of the 100 percent grade for the course. 
# Yo lot of talking is done lets have some real fun. 


MAX = 100
MIN = 0

# This is the main fuction it contains all the sub fuction.
# The sub fuctions in this main function gives a small summary of the whole program.
# Come on man why to read this boring stuff read some intresting stuff belows,i.e, codes

def main(): 
    
    intro()
    weighted_score = 0
    WEIGHT = 0
    weighted_score += exams("Midterm 1:", WEIGHT)
    weighted_score += exams("Midterm 2:", WEIGHT)
    weighted_score += exams("Final:", WEIGHT)
    weighted_score += homework("Homework:", WEIGHT)
    grades(weighted_score)
    
# This fuction presents the introduction of the program.
# Man this is shit actual fun is below.
  
def intro():
    print("This program reads exam/homework scores")
    print("and reports your overall course grade.")
    print()

# Yeah man you thought it. See you can feel it. See the smile on your face. OMG! What a lovely smile.
# This fuction Give the grades based on the weighted score.
# This fuction has used if-elif-else statements.

def grades(weighted_score):
    print("Overall percentage = "+str(round(weighted_score,1)))
    
    if(weighted_score>=90 and weighted_score<=100):
        print("Your grade will be at least: A")
        print("Excellent")
    elif(weighted_score>=80 and weighted_score<90):
        print("Your grade will be at least: B")
        print("Good Job")
    elif(weighted_score>=70 and weighted_score<80):
        print("Your grade will be at least: C")
        print("Not Bad")
    elif(weighted_score>=60 and weighted_score<70):
        print("Your grade will be at least: D")
        print("Bad")
    else:
        print("Your grade will be at least: F")
        print("Very Bad")

# This fuction calculates the exam score and returns the weight score.
# This fuction just has a single "if" statement.
# Hey dude having fun huhh. Told you. There is still whole lot to come!
    
def calculate_exam_score(weight, score, shift_amount):

    score += shift_amount
    if(score > MAX):
        score = MAX
    print ("Total points = "+ str(score) +" / 100" )
    weighted_score = (score/100)*weight
    print ("Weighted score = "+ str(round(weighted_score,1)) +" / "+str(weight) )
    return weighted_score
    
# This fuction contains Midterm 1, Midterm 2 and final.
# This fuction prints the statement and take the user input for the result of the exams.
# Hey man! hakuna matata btw a must watch animated show.

def exams(x, WEIGHT):

    print( str( x) ) 
    
    weight = int( input( "Weight (0-100)? ") )
    if(weight < MIN):
        return MIN
    else:
        WEIGHT+=weight
        if(WEIGHT > 100):
            return MIN
        
    score = int( input( "Score earned? ") )
    if(score > MAX):
        score = 100

    shift = int(input( "Were scores shifted (1=yes, 2=no)? "))
    shift_amount = 0
    if (shift == 1):
        shift_amount = int(input( "Shift amount? "))


    weighted_score = calculate_exam_score(weight, score, shift_amount)
    print()
    return weighted_score

# This fuction gives the homework calculations.
# This fuction has been created with a bunch of if-else statements.
# This fuction calculates the homework by user input.
# I know man you are feeling sad. But I cant do much man.
# huhhhaa no no no dont bring you smile down.
# Smile coz you are beautiful!
# Promise I'll come again and next even better.


def homework(x, WEIGHT):

    print( str( x) ) 
    
    weight = int( input( "Weight (0-100)? ") )
    if(weight < MIN):
        return MIN
    else:
        WEIGHT+=weight
        if(WEIGHT > 100):
            return MIN
    
    number = int( input( "Number of assignments? ") )
    if(number < 1):
        return MIN

    assignments_score = 0
    assignments_max = 0
    for i in range( 1, number+1):
        assignments_score += int( input( "Assignment " + str(i) + " score? ") )
        assignments_max += int( input( "Assignment " + str(i) + " max? ") )
        
    if(assignments_score > assignments_max):
        assignments_score = assignments_max


    sections = int( input( "How many sections did you attend? "))

    section_points = sections * 3
    
    max_section_points = 34
    if(section_points > max_section_points):
        section_points = max_section_points

    print("Section points = " + str(section_points) + " / 34")

    total_homework_points = section_points + assignments_score
    total_homework_max  = max_section_points + assignments_max
    
    print("Total points = "+str(total_homework_points)+" / "+str(total_homework_max))
    
    weighted_homework_score = (total_homework_points / total_homework_max) * weight
    
    print("Weighted score = "+str(round(weighted_homework_score,1))+" / "+str(weight))

    print()
    
    return weighted_homework_score
    

main()    
