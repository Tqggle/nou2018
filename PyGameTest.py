import pygame 
import time
#---Variables---#
screensize = [1000,700]
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)
red = (255,0,0)
teal = (39,229,162)
paddlesize = (100,40)
paddlex=screensize[0]/2
paddley=screensize[1]-100
#---End of Variables---#
pygame.init()
screen = pygame.display.set_mode((screensize[0],screensize[1]))
pygame.display.set_caption("Greatness")
clock = pygame.time.Clock()
screen.fill(teal)
pygame.display.update()

close = False
while not close: #game loop
    for event in pygame.event.get(): #event handling loop
        print(event)
        if event.type == pygame.QUIT:
            close = True
            
        pygame.draw.rect(screen,white,(paddlex,paddley,paddlesize[0],paddlesize[1]))    
        pygame.display.update()
        clock.tick(60)
pygame.quit()