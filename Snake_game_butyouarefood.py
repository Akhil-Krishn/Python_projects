#All the modules we need
import pygame,sys,time,math

pygame.init() #idk why
pygame.font.init() #idk why

#width and height of main window and player variables
Win_x = 800
Win_y = 800
player_movement_vel = 80
score_counter = pygame.time.get_ticks()
score_refresh_rate = 10000

#fonts
Ffont = pygame.font.SysFont("Forte",70)

#colours
black = (0,0,0)
white = (255,255,255)
lawn_green = (124,252,50)
cyan = (0,195,255)
maroon_red = (128,0,0)
yellow = (255,255,0)
red = (255,0,0)

#so that we dont need to type it again and agin
def lost():
	time.sleep(0.5)
	screen.fill(black)
	screen.blit(Ffont.render("You Lost, Your Score is " + str(Snake_Head.score_thingy),False,white),(50,350))
	pygame.display.update()
	time.sleep(2)
	running = False
	sys.exit()
	pygame.quit()

#so that we dont need to type it again and agin
def won():
	time.sleep(0.5)
	screen.fill(black)
	screen.blit(Ffont.render("You Won WOW! But How?",False,white),(50,350))
	pygame.display.update()
	time.sleep(2)
	running = False
	sys.exit()
	pygame.quit()

#main screen
screen = pygame.display.set_mode((Win_x,Win_y))

#player class
class Player:

	def __init__(self,colour,width,height,x,y,speed):
		self.colour = colour
		self.speed = speed
		self.rect = pygame.Rect(x,y,width,height)
		self.state = "ready"

	def move_right(self):
		if self.state == "right":
			if self.rect.x + self.speed < 799:
				self.rect.x += self.speed
		

	def move_left(self):
		if self.state == "left":
			if self.rect.x - self.speed > -1:
				self.rect.x -= self.speed

	def move_up(self):
		if self.state == "up":
			if self.rect.y - self.speed > -1:
				self.rect.y -= self.speed
		

	def move_down(self):
		if self.state == "down":
			if self.rect.y + self.speed < 799:
				self.rect.y += self.speed

	def draw(self):
		pygame.draw.rect(screen,self.colour,self.rect)

#snake head class
class Snake_Head:

	score_thingy = 0

	def __init__(self,colour,width,height,x,y,speed):
		self.colour = colour
		self.speed = speed
		self.rect = pygame.Rect(x,y,width,height)
		self.state = "ready"

#undertand the logicc....idk what else to say
#we first check wheather x > y then we check the conditions
#for it and the conditions for the conditions and so on till we decide the state
	def movement_logic(self,other,other_rect):
		if other.state != "ready":
			if other_rect.x > self.rect.x:
				if other_rect.y > self.rect.y:
					if (other_rect.x - self.rect.x) > (other_rect.y - self.rect.y):
						self.state = "right"
					else:
						self.state = "down"
				else:
					if (other_rect.x - self.rect.x) > (self.rect.y - other_rect.y):
						self.state = "right"
					else:
						self.state = "up"

			else:
				if other_rect.y > self.rect.y:
					if (self.rect.x - other_rect.x) > (other_rect.y - self.rect.y):
						self.state = "left"
					else:
						self.state = "down"
				else:
					if (self.rect.x - other_rect.x) > (self.rect.y - other_rect.y):
						self.state = "left"
					else:
						self.state = "up"

	#for movement
	def movement(self):
		if self.state == "right":
			self.rect.x += self.speed
		elif self.state == "left":
			self.rect.x -= self.speed
		elif self.state == "up":
			self.rect.y -= self.speed
		elif self.state == "down":
			self.rect.y += self.speed

	def draw(self):
		pygame.draw.rect(screen,maroon_red,self.rect)

	def reset(self,player_rect):
		if self.rect.colliderect(player_rect):
			lost()

#snake body class
class Snake_Body:

	def __init__(self,colour,width,height):
		self.colour = colour #colour - tuple
		self.width = width
		self.height = height
		#temp varaibles to store the value so in the next iteration it follows the main
		self.temp_x = -1 
		self.temp_y = -1


	def draw(self,other):
		# so it draws only if the snake head eats and increases score
		#implementation of what is said in __init__
		# we put these here so that it resets in every loop iteration
		if self.temp_x < 0 or self.temp_y < 0:# -1 xpos and -1 ypos so that it doesnt blank out when we reach boundary
			#initialy spawn on top the other but then...
			self.x = other.rect.x 
			self.y = other.rect.y
		else:
			#when temp val not < 0, it takes the previous xpos and ypos of main follower then makes it x and y
			self.x = self.temp_x
			self.y = self.temp_y
		self.rect = pygame.Rect(self.x,self.y,self.width,self.height) #a rect
		pygame.draw.rect(screen,self.colour,self.rect)
		# temp vals become not < 0 also is the previous vals of main follower
		self.temp_x = other.rect.x 
		self.temp_y = other.rect.y

	def reset(self,snake_head_rect):
		if self.rect.colliderect(snake_head_rect):
			won()

#instances of the classses
player = Player(yellow,55,55,(Win_x//10) * 5,(Win_y//10) * 5,player_movement_vel)
snake_head = Snake_Head(red,55,55,(Win_x//10) * 2,(Win_y//10) * 2,player_movement_vel//2 + 10)
#snake list is a list of objects so it counts
snake_list = []

#variables for the game loop
running = True
clock = pygame.time.Clock()

#main loop
while running:

	#fill the screen first so that it doesnt cover things
	screen.fill(cyan)

	#drawing stuff to the screen
	snake_head.movement_logic(player,player.rect)
	snake_head.movement()
	snake_head.draw()
	player.move_down()
	player.move_up()
	player.move_left()
	player.move_right()
	player.draw()


	#drawing snake body
	if len(snake_list) > 0:
		for i in range(len(snake_list)):
			if i == 0:
				snake_list[i].draw(snake_head)
			else:
				snake_list[i].draw(snake_list[i -1])

	#checks for collision with snake head
	for i in range(len(snake_list)):
		if i == 0:
			pass
		else:
			snake_list[i].reset(snake_head.rect)

	#checks for collision with player
	snake_head.reset(player.rect)

	#checks for all events
	for event in pygame.event.get():

		#event for quiting
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()

		#event for button pressing
		if event.type == pygame.KEYDOWN:

			#for quiting game when esc is pressed
			if event.key == pygame.K_ESCAPE:
				running = False
				pygame.quit()
				sys.exit()

			#for the player movement
			if event.key == pygame.K_UP and player.state != "down": #up
				player.state = "up"
			if event.key == pygame.K_DOWN and player.state != "up": #down
				player.state = "down"
			if event.key == pygame.K_LEFT and player.state != "right": #left
				player.state = "left"
			if event.key == pygame.K_RIGHT and player.state != "left": #right
				player.state = "right"

	#for increasing the score ie the snake
	if pygame.time.get_ticks() - score_counter > score_refresh_rate:
		Snake_Head.score_thingy += 1
		snake_head.speed += 4 #so it becomes harder to beat
		score_counter = pygame.time.get_ticks()

	#for the snake_list appending
	if Snake_Head.score_thingy > len(snake_list):
		snake_list.append(Snake_Body(lawn_green,55,55))

	pygame.display.update()
	clock.tick(3)