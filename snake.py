#SNAKE GAME - Kripesh Ranabhat
#A normal snake game where you can move the snake with your arrow keys
#The snake grows as you eat more food and there is a score counter
#on screen that keeps track of your score

import turtle
import random

turtle.tracer(1,0) #helps turtle move more smoothly

SIZE_X = 800
SIZE_Y = 600
turtle.setup(SIZE_X,SIZE_Y) #Turtle window size

turtle.penup()
turtle.bgcolor("Medium Aquamarine")

SQUARE_SIZE = 20
START_LENGTH = 10
TIME_STEP = 100

BORDER_X = 400
BORDER_Y = 300

SCORE = 0

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
COLORS = ["Turquoise", "Cadet Blue", "Khaki", "Dark Goldenrod", "Medium Purple", "Tomato", "Firebrick", "Sienna", "Medium Blue", "Black", "Dark Slate Gray", "Dim Gray"]

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object
turtle.hideturtle()

#Function to draw the border
def border():
    turtle.goto(BORDER_X,BORDER_Y)
    turtle.pendown()
    turtle.goto(-BORDER_X,BORDER_Y)
    turtle.goto(-BORDER_X,-BORDER_Y)
    turtle.goto(BORDER_X,-BORDER_Y)
    turtle.goto(BORDER_X,BORDER_Y)
    turtle.penup()
    turtle.hideturtle()

border()
#Function to keep write a welcome message!
def welcome():
    turtle.goto(0,BORDER_Y)
    turtle.write("Welcome to the Snake Game!", False, align = "center", font = "Verdana")

welcome()

def score():
    turtle.undo()
    turtle.goto(0,-BORDER_Y)
    turtle.write("SCORE:"+str(SCORE), False, align = "center", font = "Verdana")

score()

#Function to draw a part of the snake on screen
def new_stamp():
    snake_pos = snake.pos() #Get snake's position
    #Append the position tuple to pos_list
    pos_list.append(snake_pos)
    snkstamp = snake.stamp()
    #append the stamp ID to stamp_list
    stamp_list.append(snkstamp)

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e START_LENGTH)
for i in range(START_LENGTH):
    x_pos = snake.pos()[0]
    y_pos = snake.pos()[1]

    x_pos+=SQUARE_SIZE
    
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)

    new_stamp()

def remove_tail():
    old_stamp = stamp_list.pop(0)   #last piece of tail
    snake.clearstamp(old_stamp) #erase last piece of tail
    pos_list.pop(0) #remove last piece of tail's position

snake.direction = "Up"

def up():
    snake.direction = "Up"  #Changes direction to Up
    #move_snake()    #Update the snake drawing
    print("You pressed the up key!")

def down():
    snake.direction = "Down"  #Changes direction to Down
    #move_snake()    #Update the snake drawing
    print("You pressed the down key!")

def right():
    snake.direction = "Right"  #Changes direction to Right
    #move_snake()    #Update the snake drawing
    print("You pressed the right key!")

def left():
    snake.direction = "Left"  #Changes direction to Left
    #move_snake()    #Update the snake drawing
    print("You pressed the left key!")

#Create listeners for up,down,left,right keys
turtle.onkeypress(up,"Up")  
turtle.onkeypress(down,"Down")
turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")

turtle.listen()

turtle.register_shape("trash.gif")  #Add trash picture
food = turtle.clone()
food.shape("trash.gif")

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

for this_food_pos in food_pos:
    food.goto(this_food_pos)
    stamp1 = food.stamp()
    food_stamps.append(stamp1)

food.hideturtle()

def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(BORDER_X/SQUARE_SIZE)+1
    max_x=int(BORDER_X/2/SQUARE_SIZE)-1
    min_y=-int(BORDER_Y/2/SQUARE_SIZE)+1
    max_y=int(BORDER_Y/2/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

    food.goto(food_x,food_y)
    foodstamp = food.stamp()
    food_pos.append(food.pos())
    food_stamps.append(foodstamp)

def move_snake():
    global SCORE
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if snake.direction == "Up":
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print("You moved up!")

    elif snake.direction == "Down":
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
        print("You moved down!")

    elif snake.direction == "Right":
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
        print("You moved right!")

    elif snake.direction == "Left":
        snake.goto(x_pos-SQUARE_SIZE,y_pos)
        print("You moved left!")

    new_stamp()

    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_index = food_pos.index(snake.pos())    #stores the index of the stamp that needs to be removed 
        food.clearstamp(food_stamps[food_index])    #Remove eaten food stamp
        food_pos.pop(food_index)    #Remove eaten food positon from the list
        food_stamps.pop(food_index) #Remove eaten food stamp from the list
        print("You have eaten the food!")
        snake.color(random.choice(COLORS))
        SCORE +=1
        score()

    else:
        remove_tail()

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= BORDER_X:
        print("You hit the right edge! Game over!")
        quit()

    elif new_x_pos <= -BORDER_X:
        print("You hit the left edge! Game over!")
        quit()

    elif new_y_pos >= BORDER_Y:
        print("You hit the up edge! Game over!")
        quit()

    elif new_y_pos <= -BORDER_Y:
        print("You hit the down edge! Game over!")
        quit()

    if len(food_stamps) <= 6:
        make_food()

    if snake.pos() in pos_list[:-1]:
        print("You have eaten yourself!")
        quit()
    
    turtle.ontimer(move_snake, TIME_STEP)

move_snake()









turtle.mainloop()
