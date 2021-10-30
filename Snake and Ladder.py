# Student ID: 19009987 
# Date of modification: 14th April 2021
# 4COM1037 Programming Coursework
# Version 2 of 2

import turtle       # imports turtle
import time         # imports time
import random       # imports random

def setup():                            # this function sets up the window
    turtle.title("Snakes And Ladders")  # turtle window's title will be Snakes and Ladder
    turtle.setup(650, 650, 0, 0)        # setups the screen size (in pixels - 650 x 650) and the starting position of the screen is (0,0)
    turtle.bgcolor("#E3FF62")           # background color for the turtle window
    turtle.pencolor("#7E62FF")          # pen color for the turtle window
    turtle.width(5)                     # pen width is 5
    turtle.speed(10)                    # speed of the movement (10 is fast)

def pen_message(message="", font="", font_size=0, loc_x=0, loc_y=0):      # this function it takes a message with it's properties(font type, font size, x axis location, y axis location) then it displays it on the screen
    pen = turtle.Turtle(visible=False)                                    # defining a new turtle which has a starting property which is hidden
    pen.speed(0)                                                          # speed of the movement (0 is the fastest)
    pen.pencolor("#FF6294")                                               # pen color for the message
    pen.penup()                                                           # stops drawing
    pen.goto(loc_x, loc_y)                                                # moves turtle's coordinate at (loc_x , loc_y)
    pen.write(message, align="center", font=(font, font_size, "normal"))  # this writes on the turtle screen
    return message                                                        # returns message so it can used later in another function


def add_shapes():                      # adds images to the turtle shape
    turtle.addshape("bull.gif")
    turtle.addshape("cow.gif")
    turtle.addshape("elephant.gif")
    turtle.addshape("panda.gif")
    turtle.addshape("bunny.gif")
    turtle.addshape("fox.gif")
    turtle.addshape("penguin.gif")
    turtle.addshape("ladder.gif")
    turtle.addshape("ladder2.gif")
    turtle.addshape("ladder3.gif")
    turtle.addshape("snake.gif")
    turtle.addshape("snake2.gif")
    turtle.addshape("snake3.gif")
    turtle.addshape("dice1.gif")
    turtle.addshape("dice2.gif")
    turtle.addshape("dice3.gif")
    turtle.addshape("dice4.gif")
    turtle.addshape("dice5.gif")
    turtle.addshape("dice6.gif")
    turtle.addshape("win.gif")
    turtle.addshape("logo.gif")
    turtle.addshape("vss.gif")


def logo():                          # this function is respsssonsible fo showing the logo
    logo_turtle = turtle.Turtle()    # defining a new turtle
    logo_turtle.penup()              # stops drawing
    logo_turtle.shape("logo.gif")    # calling the shape which was added before in add_shapes()
    logo_turtle.goto(0, 250)         # moves turtle's coordinate at (0,250)
    return logo_turtle               # returns logo_turtle so it can be used later in another function


def show_screen1():                                                         # this function asks for the player name and prints it on the screen
    turtle.hideturtle()                                                     # this hides the turtle
    setup()                                                                 # calling the function setup
    logo()                                                                  # calling the function logo
    turtle.penup()                                                          # stops drawing
    turtle.goto(-130, 80)                                                   # moves turtle's coordinate at (-130,50)
    turtle.write("Please enter your names", font=("Verdana", 15, "normal"))  # this writes on the turtle screen

    turtle.penup()                                          # stops drawing
    turtle.goto(-50, 10)                                    # moves turtle's coordinate at (-50,0)
    turtle.write("Player 1", font=("Verdana", 15, "bold"))  # this writes on the turtle screen

    turtle.penup()                    # stops drawing
    turtle.goto(-150,0)             # moves turtle's coordinate at (-150,-10)
    for drawing_2_lines in range(2):  # this loop draws two lines twice inorder to make a rectangle
        turtle.pendown()              # starts drawing
        turtle.forward(300)           # moves the turtle forward by 300 pixels
        turtle.right(90)              # makes the turtle turn right by 90 degree
        turtle.forward(70)            # moves the turtle forward by 70 pixels
        turtle.right(90)              # makes the turtle turn right by 90 degree
    turtle.left(90)                   # making it go back to normal position

    player1_name = pen_message(input("Please enter name for player 1: "), "Verdana", 15, 0, -44)  # calling the function pen message and retriving player 1 name from it

    turtle.penup()                                           # stops drawing
    turtle.goto(-50, -140)                                   # moves turtle's coordinate at (-50,-150)
    turtle.write("Player 2", font=("Verdana", 15, "bold"))   # this writes on the turtle screen

    turtle.penup()                  # stops drawing
    turtle.goto(-150,-150)          # moves turtle's coordinate at (-150,-160)
    for drawing_lines in range(2):  # this loop draws two lines twice inorder to make a rectangle
        turtle.pendown()            # starts drawing
        turtle.right(90)            # makes the turtle turn right by 90 degree
        turtle.forward(300)         # moves the turtle forward by 300 pixels
        turtle.right(90)            # makes the turtle turn right by 90 degree
        turtle.forward(70)          # moves the turtle forward by 70 pixels

    player2_name = pen_message(input("Please enter name for player 2: "), "Verdana",15, 0, -195)   # calling the function pen message and retriving player 1 name from it
    pen_message("Match will be played between " + player1_name + " and " + player2_name, "Verdana", 15, 0, -290)  # calling the function pen message and displaying player 1 name and player 2 name from it and displaying it on the turtle window
    time.sleep(3)                                                                         # holds the program for 3 seconds
    print("Match will be played between ", player1_name, "and", player2_name, sep=" ")    # prints on screen about the match being played between the players
    return player1_name, player2_name        # returns players names so it can be used later in a function


