import turtle
import time
import random

WIDTH,HEIGHT = 500,500
COLORS=['red','green','blue','orange','yellow','black','purple','pink','brown','cyan']

def get_number_of_racers():
    racers=0
    while True:                                     #continue to take input till we get valid input
        racers=input("Enter the number of the racers(3-10): ")
        if racers.isdigit():                        #check if input string is numeric
            racers=int(racers)                      #convert that string to numeric
        else:
            print("Input is not numeric...Try again!")
            continue

        if 3 <= racers <= 10:
            return racers
        else:
            print("Number not in range 3-10. Try again")

def race(colors):
    turtles = create_turtles(colors)
    turtle.Screen().bgcolor("light green")

    while True:
        for racer in turtles:
            distance= random.randrange(1,20)
            racer.forward(distance)             #moves the turtle that amount of distance randomly

            x,y= racer.pos()
            if y>= HEIGHT//2 -10:
                return colors[turtles.index(racer)] #returns the index of the racer then we find the corresponding color to that index

def create_turtles(colors):
    turtles = []
    spacingx =WIDTH // (len(colors))
    for i,color in enumerate(colors): #create the number of turtles as the number of colors
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)                              #90 is angle here
        racer.penup()                               #hide line initially
        racer.setpos(-WIDTH//2+ (i+1) *spacingx,-HEIGHT//2 +20)      #set.position
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("Winner is ",winner)
time.sleep(2)





