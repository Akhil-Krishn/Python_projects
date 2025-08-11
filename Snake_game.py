#I FAINALLY DID IT!!!!!!!!
#MY VERY OWN CODE FOR SNAKE GAME!!!!!!!
#YES FAINALLY!!
#THIS IS 100% ORIGINAL CODE.....
#YES!!!! WOOOOOOOO!!!!


import pygame,random,sys,time #all the imports


pygame.init() #initialises pygame i dont know why
pygame.font.init() #dont know why


screen_width = 800 #win x
screen_height = 800 #win y


#fonts
regular_font = pygame.font.SysFont("Forte",50)
big_font = pygame.font.SysFont("Forte",70)


black = (0,0,0)
white = (255,255,255)
lawn_green = (124,252,50)
cyan = (0,255,255)
maroon_red = (128,0,0)
yellow = (255,255,0)


grid_y = screen_height//10
grid_x = screen_width//10


snake_speed = 80
snake_head_x = screen_width//10 + (80 * 4)
snake_head_y = screen_height//10 + (80 * 4)
snake_list = []


screen = pygame.display.set_mode((screen_width,screen_height)) #main surface
pygame.display.set_caption("Snake Game Redemption") #captions


clock = pygame.time.Clock() #clock for time related stuff and FPS
running = True #for running the main loop


#so that we dont need to type it again and agin
def lost():
	screen.fill(black)
	screen.blit(big_font.render("You Lost, Your Score is " + str(Snake.score),False,white),(50,350))
	pygame.display.update()
	time.sleep(2)
	running = False
	sys.exit()
	pygame.quit()

#Snake class
class Snake:
	score = 0 #class variable so that if effects all instances
	def __init__(self,colour,width,height):
		self.colour = colour #colour - tuple
		self.width = width
		self.height = height
		#temp varaibles to store the value so in the next iteration it follows the main
		self.temp_x = -1 
		self.temp_y = -1


	def draw_snake(self,other):
		# so it draws only if the snake head eats and increases score
		#implementation of what is said in __init__
		# we put these here so that it resets in every loop iteration
		if self.temp_x < 0 or self.temp_y < 0:# -1 xpos and -1 ypos so that it doesnt blank out when we reach boundary
			#initialy spawn on top the other but then...
			self.x = other.x 
			self.y = other.y
		else:
			#when temp val not < 0, it takes the previous xpos and ypos of main follower then makes it x and y
			self.x = self.temp_x
			self.y = self.temp_y
		self.snake_rect = pygame.Rect(self.x,self.y,self.width,self.height) #a rect
		pygame.draw.rect(screen,self.colour,self.snake_rect)
		# temp vals become not < 0 also is the previous vals of main follower
		self.temp_x = other.x 
		self.temp_y = other.y


	#checks wheather snake head collided with snake body
	def collision_head(self,snek_head):
		if self.snake_rect.colliderect(snek_head):
			lost()


#snake head class
class Snake_head:
	def __init__(self,colour,x,y,width,height,speed):
		self.state = "ready"
		self.colour = colour
		self.speed = speed
		self.head_rect = pygame.Rect(x,y,width,height)


	def movement_right(self):
		if self.state == "right":
			self.head_rect.x += self.speed


	def movement_left(self):
		if self.state == "left":
			self.head_rect.x -= self.speed


	def movement_up(self):
		if self.state == "up":
			self.head_rect.y -= self.speed


	def movement_down(self):
		if self.state == "down":
			self.head_rect.y += self.speed


	def draw_snake_head(self):
		pygame.draw.rect(screen,self.colour,self.head_rect)