def player_choice(player_name, cow, penguin, elephant, bull, panda, bunny):  # this function takes the player name and all the characters available for the user to choose from and it returns one of characters after asking the user for his choice
    choice = "jhrfgh"                                                        # pre-defining the variable choice before asking the user for his choice
    while choice not in ["1", "2", "3", "4", "5", "6"]:                      # looping indefinitely until the user enters a valid number
        choice = input("\n" + player_name + " please choose your character: ")      # asking user to input his choice
        if choice == "1":                                                    # if choice is equal to 1 then execute the following code
            print(player_name + " chose Cow")                                # prints player name choose cow
            return cow                                                       # returns cow
        elif choice == "2":                                                  # if choice is equal to 2 then execute the following code
            print(player_name + " chose Penguin")                            # prints player name choose penguin
            return penguin                                                   # returns penguin
        elif choice == "3":                                                  # if choice is equal to 3 then execute the following code
            print(player_name + " chose Elephant")                           # prints player name choose elephant
            return elephant                                                  # returns elephant
        elif choice == "4":                                                  # if choice is equal to 4 then execute the following code
            print(player_name + " chose Bull")                               # prints player name choose bull
            return bull                                                      # returns bull
        elif choice == "5":                                                  # if choice is equal to 5 then execute the following code
            print(player_name + " chose Panda")                              # prints player name choose panda
            return panda                                                     # returns panda
        elif choice == "6":                                                  # if choice is equal to 6 then execute the following code
            print(player_name + " chose Bunny")                              # prints player name choose bunny
            return bunny                                                     # returns bunny
        else:                                                                # if any of the conditions above aren't true then execute the following code
            print("Enter a valid number")                                    # prints on the screen


