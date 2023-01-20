import pygame
import numpy

from pygame.constants import  QUIT

pygame.init()

# screen size
screen = width, height = 800, 600
print(screen)
BLACK = 0,0,0
WHITE = 255,255,255

# call module
main_surface = pygame.display.set_mode(screen) # call window with fixed size

ball = pygame.Surface((20,20)) # create element with size (20,20)
ball.fill((WHITE)) # fill ball with a colour
ball_rect = ball.get_rect() # starting coordinates
print(ball_rect)
ball_speed = [1,1]

# create while cycle for working with pygame
is_working = True
while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    ball_rect = ball_rect.move(ball_speed) # ball_speed = [1,1] changes +1,+1

    # add left and top right merge
    if ball_rect.left <= 0 or ball_rect.right >=width:
        ball_speed[0] = -ball_speed[0]
        ball.fill(tuple(numpy.random.randint(0, 255, (3))))  # change bal`s colour accidentaly
    # end add left and top right merge

    # add bottom and top merge
    if ball_rect.bottom >=height or ball_rect.top <=0:
        ball_speed[1] = -ball_speed[1]
        ball.fill(tuple(numpy.random.randint(0, 255, (3))))  # change bal`s colour accidentaly
    # end add bottom merge

    main_surface.fill((BLACK)) # fill with black
    # main_surface.blit(ball,(100,100)) # add element into the screen with it's coordinates (100*100)
    main_surface.blit(ball,ball_rect) # add element into the screen with it's starting coordinates
    # main_surface.fill((155,155,155)) # fill with colour
    pygame.display.flip() # flip() is used for updating changes