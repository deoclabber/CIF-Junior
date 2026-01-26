import pygame
pygame.init()

#Colors
green = (70, 180, 80)
red = (255, 50, 50)
yellow = (255, 233, 0)
black = (0, 0, 0)
white = (255, 255, 255)

#Setup
#Screen
width = 900
height = 900
#Fonts
my_font = pygame.font.SysFont("helvetica", 30) #Gamemode
my_font2 = pygame.font.SysFont("times new roman", 25) #Start & goal
text_surface2 = my_font2.render("Start", True, (10, 70, 10))
my_font3 = pygame.font.SysFont("arial", 60) #Win
text_surface3 = my_font3.render("You Escaped!", True, (0, 0, 0))
my_font4 = pygame.font.SysFont("arial", 30) #Fail
text_surface4 = my_font4.render("Failed...", True, (255, 75, 75))
my_font5 = pygame.font.SysFont("arial", 100) #Main menu
text_surface5 = my_font2.render("Goal", True, (255, 75, 75))
my_font6 = pygame.font.SysFont("arial", 40) #Main menu
text_surface6 = my_font5.render("MAZE Escapists!", True, (0, 0, 0))
text_surface7 = my_font6.render("Press any key to start...", True, (0, 0, 0))
#Player movement
player_x = 15 
player_y = 100
player_x_change = 0
player_y_change = 0
player_speed = 10
#Enemy movement
enemy_y = 60
enemy_y_change = 7
enemy_y2 = 600
enemy_y2_change = 10
enemy_y3 = 0
enemy_y3_change = 7
#Walls
wall1 = pygame.Rect(60, 60, 30, 390)
wall2 = pygame.Rect(60, 420, 180, 30)
wall3 = pygame.Rect(0, 510, 330, 30)
wall4 = pygame.Rect(330, 150, 30, 390)
wall5 = pygame.Rect(60, 60, 300, 30)
wall6 = pygame.Rect(180, 330, 180, 30)
wall7 = pygame.Rect(90, 240, 150, 30)
wall8 = pygame.Rect(180, 150, 180, 30)
wall9 = pygame.Rect(420, 0, 30, 630)
wall10 = pygame.Rect(330, 0, 30, 60)
wall11 = pygame.Rect(90, 600, 600, 30)
wall12 = pygame.Rect(60, 600, 30, 210)
wall13 = pygame.Rect(420, 720, 30, 180)
wall14 = pygame.Rect(150, 720, 210, 30)
wall15 = pygame.Rect(690, 450, 210, 30)
wall16 = pygame.Rect(420, 300, 270, 30)
wall17 = pygame.Rect(690, 150, 210, 30)
wall18 = pygame.Rect(660, 600, 30, 180)
wall_list = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18]
#Goal
goal = pygame.Rect(810, 30, 60, 60)

#Tutorial
turtorial = str(input("Would you like to see the turtorial? (Yes/No)\n")).lower()
if turtorial == "yes":
    print("Use the arrow keys or WASD to move the player (green square).\n\nAvoid the enemies (red squares) and navigate through the walls (black rectangles).\n\nYour objective is to reach the goal (yellow square) at the top-right corner of the maze. You can choose the speeds of the enemies and even specate the maze!\n")
#Set player and enemy speeds
player_speed = float(input("Enter the speed of the player. (10-15) (10 recommended)\n"))
if player_speed < 10:
    player_speed = 10
elif player_speed > 15:
    player_speed = 15
enemy_y_change = float(input("Enter the speed of the top-left enemies. (7-20) (15 recommended)\n"))
if enemy_y_change < 7:
    enemy_y_change = 7
elif enemy_y_change > 20:
    enemy_y_change = 20
enemy_y2_change = float(input("Enter the speed of the bottom-left enemies. (7-15) (12 recommended)\n"))
if enemy_y2_change < 7:
    enemy_y2_change = 7
elif enemy_y2_change > 15:
    enemy_y2_change = 15
enemy_y3_change = float(input("Enter the speed of the bottom-right enemies. (7-15) (10 recommended)\n"))
if enemy_y3_change < 7:
    enemy_y3_change = 7
elif enemy_y3_change > 15:
    enemy_y3_change = 15

spectator_mode = str(input("Would you like to enable spectator mode? (Yes/No) There will be no collision in spectator mode.\n")).lower()
start = False
if spectator_mode == "yes":
    spectator_mode = True
else:
    spectator_mode = False
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
if spectator_mode == True:
    text_surface = my_font.render("You are spectating now...", True, (0, 0, 0))
else:
    text_surface = my_font.render("Escape the maze!", True, (0, 0, 0))