def show_screen2(player1_name, player2_name):                             # this function takes the player name and it returns one of characters for each player
    turtle.clearscreen()                                                  # this clears screen
    setup()                                                               # calls the function setup()
    logo_turtle = logo()                                                  # calling the function logo and storing it in logo turtle
    turtle.hideturtle()                                                   # this hides the turtle
    turtle.penup()                                                        # stops drawing
    turtle.goto(-130, 100)                                                # moves turtle's coordinate at (-130,100)
    turtle.write("Choose your characters", font=("Verdana", 15, "bold"))  # writes on the turtle screen

    penguin = turtle.Turtle(shape="penguin.gif")            # defining a new turtle and adding shape on the screen
    penguin.penup()                                         # stops drawing
    penguin.goto(0, 20)                                     # moves turtle's coordinate at (0,20)

    cow = turtle.Turtle(shape="cow.gif")                    # defining a new turtle and adding shape on the screen
    cow.penup()                                             # stops drawing
    cow.goto(-200, 20)                                      # moves turtle's coordinate at (-200,20)

    elephant = turtle.Turtle(shape="elephant.gif")          # defining a new turtle and adding shape on the screen
    elephant.penup()                                        # stops drawing
    elephant.goto(200, 20)                                  # moves turtle's coordinate at (200,20)

    bunny = turtle.Turtle(shape="bunny.gif")                # defining a new turtle and adding shape on the screen
    bunny.penup()                                           # stops drawing
    bunny.goto(200, -150)                                   # moves turtle's coordinate at (200,-150)

    panda = turtle.Turtle(shape="panda.gif")                # defining a new turtle and adding shape on the screen
    panda.penup()                                           # stops drawing
    panda.goto(0, -150)                                     # moves turtle's coordinate at (0,-150)

    bull = turtle.Turtle(shape="bull.gif")                  # defining a new turtle and adding shape on the screen
    bull.penup()                                            # stops drawing
    bull.goto(-200, -150)                                   # moves turtle's coordinate at (-200,-150)

    turtle.penup()                                          # stops drawing
    turtle.goto(-230, -30)                                  # moves turtle's coordinate at (-230,-30)
    turtle.write("Cow", font=("Verdana", 15, "bold"))       # this writes on the turtle screen

    turtle.penup()                                          # stops drawing
    turtle.goto(-210, -55)                                  # moves turtle's coordinate at (-210,-55)
    turtle.write("1", font=("Verdana", 15, "bold"))         # this writes on the turtle screen

    turtle.penup()                                          # stops drawing
    turtle.goto(-50, -30)                                   # moves turtle's coordinate at (-50,-30)
    turtle.write("Penguin", font=("Verdana", 15, "bold"))   # this writes on the turtle screen

    turtle.penup()                                          # stops drawing
    turtle.goto(-10, -55)                                   # moves turtle's coordinate at (-10,-55)
    turtle.write("2", font=("Verdana", 15, "bold"))         # this writes on the turtle screen

    turtle.penup()                                          # stops drawing
    turtle.goto(150, -30)                                   # moves turtle's coordinate at (150,-30)
    turtle.write("Elephant", font=("Verdana", 15, "bold"))  # this writes on the turtle screen

    turtle.penup()                                          # stops drawing
    turtle.goto(190, -55)                                   # moves turtle's coordinate at (190,-55)
    turtle.write("3", font=("Verdana", 15, "bold"))         # this writes on the turtle screen

    turtle.penup()                                          # stops drawing
    turtle.goto(-225, -200)                                 # moves turtle's coordinate at (-225,-200)
    turtle.write("Bull", font=("Verdana", 15, "bold"))      # this writes on the turtle screen

    turtle.penup()                                          # stops drawing
    turtle.goto(-215, -225)                                 # moves turtle's coordinate at (-215,-225)
    turtle.write("4", font=("Verdana", 15, "bold"))         # this writes on the turtle screen

    turtle.penup()                                          # stops drawing
    turtle.goto(-35, -200)                                  # moves turtle's coordinate at (-35,-200)
    turtle.write("Panda", font=("Verdana", 15, "bold"))     # this writes on the turtle screen

    turtle.penup()                                          # stops drawing
    turtle.goto(-5, -225)                                   # moves turtle's coordinate at (-5,-225)
    turtle.write("5", font=("Verdana", 15, "bold"))         # this writes on the turtle screen

    turtle.penup()                                          # stops drawing
    turtle.goto(165, -200)                                  # moves turtle's coordinate at (165,-200)
    turtle.write("Bunny", font=("Verdana", 15, "bold"))     # this writes on the turtle screen

    turtle.penup()                                          # stops drawing
    turtle.goto(190, -225)                                  # moves turtle's coordinate at (190,-225)
    turtle.write("6", font=("Verdana", 15, "bold"))         # this writes on the turtle screen

    turtle.penup()                                          # stops drawing
    turtle.goto(-205, -300)                                 # moves turtle's coordinate at (-205,300)
    turtle.write("Note: Please choose the appropriate \n              number from (1-6) ", font=("Verdana", 15, "bold"))  # writes on the turtle screen

    character1 = player_choice(player1_name, cow, penguin, elephant, bull, panda, bunny)    # making the character 1 equal to player choice for choosing character so it can be used later
    character2 = player_choice(player2_name, cow, penguin, elephant, bull, panda, bunny)    # making the character 2 equal to player choice for choosing character so it can be used later

    # hides turtle
    cow.hideturtle()
    penguin.hideturtle()
    elephant.hideturtle()
    bull.hideturtle()
    panda.hideturtle()
    bunny.hideturtle()
    logo_turtle.hideturtle()

    return character1, character2    # return characters so it can be used later in a function


