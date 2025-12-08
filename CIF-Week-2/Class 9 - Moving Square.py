import pygame
pygame.init()

yellow = (200, 200, 0)
space = (0, 0, 20)

width = 1000
height = 800
box1_x = 0
box1_y = 100
box1_x_change = 0
box1_y_change = 0
box1_speed = 7

rect1 = pygame.Rect(box1_x, box1_y, 30, 30)
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                box1_y_change = -box1_speed
            if event.key == pygame.K_a:
                box1_x_change = -box1_speed
            if event.key == pygame.K_s:
                box1_y_change = box1_speed
            if event.key == pygame.K_d:
                box1_x_change = box1_speed
        elif event.type == pygame.KEYUP:
            box1_x_change = 0
            box1_y_change = 0

    box1_x += box1_x_change
    box1_y += box1_y_change

    if box1_x < 0:
        box1_x = 0 
    if box1_x > width - 50:
        box1_x = width - 50
    if box1_y < 0:
        box1_y = 0 
    if box1_y > height - 50:
        box1_y = height - 50
        
    rect1 = pygame.Rect(box1_x, box1_y, 50, 50)

    pygame.draw.rect(screen, yellow, rect1)
    pygame.display.update()
    screen.fill(space)