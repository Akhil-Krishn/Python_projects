import pygame, sys, random

def main():
    pygame.init()
    pygame.font.init()

    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (50,255,50)
    cyan = (10,200,200)
    yellow = (255,255,0)

    screen_width = 800
    screen_height = 800

    #font and text
    font = pygame.font.SysFont("Harlow Solid Italic",70)
    small_font = pygame.font.SysFont("Harlow Solid Italic",60)
    text_x = 100
    text_y = 100
    text_mode_select1 = font.render("Press to Choose Mode",False,white)
    text_mode_select2 = font.render("e-easy,m-medium,h-hard",False,white)
    text_mode_select3 = font.render("please hold down desired key",False,white)
    text_lost1 = font.render("You lost :(",False,white)
    text_lost2 = small_font.render("Press space to restart and esc to quit",False,white)
    text_lost3 = small_font.render("To change difficulty press e,m,h",False,white)

    #modes
    easy_mode,easy = 80,400
    easy_gap = 250
    medium_mode,medium = 90,600                   
    medium_gap = 175
    hard_mode,hard = 90,700
    hard_gap = 100

    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Floppy Rectangle")

    running = True
    clock = pygame.time.Clock()

    space_press_rate = pygame.time.get_ticks()

    def select_mode():

        run = True
        while run:

            screen.fill(black)
            screen.blit(text_mode_select1,(text_x,text_y))
            screen.blit(text_mode_select2,(text_x,text_y + 200))
            screen.blit(text_mode_select3,(text_x,text_y + 400))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return "easy"

            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_e]:
                return "easy"

            elif keys_pressed[pygame.K_m]:
                return "medium"

            elif keys_pressed[pygame.K_h]:
                return "hard"

            pygame.display.update()
            clock.tick(60)

    #so that we dont have to type a lot
    def quit():
        running = False
        pygame.quit()
        sys.exit()

    def lost():
        screen.fill(black)
        screen.blit(text_lost1,(text_x + 50,text_y))
        screen.blit(text_lost2,(text_x -75,text_y + 200))
        pygame.display.update()

    #for selecting the difficulty
    select_mode()

    #defining classes

    #player class
    class Player:
        #the gravity and stuff aint perfect, maybe mess the numbers later?
        def __init__(self,width,height,colour,x,y):
            self.rect = pygame.Rect(x,y,width,height)
            self.colour = colour
            self.gravity_vel = 5
            self.destination_vel = 150
            self.movement_vel = 10
            self.apply_gravity = True
            self.destination_point = 0
            #for checking wheather space is pressed
            self.space_pressed = False 

        def movement(self,other):
            # so that no cheating
            if self.rect.y > 850:
                other.lost = True

            if self.rect.y < -50:
                other.lost = True

            if self.apply_gravity:
                if self.gravity_vel > 12.5:
                    self.gravity_vel = 12.5
                else:
                    self.rect.y += self.gravity_vel
                    self.gravity_vel = self.gravity_vel * 2
            if self.space_pressed:
                self.apply_gravity = False
                #if u dont include this line then it'll go up forever
                self.space_pressed = False 
                self.destination_point = self.rect.y - self.destination_vel
            if self.apply_gravity == False:
                if self.rect.y > self.destination_point:
                    self.rect.y -= self.movement_vel
                else:
                    self.apply_gravity = True
                    self.gravity_vel = 5
        def draw(self):
            pygame.draw.rect(screen,self.colour,self.rect)

    #the obstacle class
    class Obstacle:
        score = 0
        score_text = font.render(f"Score: {score}",False,black)
        def __init__(self,colour,x): # because y always 0 or 800

            if select_mode() == "easy":
                self.mode1,self.mode2,self.mode_gap = easy_mode,easy,easy_gap

            elif select_mode() == "medium":
                self.mode1,self.mode2,self.mode_gap = medium_mode,medium,medium_gap

            elif select_mode() == "hard":
                self.mode1,self.mode2,self.mode_gap = hard_mode,hard,hard_gap

            #if none of the modes are chosen
            else:
                self.mode1,self.mode2,self.mode_gap = easy_mode,easy,easy_gap

            self.lost = False
            self.colour = colour
            #top rect
            self.rect1 = pygame.Rect(x,0,80,10) #the 10 height is a placeholder
            self.rect1.midtop = (x,0)
            #bottom rect
            self.rect2 = pygame.Rect(x,800,80,10) #the 10 height is a placeholder
            #only for rect 1 because it will also decide rect2's height
            self.height_determiner = random.randint(self.mode1,self.mode2)
            self.rect1.height = self.height_determiner
            #not 800 - rect1 height as it would occupy all the space
            self.rect2.height = (800 - self.height_determiner) - self.mode_gap
            self.rect2.midbottom = (x,800)

        def movement(self):
            self.rect1.x -= 5
            self.rect2.x -= 5

        def reset_rect(self,last):
            #i tired but dont know what is wrong so i ctr c, ctr v'ed the __init__ code
            if self.rect1.x < -25:
                Obstacle.score += 1
                Obstacle.score_text = font.render(f"Score: {Obstacle.score}",False,black)
                self.rect1.midtop = (last + 500,0)
                self.rect2.midbottom = (last + 500,800)

                #top rect
                self.rect1 = pygame.Rect(last + 500,0,80,10) #the 10 height is a placeholder
                self.rect1.midtop = (last + 500,0)
                #bottom rect
                self.rect2 = pygame.Rect(last + 500,800,80,10) #the 10 height is a placeholder
                #only for rect 1 because it will also decide rect2's height
                self.height_determiner = random.randint(self.mode1,self.mode2)
                self.rect1.height = self.height_determiner
                #not 800 - rect1 height as it would occupy all the space
                self.rect2.height = (800 - self.height_determiner) - self.mode_gap
                self.rect2.midbottom = (last + 500,800)

        def reset_player(self,player_rect):
            if self.rect1.colliderect(player_rect) or self.rect2.colliderect(player_rect):
                self.lost = True
                Obstacle.score = 0
                Obstacle.score_text = font.render(f"Score: {Obstacle.score}",False,black)

        def draw(self):
            pygame.draw.rect(screen,self.colour,self.rect1)
            pygame.draw.rect(screen,self.colour,self.rect2)
            screen.blit(Obstacle.score_text,(25,700))
        
    #initialse classes
    player = Player(50,50,yellow,int(screen_width/4),screen_height//2 - 100)
    obstacles_lst = []
    for i in range (3): #as there are 3 obstacles which cycle back and forth
        if i == 0:
            obstacles_lst.append(Obstacle(white,500))
        else:
            obstacles_lst.append(Obstacle(white,obstacles_lst[i-1].rect1.x + 500))
    
    def main_window():

        while running:

            if obstacles_lst[0].lost == False and obstacles_lst[1].lost == False and obstacles_lst[2].lost == False:

                screen.fill(cyan)
                #player methods
                player.movement(obstacles_lst[0])
                player.draw()
                #obstacle methods
                for i in range (3):
                    if i == 0:
                        obstacles_lst[i].movement()
                        obstacles_lst[i].reset_rect(obstacles_lst[2].rect1.x)
                        obstacles_lst[i].draw()
                        obstacles_lst[i].reset_player(player.rect)
                    if i == 1:
                        obstacles_lst[i].movement()
                        obstacles_lst[i].reset_rect(obstacles_lst[0].rect1.x)
                        obstacles_lst[i].draw()
                        obstacles_lst[i].reset_player(player.rect)
                    if i == 2:
                        obstacles_lst[i].movement()
                        obstacles_lst[i].reset_rect(obstacles_lst[1].rect1.x)
                        obstacles_lst[i].draw()
                        obstacles_lst[i].reset_player(player.rect)

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        quit()

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_ESCAPE:
                            quit()

                        if event.key == pygame.K_SPACE:
                            player.space_pressed = True 

                pygame.display.update()
                clock.tick(60)

            #player collides with obstacle
            else:
                screen.fill(black)
                text_lost1 = font.render(f"Your Score is {Obstacle.score}",False,white)
                screen.blit(text_lost1,(text_x + 50,text_y))
                screen.blit(text_lost2,(text_x -75,text_y + 200))
                screen.blit(text_lost3,(text_x - 75, text_y + 400))
                
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            obstacles_lst[0].lost = False
                            obstacles_lst[1].lost = False
                            obstacles_lst[2].lost = False
                            #agin idk what is wrong so i copy pasted the __init__ code
                            for i in obstacles_lst:
                                i.rect1 = pygame.Rect(0,0,80,10) #x value is place holder
                                i.rect1.midtop = (0,0)
                                i.rect2 = pygame.Rect(0,800,80,10)
                                i.height_determiner = random.randint(i.mode1,i.mode2)
                                i.rect1.height = i.height_determiner
                                i.rect2.height = (800 - i.height_determiner) - i.mode_gap
                                i.rect2.midbottom = (0,800)
                            player.rect.y = screen_height//2 - 100
                            obstacles_lst[0].rect1.x = player.rect.x + 500
                            obstacles_lst[1].rect1.x = obstacles_lst[0].rect1.x + 500
                            obstacles_lst[2].rect1.x = obstacles_lst[1].rect1.x + 500
                            obstacles_lst[0].rect2.x = obstacles_lst[0].rect1.x
                            obstacles_lst[1].rect2.x = obstacles_lst[1].rect1.x
                            obstacles_lst[2].rect2.x = obstacles_lst[2].rect1.x

                        if event.key == pygame.K_ESCAPE:
                            sys.exit()

                        if event.key == pygame.K_e:
                            for i in obstacles_lst:
                                i.mode1,i.mode2,i.mode_gap = easy_mode,easy,easy_gap
                        if event.key == pygame.K_m:
                            for i in obstacles_lst:
                                i.mode1,i.mode2,i.mode_gap = medium_mode,medium,medium_gap
                        if event.key == pygame.K_h:
                            for i in obstacles_lst:
                                i.mode1,i.mode2,i.mode_gap = hard_mode,hard,hard_gap


                pygame.display.update()
                clock.tick(60)

    main_window()

if __name__ == "__main__":
    main()