#Game loop
runtime = True
while runtime:

    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime = False
            start = False

    #Main menu
    if start == False:
        screen.fill(white)
        screen.blit(text_surface6, (150, 250))
        screen.blit(text_surface7, (150, 400))
        pygame.display.update()
        keys1 = pygame.key.get_pressed()
        mouse1 = pygame.mouse.get_pressed()
        if any(keys1) or any(mouse1):
            start = True

    #Player movement
    if start == True:
        player_x_change = 0
        player_y_change = 0
        keys2 = pygame.key.get_pressed()

        if keys2[pygame.K_LEFT] or keys2[pygame.K_a]:
            player_x_change = -player_speed
        if keys2[pygame.K_RIGHT] or keys2[pygame.K_d]:
            player_x_change = player_speed

        if keys2[pygame.K_UP] or keys2[pygame.K_w]:
            player_y_change = -player_speed

        if keys2[pygame.K_DOWN] or keys2[pygame.K_s]:
            player_y_change = player_speed

        if player_x < 0:
            player_x = 0 
        if player_x > width - 30:
            player_x = width - 30
        if player_y < 0:
            player_y = 0 
        if player_y > height - 30:
            player_y = height - 30

        #Draw screen and goal and walls and enemies
        screen.fill(white)
        screen.blit(text_surface, (20, 10))
        screen.blit(text_surface2, (5, 60))

        pygame.draw.rect(screen, yellow, goal)
        screen.blit(text_surface5, (815, 45))

        for wall in wall_list:
            pygame.draw.rect(screen, black, wall)

        player = pygame.Rect(player_x, player_y, 30, 30)

        if player.colliderect(goal):
            screen.blit(text_surface3, (520, 355))
            pygame.display.update()
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        waiting = False
                        runtime = False
                        pygame.quit()
                        exit()

        #First set of enemies
        enemy1 = pygame.Rect(90, enemy_y, 30, 30)
        enemy2 = pygame.Rect(165, enemy_y, 90, 30)
        enemy3 = pygame.Rect(300, enemy_y, 30, 30)

        enemy_list = [enemy1, enemy2, enemy3]

        for enemy in enemy_list:
            pygame.draw.rect(screen, red, enemy)

        enemy_y += enemy_y_change

        if enemy_y >= 510:
            enemy_y = 510
            enemy_y_change = -enemy_y_change
        elif enemy_y <= 60:
            enemy_y = 60
            enemy_y_change = -enemy_y_change

        #Second set of enemies    
        enemy4 = pygame.Rect(90, enemy_y2, 60, 30)
        enemy5 = pygame.Rect(210, enemy_y2, 30, 30)
        enemy6 = pygame.Rect(270, enemy_y2, 30, 30)
        enemy7 = pygame.Rect(360, enemy_y2, 60, 30)

        enemy_list2 = [enemy4, enemy5, enemy6, enemy7]

        for enemy in enemy_list2:
            pygame.draw.rect(screen, red, enemy)
        
        enemy_y2 += enemy_y2_change

        if enemy_y2 >= height - 30:
            enemy_y2 = height - 30
            enemy_y2_change = -enemy_y2_change
        elif enemy_y2 <= 600:
            enemy_y2 = 600
            enemy_y2_change = -enemy_y2_change
        
        #Third set of enemies
        enemy8 = pygame.Rect(480, enemy_y3, 30, 30)
        enemy9 = pygame.Rect(570, enemy_y3, 30, 30)
        enemy10 = pygame.Rect(660, enemy_y3, 30, 30)
        enemy11 = pygame.Rect(750, enemy_y3, 30, 30)
        enemy12 = pygame.Rect(840, enemy_y3, 30, 30)
        enemy13 = pygame.Rect(480 + 45, enemy_y3 + 300, 30, 30)
        enemy14 = pygame.Rect(570 + 45, enemy_y3 + 300, 30, 30)
        enemy15 = pygame.Rect(660 + 45, enemy_y3 + 300, 30, 30)
        enemy16 = pygame.Rect(750 + 45, enemy_y3 + 300, 30, 30)
        enemy17 = pygame.Rect(840 + 45, enemy_y3 + 300, 30, 30)
        enemy_list3 = [enemy8, enemy9, enemy10, enemy11, enemy12, enemy13, enemy14, enemy15, enemy16, enemy17]

        for enemy in enemy_list3:
            pygame.draw.rect(screen, red, enemy)
        
        enemy_y3 += enemy_y3_change

        bottom_limit = 300 + 30
        if enemy_y3 + bottom_limit >= 900:
            enemy_y3 = 900 - bottom_limit
            enemy_y3_change = -enemy_y3_change
        elif enemy_y3 <= 0:
            enemy_y3 = 0
            enemy_y3_change = -enemy_y3_change

        #Draw player

        #Enemy collision
        if spectator_mode == False:    
            for enemy in enemy_list + enemy_list2 + enemy_list3:
                if player.colliderect(enemy):
                    screen.blit(text_surface4, (230, 10))
                    player_x = 15
                    player_y = 100
                    pygame.display.update()
                    waiting = True
                    while waiting:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                waiting = False
                                runtime = False
                                pygame.quit()
                                exit()
                            if event.type == pygame.KEYDOWN:
                                waiting = False
            
        #Wall collision
        if spectator_mode == False: 
            player_x += player_x_change
            player = pygame.Rect(player_x, player_y, 30, 30)
            for wall in wall_list:
                if player.colliderect(wall):
                    if player_x_change > 0:
                        player_x = wall.left - 30
                    if player_x_change < 0:
                        player_x = wall.right
                    break
            
            player_y += player_y_change
            player = pygame.Rect(player_x, player_y, 30, 30)
            for wall in wall_list:
                if player.colliderect(wall):
                    if player_y_change > 0:
                        player_y = wall.top - 30
                    if player_y_change < 0:
                        player_y = wall.bottom  
                    break
        else:
            player_x += player_x_change
            player_y += player_y_change
        player = pygame.Rect(player_x, player_y, 30, 30)
        pygame.draw.rect(screen, green, player)   
    pygame.display.update()