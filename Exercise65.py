import random

print("Welcome to the hurdles challange")

def turn_left():
    print("Turning left")

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move():
    print("Moving>>")


def jump():
   print("Jumping")

at_goal = 0
wall_is_infront = 1
front_is_clear = 2

random_hurdle = random.randint(0, 10)

while not at_goal:
  
    if(wall_is_infront == 1 ):
        while (random_hurdle > 0):

          jump()
    else:
        move()

        