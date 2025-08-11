#LEZ GOOOO
#IT WORKS!!.............i think
#BUT LEZZ GO BOIS 100% ORIGINAL AND INEFFICEINET CODE
#I DIDN'T TAKE 3HRS, YOU TOOK 3HRS

import pygame,sys,os,time

pygame.init() #initialises pygame i dont know why
pygame.font.init()
                 
screen_width = 600 #win x
screen_height = 600 #win y

#rects?
#verticals
boreder_rect1 = pygame.Rect(screen_width//3-5,0,10,screen_height)
boreder_rect2 = pygame.Rect(((screen_width//3)*2)-5,0,10,screen_height)
#horzontals
boreder_rect3 = pygame.Rect(0,screen_height//3-5,screen_width,10)
boreder_rect4 = pygame.Rect(0,((screen_height//3)*2)-5,screen_width,10)

#fonts
regular_font = pygame.font.SysFont("Comic Sans MS",69)
big_font = pygame.font.SysFont("Arial Black",225)

#positions for each box
box1_pos = (10,-70)
box2_pos = (210,-70)
box3_pos = (410,-70)
box4_pos = (10,130)
box5_pos = (210,130)
box6_pos = (410,130)
box7_pos = (10,330)
box8_pos = (210,330)
box9_pos = (410,330)

#positions for each buttons
bb1_pos =(0,0)
bb2_pos =(200,0)
bb3_pos =(400,0)
bb4_pos =(0,200)
bb5_pos =(200,200)
bb6_pos =(400,200)
bb7_pos =(0,400)
bb8_pos =(200,400)
bb9_pos =(400,400)

#box class??idk
class box_var():
    def __init__(self):
        self.x = False
        self.o = False 

#variables for button presses (once pressed cant be pressed again)
b1 = box_var()
b2 = box_var()
b3 = box_var()
b4 = box_var()
b5 = box_var()
b6 = box_var()
b7 = box_var()
b8 = box_var()
b9 = box_var()

#colors
black = (0,0,0)
white = (255,255,255)
lawn_green = (124,252,50)
cyan = (0,255,255)
maroon_red = (128,0,0)
yellow = (255,255,0)

#basic stuffs
screen = pygame.display.set_mode((screen_width,screen_height)) #main surface
pygame.display.set_caption("Tick Tack Toe Redemption") #captions

turn = "X"

clock = pygame.time.Clock() #clock for time related stuff and FPS
running = True #for running the main loop  

#button that i copied from tim
class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x,self.y,self.width,self.height),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

#buttons
but_box_1 = button(lawn_green,bb1_pos[0],bb1_pos[1],200,200,"")
but_box_2 = button(lawn_green,bb2_pos[0],bb2_pos[1],200,200,"")
but_box_3 = button(lawn_green,bb3_pos[0],bb3_pos[1],200,200,"")
but_box_4 = button(lawn_green,bb4_pos[0],bb4_pos[1],200,200,"")
but_box_5 = button(lawn_green,bb5_pos[0],bb5_pos[1],200,200,"")
but_box_6 = button(lawn_green,bb6_pos[0],bb6_pos[1],200,200,"")
but_box_7 = button(lawn_green,bb7_pos[0],bb7_pos[1],200,200,"")
but_box_8 = button(lawn_green,bb8_pos[0],bb8_pos[1],200,200,"")
but_box_9 = button(lawn_green,bb9_pos[0],bb9_pos[1],200,200,"")

#functions
def draw_scr(font,colour_text,colour_bg):
    screen.fill(colour_bg)

    #buttons?
    but_box_1.draw(screen)
    but_box_2.draw(screen)
    but_box_3.draw(screen)
    but_box_4.draw(screen)
    but_box_5.draw(screen)
    but_box_6.draw(screen)
    but_box_7.draw(screen)
    but_box_8.draw(screen)
    but_box_9.draw(screen)

    # borders
    pygame.draw.rect(screen,black,boreder_rect1)
    pygame.draw.rect(screen,black,boreder_rect2)
    pygame.draw.rect(screen,black,boreder_rect3)
    pygame.draw.rect(screen,black,boreder_rect4)

    #  x and O images/fonts 
    tick_X = font.render("X",1,colour_text)
    tick_O = font.render("O",1,colour_text)

    # if(turn == "X"):
    if(b1.x):
        screen.blit(tick_X,box1_pos)
    if(b2.x):
        screen.blit(tick_X,box2_pos)
    if(b3.x):
        screen.blit(tick_X,box3_pos)
    if(b4.x):
        screen.blit(tick_X,box4_pos)
    if(b5.x):
        screen.blit(tick_X,box5_pos)
    if(b6.x):
        screen.blit(tick_X,box6_pos)
    if(b7.x):
        screen.blit(tick_X,box7_pos)
    if(b8.x):
        screen.blit(tick_X,box8_pos)
    if(b9.x):
        screen.blit(tick_X,box9_pos)
       
    # if(turn == "O"):
    if(b1.o):
        screen.blit(tick_O,box1_pos)
    if(b2.o):
        screen.blit(tick_O,box2_pos)
    if(b3.o):
        screen.blit(tick_O,box3_pos)
    if(b4.o):
        screen.blit(tick_O,box4_pos)
    if(b5.o):
        screen.blit(tick_O,box5_pos)
    if(b6.o):
        screen.blit(tick_O,box6_pos)
    if(b7.o):
        screen.blit(tick_O,box7_pos)
    if(b8.o):
        screen.blit(tick_O,box8_pos)
    if(b9.o):
        screen.blit(tick_O,box9_pos)

def check_won():

    #XXXXXXX
    if(b1.x and b5.x and b9.x):
        return "Wx"
    if(b7.x and b5.x and b3.x):
        return "Wx"
    if(b1.x and b4.x and b7.x):
        return "Wx"
    if(b2.x and b5.x and b8.x):
        return "Wx"
    if(b3.x and b6.x and b9.x):
        return "Wx"
    if(b1.x and b2.x and b3.x):
        return "Wx"
    if(b4.x and b5.x and b6.x):
        return "Wx"
    if(b7.x and b8.x and b9.x):
        return "Wx"

    #OOOOOOOOO
    if(b1.o and b5.o and b9.o):
        return "Wo"
    if(b7.o and b5.o and b3.o):
        return "Wo"
    if(b1.o and b4.o and b7.o):
        return "Wo"
    if(b2.o and b5.o and b8.o):
        return "Wo"
    if(b3.o and b6.o and b9.o):
        return "Wo"
    if(b1.o and b2.o and b3.o):
        return "Wo"
    if(b4.o and b5.o and b6.o):
        return "Wo"
    if(b7.o and b8.o and b9.o):
        return "Wo"

def check_draw():
    if(b1.x or b1.o):
        if(b2.x or b2.o):
            if(b3.x or b3.o):
                if(b4.x or b4.o):
                    if(b5.x or b5.o):
                        if(b6.x or b6.o):
                            if(b7.x or b7.o):
                                if(b8.x or b8.o):
                                    if(b9.x or b9.o):
                                        return "draw"

def Won_X():
    screen.fill(cyan)
    won_text = regular_font.render("PLAYER X WON!!",1,black)
    screen.blit(won_text,(20,230))
    pygame.display.update()
    time.sleep(2.5)
    running = False
    sys.exit()
    pygame.quit()

def Won_O():
    screen.fill(cyan)
    won_text = regular_font.render("PLAYER O WON!!",1,black)
    screen.blit(won_text,(20,230))
    pygame.display.update()
    time.sleep(2.5)
    running = False
    sys.exit()
    pygame.quit()

def draw_game():
    screen.fill(cyan)
    won_text = regular_font.render("IT'S A DRAW!!",1,black)
    screen.blit(won_text,(50,230))
    pygame.display.update()
    time.sleep(2.5)
    running = False
    sys.exit()
    pygame.quit()

while running: #main loop
    
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if but_box_1.isOver(mouse_pos) and b1.x == False and b1.o == False:
                if(turn == "X"):
                    b1.x = True
                    turn = "O"
                elif (turn == "O"):
                    b1.o = True
                    turn = "X"
            elif but_box_2.isOver(mouse_pos) and b2.x == False and b2.o == False:
                if(turn == "X"):
                    b2.x = True
                    turn = "O"
                elif (turn == "O"):
                    b2.o = True
                    turn = "X"
            elif but_box_3.isOver(mouse_pos) and b3.x == False and b3.o == False:
                if(turn == "X"):
                    b3.x = True
                    turn = "O"
                elif (turn == "O"):
                    b3.o = True
                    turn = "X"
            elif but_box_4.isOver(mouse_pos) and b4.x == False and b4.o == False:
                if(turn == "X"):
                    b4.x = True
                    turn = "O"
                elif (turn == "O"):
                    b4.o = True
                    turn = "X"
            elif but_box_5.isOver(mouse_pos) and b5.x == False and b5.o == False:
                if(turn == "X"):
                    b5.x = True
                    turn = "O"
                elif (turn == "O"):
                    b5.o = True
                    turn = "X"
            elif but_box_6.isOver(mouse_pos) and b6.x == False and b6.o == False:
                if(turn == "X"):
                    b6.x = True
                    turn = "O"
                elif (turn == "O"):
                    b6.o = True
                    turn = "X"
            elif but_box_7.isOver(mouse_pos) and b7.x == False and b7.o == False:
                if(turn == "X"):
                    b7.x = True
                    turn = "O"
                elif (turn == "O"):
                    b7.o = True
                    turn = "X"
            elif but_box_8.isOver(mouse_pos) and b8.x == False and b8.o == False:
                if(turn == "X"):
                    b8.x = True
                    turn = "O"
                elif (turn == "O"):
                    b8.o = True
                    turn = "X"
            elif but_box_9.isOver(mouse_pos) and b9.x == False and b9.o == False:
                if(turn == "X"):
                    b9.x = True
                    turn = "O"
                elif (turn == "O"):
                    b9.o = True
                    turn = "X"

    if(check_won() == "Wx"):
        Won_X()
    elif(check_won() == "Wo"):
        Won_O()
    elif(check_draw() == "draw"):
        draw_game()
    
    draw_scr(big_font,black,cyan)
    print()
    clock.tick(30)
    pygame.display.update()

pygame.quit()
sys.exit()