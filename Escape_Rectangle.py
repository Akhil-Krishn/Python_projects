import pygame,win32api,random,time,sys
pygame.font.init()
font = pygame.font.SysFont("Forte",100)
large_font = pygame.font.SysFont("Forte",115)
win_x = win32api.GetSystemMetrics(0)
win_y = win32api.GetSystemMetrics(1)
screen = pygame.display.set_mode((win_x,win_y))
clock = pygame.time.Clock()
movement_vel_player = 5
movement_vel_enemy = 3
player_state = "ready"
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (50,255,50)
cyan = (10,200,200)
yellow = (255,255,0)
running = True
class rectangle:
    def __init__ (self,width,height,x,y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x,y,height,width)
        self.reset = False
    def draw(self,colour):
        self.colour = colour
        pygame.draw.rect(screen,self.colour,self.rect)
    def movement_left(self):
        self.rect.x -= movement_vel_player
    def movement_right(self):
        self.rect.x += movement_vel_player
    def movement_up(self):
        self.rect.y -= movement_vel_player
    def movement_down(self):
        self.rect.y += movement_vel_player
    def follow(self,other_obj):
        self.obj = other_obj
        if player_state != "ready":
            if self.obj.x > self.rect.x:
                self.rect.x += movement_vel_enemy
            if self.obj.x < self.rect.x:
                self.rect.x -= movement_vel_enemy
            if self.obj.y > self.rect.y:
                self.rect.y += movement_vel_enemy
            if self.obj.y < self.rect.y:
                self.rect.y -= movement_vel_enemy
    def collision(self,other,score):
        self.other = other
        self.score = score
        self.lose_text = large_font.render("Your Score is " + str(self.score) + " " + "Akhil Rocks", False , white)
        if self.rect.colliderect(self.other):
            screen.fill(black)
            screen.blit(self.lose_text,(screen.get_width()//2 - 650,screen.get_height()//2))
            pygame.display.update()
            time.sleep(3)
            sys.exit()
            running = False
            pygame.quit()
class food:
    def __init__(self):
        self.x = random.randint(10, win_x - 10)
        self.y = random.randint(10, win_y - 10)
        self.rect = pygame.Rect(self.x,self.y,40,40)
        self.score = 0
    def draw(self,colour):
        self.colour = colour
        pygame.draw.rect(screen,self.colour,self.rect)
    def reset_or_collide(self,other):
        if self.rect.colliderect(other):
            self.x = random.randint(10, win_x - 10)
            self.y = random.randint(10, win_y - 10)
            self.rect = pygame.Rect(self.x,self.y,40,40)
            self.score += 1
    def display_score(self):
        self.score_text = font.render("Score: " + str(self.score) , False, black)
        screen.blit(self.score_text,(10/100*win_x,90/100*win_y))

player = rectangle(60,60,800,300)
enemy = rectangle(60,60,800,600)
food = food()

while running:
    screen.fill(cyan)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
            if event.key == pygame.K_a: #left
                player_state = "left"
            if event.key == pygame.K_d: #right
                player_state = "right"
            if event.key == pygame.K_w: #up
                player_state = "up"
            if event.key == pygame.K_s: #down
                player_state = "down"
    if player_state == "right" and player.rect.x + movement_vel_player < win_x - 70:
        player.movement_right()
    if player_state == "left" and player.rect.x - movement_vel_player > 10:
        player.movement_left()
    if player_state == "up" and player.rect.y - movement_vel_player > 10:
        player.movement_up()
    if player_state == "down" and player.rect.y + movement_vel_player < win_y - 70:
        player.movement_down()
    player.draw(green)
    enemy.draw(red)
    enemy.follow(player.rect)
    food.draw(yellow)
    food.reset_or_collide(player.rect)
    food.display_score()
    player.collision(enemy.rect,food.score)
    clock.tick(60)
    pygame.display.update()