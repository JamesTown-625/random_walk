""" 
Student Name: James Teerlink 
Course: CS 1400 Fundamentals of Programming
Project 5: Random Walk - Coin Flip
Due Date: 11/01/2018
No help was used while writing this code

Use the turtle module to draw a birds eye view of a person 
walking dependent on the inputed number of steps to take. 
The person will randomly choose a direction to move every
time he/she takes a step. The starting point of the person
is always assumed to be 0,0 on an x/y axis grid with a max 
100x100 unit grid. Then draw a straight line from the end 
point to the start point and calculate its length and print
to the screen. 

0.  Import turtle, random and math modules to draw and get angles
1.  Instantiate the window object with the turtle.Screen() function
2.  Define a function called random_walk(steps) that takes 
    in integer of steps from the user input
3.  Inside function: Create a person named 'James' to draw line for each step
4.  Inside function: Use a while loop to keep person
    moving until it reaches the number of steps 
5.  Inside While loop: Use provided formulas to get random 
    direction to move
6.  Once while loop ends change pen color, save end coordinates, calculate
    distance from end to origin and draw a line back to origin
7.  Print distance to the window object and actual traveled distance
8.  Close the window object when the user clicks on the screen
"""

#import turtle and math modules to draw and get angles
import turtle
import math
import random

#instantiate the window object
wn = turtle.Screen()

#define the function called random_walk(steps)
def random_walk(steps):
    james = turtle.Turtle()
    james.color('blue')

    step = 0
    x = 1
    y = 1
    while step < steps:
        angle = random.random() * 2 * math.pi
        
        x = x + math.cos(angle)
        
        y = y + math.sin(angle)
        
        step = step + 1
        james.goto(x, y)
    
    print("Actual dist. traveled: ", step)
  
    dt = math.sqrt(((james.xcor() - 0)**2) + ((james.ycor() - 0)**2))
    james.color('red')
    james.goto(0,0)
    james.write("{:.0f}".format(dt))
    print("Straight line dist: {:.0f}".format(dt))

steps = int(input("Enter the number of steps you want to randomly take >> "))

random_walk(steps)

wn.exitonclick()