def draw_board():             # this function draws the lines of the board
    turtle.penup()            # stops drawing
    turtle.goto(-250, -250)   # moves turtle's coordinate at (-250,-250)
    turtle.pendown()          # stars drawing
    turtle.left(90)           # makes the turtle turn left by 90 degree
    turtle.forward(500)       # moves the turtle forward by 500 pixels

    for lines in range(11):      # looping 11 times for each of the 11 lines
        if lines % 2 == 0:       # if remainder of lines/2 equal 0 then execute the following code
            turtle.right(90)     # makes the turtle turn right everytime by 90 degree
            turtle.forward(100)  # moves the turtle forward everytime by 100 pixels
            turtle.right(90)     # makes the turtle turn right everytime by 90 degree
            turtle.forward(500)  # moves the turtle forward everytime by 500 pixels
        elif lines == 5:         # if the first condition isn't true and lines equal 5 then execute the following code
            turtle.right(90)     # makes the turtle turn right everytime by 90 degree
            turtle.forward(500)  # moves the turtle forward everytime by 500 pixels
        else:                    # if it is not true to any of the above conditions then execute the following code
            turtle.left(90)      # makes the turtle turn left everytime by 90 degree
            turtle.forward(100)  # moves the turtle forward everytime by 100 pixels
            turtle.left(90)      # makes the turtle turn left everytime by 90 degree
            turtle.forward(500)  # moves the turtle forward everytime by 500 pixels

def write_numbers():            # this function writes the numbers on board
    turtle.penup()              # stops drawing
    turtle.goto(-340, -175)     # moves turtle's coordinate at (-340,-175)
    for line1 in range(5):      # looping 5 times for writing numbers on the line
        turtle.penup()          # stops drawing
        turtle.forward(100)     # moves the turtle forward everytime by 100 pixels
        turtle.write(line1 + 1, font=("Verdana", 15, "normal"))  # this writes numbers on window from 1-5 as it will add 1 with the current number eg (0+1,..,4+1)

    turtle.goto(260, -75)       # moves turtle's coordinate at (260,-75)
    for line2 in range(6, 11):  # looping 5 times starting from 6 for writing numbers on the line
        turtle.penup()          # stops drawing
        turtle.forward(-100)    # moves the turtle forward everytime by -100 pixels
        turtle.write(line2, font=("Verdana", 15, "normal"))  # this writes numbers on window from 6-10

    turtle.goto(-340, 25)       # moves turtle's coordinate at (-340,25)
    for line3 in range(11, 16): # looping 5 times starting from 11 for writing numbers on the line
        turtle.penup()          # stops drawing
        turtle.forward(100)     # moves the turtle forward everytime by 100 pixels
        turtle.write(line3, font=("Verdana", 15, "normal"))  # this writes numbers on window from 11-15

    turtle.goto(260, 125)       # moves turtle's coordinate at (260,125)
    for line4 in range(16, 21): # looping 5 times starting from 16 for writing numbers on the line
        turtle.penup()          # stops drawing
        turtle.forward(-100)    # moves the turtle forward everytime by -100 pixels
        turtle.write(line4, font=("Verdana", 15, "normal")) # this writes numbers on window from 16-20

    turtle.goto(-340, 225)      # moves turtle's coordinate at (-340,225)
    for line5 in range(21, 26): # looping 5 times starting from 21 for writing numbers on the line
        turtle.penup()          # stops drawing
        turtle.forward(100)     # moves the turtle forward everytime by 100 pixels
        turtle.write(line5, font=("Verdana", 15, "normal"))  # this writes numbers on window from 20-25

def dice_rolling():                               # this function gets a random dice number and shows the appropriate dice number on the screen
    dice = turtle.Turtle(visible=False)           # defining a new turtle which has a starting property which is hidden
    dice.penup()                                  # stops drawing
    dice.goto(-290, 0)                            # moves turtle's coordinate at (-290,0)
    dice.showturtle()                             # shows turtle
    dice_num = random.randint(1, 6)               # gets random number and stores in dice num
    print("Your number is", dice_num)             # prints the dice num on the screen
    dice.shape("dice" + str(dice_num) + ".gif")   # change the shape of the dice according to the number obtained by the random function
    return dice_num                               # return dice number so it can be used later


