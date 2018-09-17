# Name- Pratyush Singh
# Programming Assignment #2, Part B


# This fuction intends to create rocketship and change the size of the figure when required.
# And to lessen the redundancy as much as possible.

SIZE = 3 # a constant variable to change the size of the rocketship

def main(): # this is the main fuction in which it has every sub fuction to call.
    triangle()
    line()
    middle_upper()
    line()
    middle_lower()
    line()
    triangle()
  
def triangle(): # This fuction creates the top and the bottom portion of the program.
    for line in range(1,2*SIZE):
        for j in range(1,-1*line+(2 * SIZE )+1):
            print(" ", end='')
        for j in range(1,1*line+1):
            print("/", end='')
        for j in range(1,3):
            print("*", end='')
        for j in range(1,1*line+1):
            print("\\", end='')       
        print()
        

def line(): # This fuction seperates the different portions of the rocketships through lines. 
    print("+", end = '')
    for i in range(1,2*SIZE+1):
        print("=*", end = '')
    print("+")

def upper(): # This fuction creates the middle upper half of the rocketship
    for line in range(1, SIZE+1):
        print("|",end='')
        for l in range(1, 3):
            for i in range(1,-1*line+SIZE+1):
                print(".", end='')

            for j in range(1, line + 1):
                print("/\\", end='')

            for k in range(1,-1*line+SIZE+1):
                print(".", end='')
        print("|")
        
def lower(): # This fuction creates the middle lower half of the rocketship
    for line in range(SIZE, 0, -1):
        print("|",end='')
        for l in range(1, 3):
            for i in range(1,-1*line+SIZE+1):
                print(".", end='')

            for j in range(1, line +1):
                print("\\/", end='')

            for k in range(1,-1*line+SIZE+1):
                print(".", end='')
        print("|")
    
def middle_upper(): # This fuction creates the upper portion body of the rocketship
    upper()
    lower()   

def middle_lower(): # This fuction creates the lower portion body of the rocketship
    lower()
    upper()
    
main()            
            
        
    

