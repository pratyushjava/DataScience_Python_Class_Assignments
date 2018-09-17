# Pratyush Singh
# Programming Assignment #2, Part A


# This Program contains three shapes, uses at three distinct colors  

from drawingpanel import *

# This is the main fuction contains all the sub-fuctions.
# Man its easy there is nothing to read.
# Come on you still here read cafewall there is more insteresting stuff wating fayou  

def main(): 
             
    p = DrawingPanel( 300, 200, background="black")

    p.canvas.create_rectangle(50,50,100,100, fill="red", width=2)
    p.canvas.create_oval(100,50,120,120, fill="yellow", width=2)
    p.canvas.create_rectangle(150,50,200,200, fill="green", width=2)

           
        
main()