def score(player1_name, player2_name, score_player1=0, score_player2=0):            # this function takes the player names and the scores
    # displaying names and scores on the turtle window
    turtle.pencolor("#FF6294")                                              # defining pen color for writing the below code
    turtle.goto(-90, 285)                                                          # moves turtle's coordinate at (-100,280)
    turtle.write(str(player1_name), align="center", font=("Verdana", 12, "bold"))   # this displays player 1 name on the turtle screen
    turtle.penup()                                                                  # stops drawing
    turtle.goto(-90, 260)                                                          # moves turtle's coordinate at (-100,260)
    turtle.write(str(score_player1), align="center", font=("Verdana", 12, "bold"))  # this displays score for player 1 on the turtle screen

    turtle.goto(100, 285)                                                           # moves turtle's coordinate at (100,280)
    turtle.write(str(player2_name), align="center", font=("Verdana", 12, "bold"))   # this displays player 2 name on the turtle screen
    turtle.penup()                                                                  # stops drawing
    turtle.goto(100, 260)                                                           # moves turtle's coordinate at (100,260)
    turtle.write(str(score_player2), align="center", font=("Verdana", 12, "bold"))  # this displays score for player 2 on the turtle screen

    vss = turtle.Turtle()  # vs logo
    vss.penup()            # stops drawing
    vss.shape("vss.gif")   # calling the shape which was added before in add_shapes()
    vss.goto(0, 285)       # moves turtle's coordinate at (0,285)


def up(animal, square_num):   # this function takes the character chosen and moves it a certain number of squares up according to square num obtained from calling function
    if square_num == 2:                   # if square number is equal to 2 then execute the following code
        animal.left(90)                   # makes the character turtle turn left by 90 degree
        animal.forward(100 * square_num)  # moves the character turtle forward by 100 pixels x square number
        animal.right(90)                  # makes the character turtle turn right by 90 degree
    elif animal.xcor() > 10:              # if first condition isn't true and characters x coordinate is greater than 10 then execute the following code
        animal.left(90)                   # makes the character turtle turn left by 90 degree
        animal.forward(100 * square_num)  # moves the character turtle forward by 100 pixels x square number
        animal.left(90)                   # makes the character turtle turn left by 90 degree
    else:                                 # if any of the above conditions aren't true then execute the following code
        animal.right(90)                  # makes the character turtle turn right by 90 degree
        animal.forward(100 * square_num)  # moves the character turtle forward by 100 pixels x square number
        animal.right(90)                  # makes the character turtle turn right by 90 degree


def down(animal, square_num):             # this function takes the character chosen and moves it a certain number of squares down according to square num obtained from calling function
    if animal.xcor() > 10:                # if characters x coordinate is greater than 10 then execute the following code
        animal.right(90)                  # makes the character turtle turn right by 90 degree
        animal.forward(100 * square_num)  # moves the character turtle forward by 100 pixels x square number
        animal.left(90)                   # makes the character turtle turn left by 90 degree
    else:                                 # else execute the following code
        animal.left(90)                   # makes the character turtle turn left by 90 degree
        animal.forward(100 * square_num)  # moves the character turtle forward by 100 pixels x square number
        animal.left(90)                   # makes the character turtle turn left by 90 degree


def forward(animal, square_num):         # this function takes the character chosen and moves it a certain number of squares forward according to square num obtained from calling function
    animal.forward(100 * square_num)     # moves the character turtle forward by 100 pixels x square number


def switch_turn(truth):                  # this function take a boolean and reverses it's value and returns it
    return not truth


def check_ladder(animal, animal_current_square_num, final_animal_position): # this function checks if there is any ladder and makes it go up by taking the character chosen and it's current and final position and it return the current and final position
    if animal_current_square_num == 5 and final_animal_position == 5:       # if character is on square 5 and final destination is square 5 then execute the following code
        up(animal, 2)                                                       # move character up 2 squares
        animal_current_square_num = final_animal_position = 15              # updating the characters current and final position which will be 15 in order to break the loop and end the turn in movement function
    elif animal_current_square_num == 9 and final_animal_position == 9:     # if first condition isn't true and character is on square 9 and final destination is square 9 then execute the following code
        up(animal, 1)                                                       # move character up 1 square
        animal_current_square_num = final_animal_position = 12              # updating the characters current and final position which will be 12 in order to break the loop and end the turn in movement function
    elif animal_current_square_num == 18 and final_animal_position == 18:   # if character is on square 18 and final destination is square 18 then execute the following code
        up(animal, 1)                                                       # move character up 1 square
        animal_current_square_num = final_animal_position = 23              # updating the characters current and final position which will be 23 in order to break the loop and end the turn in movement function
    return animal_current_square_num, final_animal_position                 # returns current and final position


