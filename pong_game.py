import pygame,sys,time,random
pygame.init()
pygame.font.init()
Win_x = 900
Win_y = 600
text_x = 250
text_y = 250
colour_x = random.randint(0,255)
colour_y = random.randint(0,255)
colour_z = random.randint(0,255)
random_colour_tuple = (colour_x,colour_y,colour_z)
Win_width_height = (Win_x,Win_y)
screen = pygame.display.set_mode(Win_width_height)
pygame.display.set_caption("Pong")
Player_movement_vel = 5
Ball = pygame.image.load("Attack.png")
Ball = pygame.transform.scale(Ball,(50,50))
Ball_rect = Ball.get_rect()
Ball_rect.center = (450,300)
global Delta_ball_x,Delta_ball_y
Delta_ball_x = 0
Delta_ball_y = 0
font = pygame.font.SysFont("pygame.font.get_default_font()",100)
Text_player1_lost = font.render("Unni Won!",False,(0,0,0))
Text_player2_lost = font.render("Unni Won!",False,(0,0,0))
Ball_movement_vel = 5
Ball_state = "idk"
Blank_screen_rect = pygame.Rect(0,0,900,600)
Player1_rect = pygame.Rect(450,50,150,15) # top player
Player1_state = "ready"
Player2_rect = pygame.Rect(450,550,150,15) # bottom player
Player2_state = "ready"
Player1_quadrant1_right = False
Player1_quadrant2_right = False
Player2_quadrant3_right = False
Player2_quadrant4_right = False
right_wall_top_right = False
right_wall_bottom_right = False
left_wall_top_right = False
left_wall_bottom_right = False
running = True
clock = pygame.time.Clock()
while running:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),Player1_rect)
    pygame.draw.rect(screen,(255,255,255),Player2_rect)
    screen.blit(Ball,Ball_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False and pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            # bottom player
            if event.key == pygame.K_LEFT and event.key != pygame.K_RIGHT : #left
                Player1_state = "left"
            if event.key == pygame.K_RIGHT and event.key != pygame.K_LEFT: #right
                Player1_state = "right"
            # top player
            if event.key == pygame.K_a and event.key != pygame.K_d: #left
                Player2_state = "left"
            if event.key == pygame.K_d and event.key != pygame.K_a: #right
                Player2_state = "right"

        if event.type == pygame.KEYUP:
            # bottom player
            if event.key == pygame.K_LEFT: #left
                Player1_state = "ready"
            if event.key == pygame.K_RIGHT: #right
                Player1_state = "ready"
            # top player
            if event.key == pygame.K_a: #left
                Player2_state = "ready"
            if event.key == pygame.K_d: #right
                Player2_state = "ready"

    if Player1_state == "left" and Player1_rect.x - Player_movement_vel > 5:
        Player1_rect.x -= Player_movement_vel
    if Player1_state == "right" and Player1_rect.x + Player_movement_vel < 750:
        Player1_rect.x += Player_movement_vel
    if Player2_state == "left" and Player2_rect.x - Player_movement_vel > 5 :
        Player2_rect.x -= Player_movement_vel
    if Player2_state == "right" and Player2_rect.x + Player_movement_vel < 750:
        Player2_rect.x += Player_movement_vel

    if Ball_state =="idk":
        Delta_ball_y = -8
        Delta_ball_x = 0
    if Ball_rect.x > 850: # right wall
        if Ball_rect.y > screen.get_height()//2 : # right wall top
            if right_wall_top_right == False:
                Ball_movement_vel =  Ball_movement_vel 
                Delta_ball_x = -8
                Delta_ball_y = -8
                Ball_state = "haha" # help
            else:
                Ball_movement_vel =  Ball_movement_vel 
                Delta_ball_x = -8
                Delta_ball_y = 0
                Ball_state = "haha" # help           
        else : #right wall bottom
            if right_wall_bottom_right == True:
                Ball_movement_vel = Ball_movement_vel 
                Delta_ball_x = -8
                Delta_ball_y = 0
                Ball_state = "haha" # help
            else:
                Ball_movement_vel = Ball_movement_vel 
                Delta_ball_x = -8
                Delta_ball_y = -8
                Ball_state = "haha" # help
        Player1_quadrant1_right = True 
        Player1_quadrant2_right = True 
        Player2_quadrant3_right = True 
        Player2_quadrant4_right = True                  
    if Ball_rect.x < 10 : # left wall
        if Ball_rect.y > screen.get_height()//2 : #left wall top
            if left_wall_top_right == False:
                Ball_movement_vel = Ball_movement_vel 
                Delta_ball_x = 0
                Delta_ball_y = 0
                Ball_state = "haha" # help
            else:
                Ball_movement_vel = Ball_movement_vel 
                Delta_ball_x = 0
                Delta_ball_y = -8
                Ball_state = "haha" # help                
        else : #left wall bottom 
            if left_wall_bottom_right == True:
                Ball_movement_vel = Ball_movement_vel 
                Delta_ball_x = 0
                Delta_ball_y = -8
                Ball_state = "haha" # help
            else:
                Ball_movement_vel = Ball_movement_vel 
                Delta_ball_x = 0
                Delta_ball_y = 0
                Ball_state = "haha" # help
        Player1_quadrant1_right = False 
        Player1_quadrant2_right = False 
        Player2_quadrant3_right = False 
        Player2_quadrant4_right = False 

    if Ball_rect.colliderect(Player1_rect): # top 
        if Ball_rect.x > screen.get_width()//2: #quadrant 1
            if Player1_quadrant1_right == True :
                Ball_movement_vel = Ball_movement_vel 
                Delta_ball_x = -8
                Delta_ball_y = 0
                left_wall_bottom_right = False
                left_wall_top_right = False
            else:
                Ball_movement_vel = Ball_movement_vel 
                Delta_ball_x = 0
                Delta_ball_y = 0
                right_wall_bottom_right = True
                right_wall_top_right = True
        else: #quadrant 2
            if Player1_quadrant2_right == False :
                Ball_movement_vel = Ball_movement_vel 
                Delta_ball_x = 0
                Delta_ball_y = 0
                right_wall_bottom_right = True
                right_wall_top_right = True
            else:
                Ball_movement_vel = Ball_movement_vel 
                Delta_ball_x = -8
                Delta_ball_y = 0
                left_wall_bottom_right = False
                left_wall_top_right = False         
    if Ball_rect.colliderect(Player2_rect): # bottom
        if Ball_rect.x > screen.get_width()//2: # quadrant 4
            if Player2_quadrant4_right == True:
                Ball_movement_vel = Ball_movement_vel 
                Delta_ball_x = -8
                Delta_ball_y = -8
                left_wall_bottom_right = True
                left_wall_top_right = True
            else:
                Ball_movement_vel = Ball_movement_vel 
                Delta_ball_x = 0
                Delta_ball_y = -8
                right_wall_bottom_right = False
                right_wall_top_right = False                
        else : # quadrant 3
            if Player2_quadrant3_right == False:
                Ball_movement_vel = Ball_movement_vel 
                Delta_ball_x = 0
                Delta_ball_y = -8
                right_wall_bottom_right = False
                right_wall_top_right = False
            else:
                Ball_movement_vel = Ball_movement_vel 
                Delta_ball_x = -8
                Delta_ball_y = -8
                left_wall_bottom_right = True
                left_wall_top_right = True
    Ball_rect.x += Ball_movement_vel + Delta_ball_x
    Ball_rect.y += Ball_movement_vel + Delta_ball_y
    if Ball_rect.y > 600:
        pygame.draw.rect(screen,random_colour_tuple,Blank_screen_rect)
        screen.blit(Text_player2_lost,(text_x,text_y))
        pygame.display.update()
        time.sleep(3)
        running = False and pygame.quit()
    if Ball_rect.y < 0:
        pygame.draw.rect(screen,random_colour_tuple,Blank_screen_rect)
        screen.blit(Text_player1_lost,(text_x,text_y))
        pygame.display.update()
        time.sleep(3)
        running = False and pygame.quit()
    pygame.display.update()
    clock.tick(60)