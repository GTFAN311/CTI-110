#Curtis Bauer
#29 Oct 2026
#P4LAB1
#Use turtle and loops to draw a square and a triangle.

#import the library
import turtle

#create the turtle window and drawing object
win = turtle.Screen()
t = turtle.Turtle()

#set turtle options
t.pensize(3)
t.pencolor("green")
t.shape("turtle")

for side in range(4):
    t.forward(100)
    t.right(90)
   
#while loop that executes 3 times
sides = 3

while sides > 0:
    t.forward(100)
    t.left(120)
    sides = sides - 1
      
#wait for window to close
win.mainloop()   