def check_snake(animal, animal_current_square_num, final_animal_position):  # this function checks if there is any snake and makes it go down the snake by taking the character chosen and it's current and final position and it return the current and final position
    if animal_current_square_num == 8 and final_animal_position == 8:       # if character is on square 8 and final destination is square 8 then execute the following code
        down(animal, 1)                                                     # move character down 1 squares
        animal_current_square_num = final_animal_position = 3               # updating the characters current and final position which will be 3 in order to break the loop and end the turn in movement function
    elif animal_current_square_num == 20 and final_animal_position == 20:   # if first condition isn't true and character is on square 20 and final destination is square 20 then execute the following code
        down(animal, 3)                                                     # move character down 3 squares
        animal_current_square_num = final_animal_position = 1               # updating the characters current and final position which will be 1 in order to break the loop and end the turn in movement function
    elif animal_current_square_num == 24 and final_animal_position == 24:   # if character is on square 24 and final destination is square 24 then execute the following code
        down(animal, 2)                                                     # move character down 2 squares
        animal_current_square_num = final_animal_position = 14              # updating the characters current and final position which will be 14 in order to break the loop and end the turn in movement function
    return animal_current_square_num, final_animal_position                 # returns current and final position


def check_finish(animal, animal_current_square_num, final_animal_position, score_player): # this function checks if the player has reached the final square by taking the character chosen, it's current and final position and score player and it return the game not finished and score player
    game_not_finished = True                                                              # defining game not finished with an initial value true
    if animal_current_square_num == 25 and final_animal_position == 25:                   # if character is on square 25 and final destination is square 25 then execute the following code
        game_not_finished = False                                                         # setting the game not finished value to false
        score_player += 1                                                                 # incrementing score player
        win = turtle.Turtle()                                                             # defining a new turtle
        win.penup()                                                                       # stops drawing
        win.shape("win.gif")                                                              # adding shape on the screen
        return game_not_finished, score_player                                            # returns game not finished and score player
    return game_not_finished, score_player                                                # returns game not finished and score player

def reverse_direction(animal, animal_current_square_num, final_animal_position):          # this function checks if the character is gonna exceed the final square by moving the dice number and if it's gonna exceed the final square num then it reverses the character direction and update the final character position
    if final_animal_position > 25:                                                        # if characters final position is greater than 25 then execute the following code
        reverse_square_num = final_animal_position - 25                                   # defining the reverse square num variable which stores the number of square needed to go backwards
        forward_square_num = 25 - animal_current_square_num                               # defining the forward square num variable which stores the number of square needed to go forward before going backwards
        animal.forward(forward_square_num * 100)                                          #  moves the character turtle forward by 100 pixels x square number
        animal.left(180)                                                                  #  makes the character turtle turn left by 90 degree
        animal.forward(reverse_square_num * 100)                                          #  moves the character turtle forward by 100 pixels x square number
        animal.right(180)                                                                 #  makes the character turtle turn right by 90 degree
        animal_current_square_num = final_animal_position = 25 - reverse_square_num       # this updates the animal current square num by subtracting the number of squares needed to go backward (reverse square num) from the final square num (25)
        animal_current_square_num, final_animal_position = check_snake(animal, animal_current_square_num, final_animal_position)   # this calls the function check snake and checks if there any snake after going backwards
        return animal_current_square_num, final_animal_position                           # returns current and final position
    return animal_current_square_num, final_animal_position                               # returns current and final position