#food class
class Food:
	def __init__(self,colour,width,height):
		self.colour = colour
		self.x = random.randint(10,700)
		self.y = random.randint(10,700)
		self.food_rect = pygame.Rect(self.x,self.y,width,height)


	def draw_friut(self):
		pygame.draw.rect(screen,self.colour,self.food_rect)


	#to reset the xpos and ypos that is if the snake head collide with food
	def reset(self,other,snake_class):
		if self.food_rect.colliderect(other):
			self.food_rect.x = random.randint(10,700)
			self.food_rect.y = random.randint(10,700)
			Snake.score += 1



#instaniate the objects
snake_head = Snake_head(maroon_red,snake_head_x,snake_head_y,80,80,snake_speed)
friut = Food(yellow,40,40)


while running: #main loop

	
	for event in pygame.event.get(): #we get all events


		#quit game
		if event.type == pygame.QUIT: 
			running = False 
			pygame.quit()
			sys.exit()


		#for the movement of snake head using input
		if event.type == pygame.KEYDOWN:


			# to exit the game
			if event.key == pygame.K_ESCAPE:
				running = False 
				pygame.quit()
				sys.exit()				


			if event.key == pygame.K_UP and snake_head.state != "down":
				snake_head.state = "up"


			elif event.key == pygame.K_DOWN and snake_head.state != "up":
				snake_head.state = "down"


			elif event.key == pygame.K_RIGHT and snake_head.state != "left":
				snake_head.state = "right"


			elif event.key == pygame.K_LEFT and snake_head.state != "right":
				snake_head.state = "left" 
			

	screen.fill(cyan)
	#we need to draw between scren.fill and the grid because we want it below grid and above screen fill
	snake_head.movement_down()
	snake_head.movement_up()
	snake_head.movement_left()
	snake_head.movement_right()
	snake_head.draw_snake_head()
	if len(snake_list) > 0: #so that if score is < 0 it doesnt execute
		for i in range(Snake.score): # we made this for loop as multiple while loops cause problem in pygame
			if i == 0: #so that the first body part would follow head
				snake_list[i].draw_snake(snake_head.head_rect)
			else: # so that remaining body parts follow the boby part before it
				snake_list[i].draw_snake(snake_list[i -1].snake_rect)
	friut.reset(snake_head.head_rect,Snake)
	friut.draw_friut()


	# we dont want a visible grid so i'll just comment out the lines :(
	#to add grid back, just remove all "#" from "for i " till "grid_y = "....

	#we make it 9 so that in the last iteration it rests otherwise some weird stuff happens
	# for i in range(9): 
	#  	#implementaion
	# 	grid_rect_x = pygame.Rect(grid_x,0,5,screen_height)#create first vertical line
	# 	pygame.draw.rect(screen,black,grid_rect_x) #then blit it
	# 	grid_rect_y = pygame.Rect(0,grid_y,screen_width,5) #same but horizontal lines
	# 	pygame.draw.rect(screen,black,grid_rect_y) #then blit it
	# 	#then increase it to get the grid
	# 	grid_y += 80 
	# 	grid_x += 80
	# 	#this makes it so that when the global variable passes the diplay limit, it resets
	# 	if grid_x + 80 > 800:
	# 		grid_x = screen_width//10
	# 	if grid_y + 80 > 800:
	# 		grid_y = screen_height//10


	#checks for snake head and body collision
	if Snake.score > 1: # because the first body part always collides with head
		for i in snake_list:
			i.collision_head(snake_head.head_rect)


	#checks wheather snake head goes beyond boundaries

	if snake_head.head_rect.x > 800: #right
		lost()


	if snake_head.head_rect.x < 0: #left
		lost()


	if snake_head.head_rect.y > 800: #down
		lost()


	if snake_head.head_rect.x < 0: #up
		lost()


	#creates a instance of snake whenever score is greater than list items, ie bodyparts
	if Snake.score - len(snake_list) > 0:
		snake_list.append(Snake(lawn_green,80,80)) #very important


	#to display score
	screen.blit(regular_font.render("Your Score is " + str(Snake.score),False,black),(10,725))


	pygame.display.update() #updates display
	clock.tick(3) #FPS