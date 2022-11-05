import pygame
import time
import random


snake_speed = 15

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

xsize = 720  # velicina prozora po x
ysize = 480  # velicina prozora po y

# inicijalizacija prozora
game_window = pygame.display.set_mode((xsize, ysize))

# FPS
fps = pygame.time.Clock()

# pocetna pozicija zmije
snake_position = [100, 50]
 
# prva 4 bloka zmije
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# pozicija hrane
food_pos = [random.randrange(1, (xsize//10)) * 10,
                  random.randrange(1, (ysize//10)) * 10]
 
food_spawn = True

# pocetni smjer kretanja postavljamo na desno
direction = 'RIGHT'
change_to = direction
 
# initial score
# score = 0

def game_over():
   
    # after 2 seconds we will quit the program
    time.sleep(2)
     
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()
 

while True:
     
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_pos[0] and snake_position[1] == food_pos[1]:
        # score += 10
        food_spawn = False
    else:
        # ako se nismo sudarili sa hranom, obrisi zadnji kvadrat
        snake_body.pop()
         
    if not food_spawn:
        food_pos = [random.randrange(1, (xsize//10)) * 10,
                          random.randrange(1, (ysize//10)) * 10]
         
    food_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))
 
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > xsize-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > ysize-10:
        game_over()
 
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()        
 
    # displaying score countinuously
    # show_score(1, white, 'times new roman', 20)
 
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)