def animal_next_position(animal, corner_points, current_animal_square_num, final_animal_position, score_player, game_not_finished):  # this function keeps moving the character a square at a time till it reaches the final position
    while current_animal_square_num != final_animal_position:  # while we didn't reach final character position yet then execute the following code
        if current_animal_square_num == 5 and final_animal_position == 5:  # if character is on square 5 and final destination is square 5
            current_animal_square_num, final_animal_position = check_ladder(animal, current_animal_square_num, final_animal_position) # this calls the function check ladder and checks if there any ladder
            current_animal_square_num, final_animal_position = check_snake(animal, current_animal_square_num, final_animal_position)  # this calls the function check snake and checks if there any snake
            game_not_finished, score_player = check_finish(animal, current_animal_square_num, final_animal_position, score_player)    # this calls the function check finish and checks if character has reached the final square
            current_animal_square_num, final_animal_position = reverse_direction(animal, current_animal_square_num, final_animal_position)   # this calls the function reverse direction and checks if character needs to go reverse if exceeding the final position (final square)
        elif current_animal_square_num in corner_points:            # if the first condition isn't true and character current position is any defined in corner points [5,10,15,20] then execute the following code
            up(animal, 1)                                           # move character up 2 squares
            current_animal_square_num += 1                          # incrementing character current position
        else:                                                       # if any of the above conditions aren't true then execute the following code
            forward(animal, 1)                                      # move character up 2 squares
            current_animal_square_num += 1                          # incrementing character current position
            current_animal_square_num, final_animal_position = check_ladder(animal, current_animal_square_num, final_animal_position)       # this calls the function check ladder and checks if there any ladder
            current_animal_square_num, final_animal_position = check_snake(animal, current_animal_square_num, final_animal_position)        # this calls the function check snake and checks if there any snake
            game_not_finished, score_player = check_finish(animal, current_animal_square_num, final_animal_position, score_player)          # this calls the function check finish and checks if character has reached the final square
            current_animal_square_num, final_animal_position = reverse_direction(animal, current_animal_square_num, final_animal_position)  # this calls the function reverse direction and checks if character needs to go reverse if exceeding the final position (final square)
    return current_animal_square_num, final_animal_position, score_player, game_not_finished                                                # returns current and final position, the score player and game not finished


def movement(character_1, character_2, score_player1, score_player2, player1_name, player2_name):  # this function keeps moving the players alternatively until the game finishes and it updates the winner score
    print("\nNew Game!\n")                 # prints new game on the screen
    character_1.penup()                    # stops drawing
    character_1.goto(-190, -175)           # moves turtle's coordinate at (-190,-175)
    character_2.penup()                    # stops drawing
    character_2.goto(-220, -220)           # moves turtle's coordinate at (-220,-220)
    character1 = character_1.clone()       # cloning character_1 with all it's properties to a new turtle called character 1
    character2 = character_2.clone()       # cloning character_2 with all it's properties to a new turtle called character 2
    character1.showturtle()                # shows turtle
    character2.showturtle()                # shows turtle
    character1.speed(1)                    # speed of the movement (1 is the slowest)
    character2.speed(1)                    # speed of the movement (1 is the slowest)
    corner_points = [5, 10, 15, 20]        # defining the corner points
    truth = True                           # setting truth equal true
    current_character1_square_num = 1      # pre defining current character 1 square num is equal to 1
    current_character2_square_num = 1      # pre defining current character 2 square num is equal to 1
    game_not_finished = True               # setting the game not finished value to true
    while game_not_finished == True:       # while game not finished is equal to true then execute the following code
        if truth == True:                  # if truth is equal to true
            input(player1_name + ": Press enter to roll the dice")   # waiting for user to press enter
            dice_num = dice_rolling()                                # calling the function dice rolling and storing the random number returned in dice num
            final_character1_position = dice_num + current_character1_square_num  # defining the final character 1 position which adds the dice number and it's current position
            current_character1_square_num, final_character1_position, score_player1, game_not_finished = animal_next_position(character1, corner_points, current_character1_square_num, final_character1_position, score_player1, game_not_finished)  # calling the function animal next position
            print(player1_name + " current square number is " + str(current_character1_square_num) + "\n") # prints the current square num on the screen
            truth = switch_turn(truth)                                                               # calling the function switch turn and switching the turn
        else:                                                        # if the first condition isn't true then execute the following code
            input(player2_name + ": Press enter to roll the dice")   # waiting for user to press enter
            dice_num = dice_rolling()                                # calling the function dice rolling and storing the random number returned in dice num
            final_character2_position = dice_num + current_character2_square_num  # defining the final character 1 position which adds the dice number and it's current position
            current_character2_square_num, final_character2_position, score_player2, game_not_finished = animal_next_position(character2, corner_points, current_character2_square_num, final_character2_position, score_player2, game_not_finished) # calling the function animal next position
            print(player2_name + " current square number is " + str(current_character2_square_num) + "\n")  # prints the current square num on the screen
            truth = switch_turn(truth)                                                               # calling the function switch turn and switching the turn
    return score_player1, score_player2                                                              # returns score player for both the players


