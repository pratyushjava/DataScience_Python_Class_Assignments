# Name- Pratyush Singh
# Programming Assignment #2, Part B


# This program intends to draw several instances of the Café Wall illusion.
# In this optical illusion
# The rows appear not to be straight even though they are.
# This image has several levels of structure.
# Black and white squares are used to form rows and rows are combined to form grids.


from drawingpanel import*

MORTAR = 2

# This fuction includes all the parameters which are required to be passed.
# This fuction also includes the drawing panel.
# This fuction calls all the sub fuctions.
# Yo thats it bro! rest read down

def main():
    
    p = DrawingPanel( 650, 400, background= "grey")
    
    draw_row(p, 0, 0, 20, 4)
    
    draw_row(p, 50, 70, 30, 5)
       
    draw_grid(p, 10, 150, 25, 8, 0, 4)
    
    draw_grid(p, 250, 200, 25, 6, 10, 3)
    
    draw_grid(p, 425, 180, 20, 10, 10, 5)
    
    draw_grid(p, 400, 20, 35, 4, 35, 2)

# This fuction draws the the rows.
# All the paramenters of this fuction has been passed above
# Yo I can see you reading my codes.
# You seems to be intresed in my coding I can see in you eyes.

def draw_row(p, x, y, size, pair):
                                  
    for i in range(0,pair):
        draw_pair(p, x+(size*2)*i, y, size)
    
# Come on man as the name sugests you can see.
# This fuction creates the pair of the white and black boxs.
# Same as above all the parameters are being called above.
# Hey man you are still here I can see now you are loving my coding.
# Nice to see that. If you are still intresed roll your eyes down coz
# Best is yet to come man!

def draw_pair(p, x, y, size): 
           
    p.canvas.create_rectangle(x, y, size+x, size+y-MORTAR, fill= "black", width="0")
    
    p.canvas.create_rectangle(x+size, y, size+x+size, size+y-MORTAR, fill= "white",width="0")

    p.canvas.create_line(x, y, size+x, size+y-MORTAR, fill= "blue")

    p.canvas.create_line(x+size, y, x, size+y-MORTAR, fill= "blue")
    
# Come on man seriously as the name sugests you can see told you earlier.
# This fuction creates the grid and the grids which have offsets.
# The offsets causes the optical illusion.
# And man this is it. I know you love my coding.
# But rest for the next buddy cya.

def draw_grid(p, x, y, size, rows, offset, pairs): 

    row = 0
    for k in range(0,int(rows/2)):
        draw_row(p, x, y+size*row, size, pairs)
        row = row + 1

        draw_row(p, x+offset, y+size*row, size, pairs)
        row = row + 1

       

    
main()    
