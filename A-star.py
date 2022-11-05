from Node import Node
from Snake import Snake
from queue import PriorityQueue
import pygame
import random
import time

def game_over():
   
    # after 2 seconds we will quit the program
    time.sleep(2)
     
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()

def contains(closed_list, tuples):
    for x in closed_list:
        for i in range(0, len(tuples)):
            if x == tuples[i]:
                return True
    
    return False

def astar(game):

    global food_pos
    global new_state
    global new_pos
    global score

    open_list = PriorityQueue()
    closed_list = set(())
    open_list.put(Node(game.body, game.position))

    node = open_list.get()
    
    # moram da napravim praznu listu, u nju stavim torke, zatim od te liste napravim torku
    state_tuples = [tuple(x) for x in node.state]

    closed_list.add(tuple(state_tuples))

    if game.goal_test(node.position):
        food_pos = [random.randrange(1, (xsize//10)) * 10, random.randrange(1, (ysize//10)) * 10]
        game.food_pos = food_pos
        score += 1

    for child_node in node.expand(game):
        new_tuple = [tuple(x) for x in node.state]
        if not contains(closed_list, tuple(new_tuple)):
            open_list.put(child_node)

    node = open_list.get()
    new_state = node.state
    new_pos = node.position

snake_speed = 50

score = 0

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

xsize = 720  # velicina prozora po x
ysize = 480  # velicina prozora po y

game_window = pygame.display.set_mode((xsize, ysize))

# FPS
fps = pygame.time.Clock()

# pocetna pozicija zmije
snake_position = [100, 50]
 
# prva 2 bloka zmije
snake_body = [[100, 50],
              [90, 50]]

# pozicija hrane
food_pos = [random.randrange(1, (xsize//10)) * 10,
                 random.randrange(1, (ysize//10)) * 10]
# food_pos = [120,100]
# pocetni smjer kretanja postavljamo na desno
# direction = 'RIGHT'

snake = Snake(snake_position, snake_body, food_pos)

while True:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()


    astar(snake)

    snake.body = new_state.copy()
    snake.position = new_pos.copy()

    game_window.fill(black)
    i = 0
    for joint in snake.body:
        if i == 0:
            pygame.draw.rect(game_window, red, pygame.Rect(joint[0], joint[1], 10, 10))
            i += 1
        else:
            pygame.draw.rect(game_window, green, pygame.Rect(joint[0], joint[1], 10, 10))
    
    pygame.draw.rect(game_window, white, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))

    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
    print(score)