def another_game_option():                                                            # this function asks the user if he wants to play another game
    ask = turtle.Turtle(visible=False)                                                # defining a new turtle which has a starting property which is hidden
    ask.penup()                                                                       # stops drawing
    ask.goto(0, 280)                                                                  # moves turtle's coordinate at (0,280)
    ask.write("Play another game?", align="center", font=("Verdana", 15, "bold"))     # this writes on the turtle window
    ask.penup()                                                                       # stops drawing
    ask.goto(-5, 240)                                                                  # moves turtle's coordinate at (0,240)
    ask.write("Yes          No ", align="center", font=("Verdana", 15, "bold"))  # this writes on the turtle window
    answer = "jdhisj"                                                                 # pre-defining the variable answer before asking the user for his answer
    while answer not in ["1", "0"]:                                                   # while answer is not 1 or 0 then execute the following code
        print("\nEnter 1 for Yes & 0 for No")
        answer = input("Enter your Answer: ")                                         # asking the user to input his answer
        if answer == "1":                                                             # if answer is equal to 1 then execute the following code
            return True                                                               # returns true and the game is played again
        elif answer == "0":                                                           # if the first condition isn't true and answer is equal to 0 then execute the following code
            print("Game Finished")                                                    # prints Game finished on the screen
            return False                                                              # returns false and the game finishes
        else:                                                                         # if all the above conditions aren't true then execute the following code
            print("Please enter a valid number")                                      # prints enter a valid number on the screen

def show_screen3(player1_name, player2_name, score_player1, score_player2):           # this function is responsible for showing the board, numbers, images and score
    turtle.clear()                                                                    # this clears text and drawings
    setup()                                                                           # calling the function to setup the turtle window
    draw_board()                                                                      # calling the function for drawing board
    write_numbers()                                                                   # calling the function for writing numbers on the board
    score(player1_name, player2_name, score_player1, score_player2)                   # calling the function for score

    # adds images on the board
    snake = turtle.Turtle(shape="snake.gif")      # defining a new turtle and adding shape on the screen
    snake.penup()                                 # stops drawing
    snake.goto(100, 100)                          # moves turtle's coordinate at (100,100)

    snake2 = turtle.Turtle(shape="snake2.gif")    # defining a new turtle and adding shape on the screen
    snake2.penup()                                # stops drawing
    snake2.goto(0, -150)                          # moves turtle's coordinate at (0,-150)

    snake3 = turtle.Turtle(shape="snake3.gif")    # defining a new turtle and adding shape on the screen
    snake3.penup()                                # stops drawing
    snake3.goto(-200, -50)                        # moves turtle's coordinate at (-200,-50)

    ladder = turtle.Turtle(shape="ladder.gif")    # defining a new turtle and adding shape on the screen
    ladder.penup()                                # stops drawing
    ladder.goto(-100, -50)                        # moves turtle's coordinate at (-100,-50)

    ladder2 = turtle.Turtle(shape="ladder2.gif")  # defining a new turtle and adding shape on the screen
    ladder2.penup()                               # stops drawing
    ladder2.goto(0, 150)                          # moves turtle's coordinate at (0,150)

    ladder3 = turtle.Turtle(shape="ladder3.gif")  # defining a new turtle and adding shape on the screen
    ladder3.penup()                               # stops drawing
    ladder3.goto(200, -100)                       # moves turtle's coordinate at (200,-100)

def main():                  # this function is the main function responsible for getting all parts of the program together
    add_shapes()             # calling the function to add shapes
    another_game = True      # another_game is True
    score_player1 = 0        # the score by default will be 0
    score_player2 = 0        # the score by default is 0
    player1_name, player2_name = show_screen1()  # calling the function screen 1 and taking the player names from it
    while another_game:                          # while another game boolean is true then execute
        character1, character2 = show_screen2(player1_name, player2_name)      # calling the function screen 2 and taking the character turtles from it
        show_screen3(player1_name, player2_name, score_player1, score_player2) # calling the function screen 3
        score_player1, score_player2 = movement(character1, character2, score_player1, score_player2, player1_name, player2_name) # calling the function movement and updating the scores of the players
        another_game = another_game_option()    # asking the user if he wants to play another game through another game option function and updating the another game boolean accordingly
main()                                          # calling the function main
