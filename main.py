import turtle


#declaring variables
run = True
radius = 40
shells = 0

#checking for input error
try:
    electron_inp = int(input("Enter the number of electrons in the atom: "))
except ValueError:
    print("please enter a valid value")
    electron_inp = int(input("Enter the number of electrons in the atom: "))

#checking for number of shells in the atom
if shells < 0:
    print("please enter a value greater than 0 next time")
    run = False
elif shells > 0 and shells <= 2:
    shells = 1
elif shells > 2 and shells <= 8:
    shells = 2
elif shells > 8 and shells <= 18:
    shells = 3
else:
    shells = 4


#creating window
win = turtle.Screen()
win.setup(width=600, height=600)
win.tracer(0)

#creating turtle
t = turtle.Turtle()
t.pensize(5)
t.color("black", "red")

#drawing nucleus
def draw_nucleus():
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

#drawing electron

def draw_electron(r, extent):
    #declaring variables
    global electron_radius
    electron_radius = 10

    #setting color
    t.color("black", "yellow")

    #setting position
    t.penup()
    t.setheading(t.heading() - 90)
    t.forward(10)
    t.setheading(t.heading() + 90)

    #drawing electron
    t.pendown()
    t.begin_fill()
    t.pendown()
    t.circle(electron_radius)
    t.end_fill()

    #going back and moving to the next position
    t.penup()
    t.setheading(t.heading() - 90)
    t.back(10)
    t.setheading(t.heading() + 90)

    t.circle(r, extent)
    


#drawing first shell
def shell_1():
    """
    logic behind the function in steps:
        1. check if the shell is full or not, if it draw a full shell otherwise draw one electron calling the function once
        2. using a while loop to call the function multiple times according to the requirement
        3. passing in input in the form of variables delcared globally in the function
    """

    #declaring variables
    global full_1, n, fse, increment_y, rotation
    full_1  = False
    n = 0
    fse = electron_inp - 2
    increment_y = -10
    rotation = 2

    #drawing plain orbit
    t.penup()
    t.sety(t.ycor() - radius)
    t.pendown()
    t.circle(radius * 2)

    #condition and loop to draw electrons
    if fse >= 0 or electron_inp >= 2:
        full_1 = True
        n = 2
    else:
        full_1 = False  
    
    if full_1 == True:
        while n > 0:
            draw_electron(radius * 2, 360/n)
            n -= 1
    else:
        draw_electron(0, 0)

    t.circle(radius * 2, 180)


def shell_2():
    #declaring variables
    if shells >= 2:
        global electrons, n_2, full_2
        n_2 = electron_inp - 2

        if n_2 > 0:
            #drawing plain orbit
            if electron_inp >= 2 or electron_inp - 2 > 0:
                if t.ycor() < 0:
                    t.penup()
                    t.sety(t.ycor() - radius)
                    t.pendown()
                    t.circle(radius * 3)
                else:
                    t.circle(radius * 2, 180)
                    t.penup()
                    t.sety(t.ycor() - radius)
                    t.pendown()
                    t.circle(radius * 3)

                #drawing electrons
                num = n_2

                if n_2 >= 8 or electron_inp >= 8:
                    full_2 = True
                else:
                    full_2 = False

                if num > 8:
                    n_2 = 8
                    num = n_2
                        

                if full_2 == True:
           
                    while num > 0:
                        draw_electron(radius * 3, 360/n_2)
                        num -= 1
                else:
                    while num > 0:
                        draw_electron(radius * 3, 360/n_2)
                        num -= 1

        
def shell_3():
    #declaring variables
    if shells >= 3:
        global electrons, n_3, full_3
        n_3 = electron_inp - 10

        if n_3 > 0:
            #drawing plain orbit
            if electron_inp >= 2 or electron_inp - 2 > 0:
                if t.ycor() < 0:
                    t.penup()
                    t.sety(t.ycor() - radius)
                    t.pendown()
                    t.circle(radius * 4)
                else:
                    t.circle(radius * 3, 180)
                    t.penup()
                    t.sety(t.ycor() - radius)
                    t.pendown()
                    t.circle(radius * 4)

                #drawing electrons
                num = n_3

                if n_3 >= 8 or electron_inp >= 8:
                    full_3 = True
                else:
                    full_3 = False

                if num > 8:
                    n_3 = 8
                    num = n_3
                        

                if full_3 == True:
           
                    while num > 0:
                        draw_electron(radius * 4, 360/n_3)
                        num -= 1
                else:
                    while num > 0:
                        draw_electron(radius * 4, 360/n_3)
                        num -= 1

def shell_4():
    #declaring variables
    if shells >= 3:
        global electrons, n_4, full_4
        n_4 = electron_inp - 18

        if n_4 > 0:
            #drawing plain orbit
            if electron_inp >= 2 or electron_inp - 2 > 0:
                if t.ycor() < 0:
                    t.penup()
                    t.sety(t.ycor() - radius)
                    t.pendown()
                    t.circle(radius * 5)
                else:
                    t.circle(radius * 4, 180)
                    t.penup()
                    t.sety(t.ycor() - radius)
                    t.pendown()
                    t.circle(radius * 5)

                #condition and loop to draw electrons
                num = n_4

                if n_4 >= 2 or electron_inp >= 20:
                    full_4 = True
                else:
                    full_4 = False

                if num > 2:
                    n_4 = 2
                    num = n_4

                if full_4 == True:
                    while num > 0:
                        draw_electron(radius * 5, 360/n_4)
                        num -= 1
                else:
                    draw_electron(0, 0)


draw_nucleus()
shell_1()
shell_2()
shell_3()
shell_4()

#main loop
while run:
    win.update()