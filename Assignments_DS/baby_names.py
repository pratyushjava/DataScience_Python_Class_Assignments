
# Name- Pratyush Singh
# Programming Assignment #6


'''
This assignment focuses on reading input files.
This program has used the drawing panel
'''
from drawingpanel import *

"""
below are default variables used to control layout of the drawing pannel
"""
starting_year = 1890
width = 60
legend_height = 30

"""
The controler of the program.
This fuction contains all the main function. 
"""
def main():
    fname = "names.txt"
    fmeaning = "meanings.txt"
    name = str(input("Name: "))
    gender = str(input("Gender: "))
    
    # get the line, if name exist in the names.txt
    name_line = find_name(fname, name, gender)
    meaning_line = ""
    
    # go for finding the meaning and drawing the histogram only if name exist in the names.txt
    if(len(name_line) > 2):
        # Draw the default layout of the panel
        panel = DrawingPanel(780,500 + (2*legend_height),background = "white")
        # Get meaning of the name from meanings.txt
        meaning_line = find_name(fmeaning, name, gender)
        # Draw the legends top and bottom and then put the meaning at the top rectangle
        draw_basics(panel, meaning_line)
        # Draw Histogram based on the data retrived from the file
        draw_histogram(panel, name_line)
    else:
        print("Name Not Found")




"""
This is a file reader function.
Takes input a file name, name of child and child gender.
Once the user types a name and gender,
search each line of names.txt to see if it contains data for that name and gender. 
"""
def find_name(fname, name, gender):
    # conver all into lower case to avoid discrepancy
    name = name.lower()
    gender = gender.lower()
    # open file
    file = open(fname)
    # Read line by line
    for line in file.readlines():
        # for each line split 
        words = line.split(" ")
        # check if name and gender matches, 
        if name == str(words[0]).lower() and gender == str(words[1]).lower():
            file.close() # close file
            return line
    file.close()
        
    return ""

"""
 Draw the legends top and bottom and then put the meaning at the top rectangle.
 The panel's overall size is 780x560 pixels.
 Its background is white.
 It has light gray ("light gray") filled rectangles along its top and bottom with a black line at their bottom and top, respectively.
 The two rectangles are each 30 pixels tall and span across the entire panel, leaving an open area of 780x500 pixels in the middle.
 The line of data about the name's meaning appears in the top gray rectangle at (390, 16).
"""
def draw_basics(p, meaning_line):
    # Draw top rectangle
    p.canvas.create_rectangle(0,0,780,legend_height, fill = "light gray")
    # Draw bottom rectangle
    p.canvas.create_rectangle(0,500 + legend_height,780,500 + (2 * legend_height), fill = "light gray")
    # put the meaning in the top rectangle
    p.canvas.create_text(390,16,text = meaning_line)



"""
create histogram.
Starting at the same x-coordinate, a bar shows the name ranking data for each year.
The bars are light green for male names and yellow for female names.
Bars are half as wide as each decade (30px).
The table at right shows the mapping between rankings and y-values of the tops of bars.
Y-values start at 30 (below the top gray rectangle), and there is a vertical scaling factor of 2 between pixels and rankings.
With a legend height of 30, the y-coordinate is 30 plus the rank divided by 2.
"""
def draw_histogram(p, name_line):
    # remove extra spaces and endline
    name_line = name_line.strip()
    # split the line 
    ranks = name_line.split(" ")
    rank_count = 0
    bars_color = ""
    # set the color for histogram based on male or female
    if(str(ranks[1]).lower() == "f"):
        bars_color = "yellow"
    else:
        bars_color = "light green"
    ranks.pop(0)
    ranks.pop(0)
    for rank in ranks:
        # start of decade x-coordinate
        rank_pixel_x = width * rank_count + 15
        # create the decade label
        p.canvas.create_text(rank_pixel_x, 500 + (2 * legend_height) - 8 ,text = starting_year + rank_count * 10)
        # considering 0 to be last for easy calculation
        if(int(rank) == 0):
            rank = 1000
        # Create histogram
        p.canvas.create_rectangle(rank_pixel_x, legend_height + int(rank)/2 , rank_pixel_x + (width/2) ,500 + legend_height ,fill = bars_color)
        # Create rank label at top of the histogram
        p.canvas.create_text(rank_pixel_x, legend_height + int(rank)/2 ,text = ranks[rank_count] , font = "bold")
        rank_count+=1
main()
