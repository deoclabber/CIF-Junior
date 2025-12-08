import pygame
pygame.init()

green = (50, 255, 75)
pink = (255, 100, 200)
black = (0, 0, 0)

width = 800
height = 600
box1_x = 0
box1_y = 50
box2_x = 800
box2_y = 500

rect1 = pygame.Rect(box1_x, box1_y, 50, 50)
rect2 = pygame.Rect(box2_x, box2_y, 50, 50)
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if box1_x < 0:
        box1_x = 0 
    if box1_x > width - 50:
        box1_x = width - 50
    if box1_y < 0:
        box1_y = 0 
    if box1_y > height - 50:
        box1_y = height - 50
    
    if box2_x < 0:
        box2_x = 0 
    if box2_x > width - 50:
        box2_x = width - 50
    if box2_y < 0:
        box2_y = 0 
    if box2_y > height - 50:
        box2_y = height - 50
        
    rect1 = pygame.Rect(box1_x, box1_y, 50, 50)

    box1_x += 5
    box2_x -= 5
    rect1 = pygame.Rect(box1_x, box1_y, 50, 50)
    rect2 = pygame.Rect(box2_x, box2_y, 50, 50)

    pygame.draw.rect(screen, green, rect1)
    pygame.draw.rect(screen, pink, rect2)
    pygame.display.update()
    screen.fill(black)