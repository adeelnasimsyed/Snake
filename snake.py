import random 
import pygame
import sys

pygame.init() 
(width, height) = (400, 600)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)  
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')
fps = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 16) 


score = 0



class Snake:

	def __init__(self):

		self.width, self.height = screen.get_size()
		self.posX = self.width/2
		self.posY = self.height/4
		self.body = [[self.posX, self.posY], [self.posX - 10, self.posY], [self.posX - 20, self.posY]]
		self.direction = "RIGHT"

	def changeDirTo(self, dir):

		if dir == "RIGHT" and self.direction != "LEFT":
			self.direction = "RIGHT"

		if dir == "LEFT" and self.direction != "RIGHT":
			self.direction = "LEFT"

		if dir == "UP" and self.direction != "DOWN":
			self.direction = "UP"

		if dir == "DOWN" and self.direction != "UP":
			self.direction = "DOWN"

	def move(self, foodPos):

		if self.direction == "RIGHT":

			self.posX += 10

		if self.direction == "LEFT":

			self.posX -= 10

		if self.direction == "UP":

			self.posY -= 10

		if self.direction == "DOWN":

			self.posY += 10

		position = [self.posX, self.posY]

		self.body.insert(0, list(position))

		if [self.posX, self.posY] == foodPos:
			return 1

		else:
			self.body.pop()
			return 0

	def checkCollision(self):

		if self.posX > self.width or self.posX < 0 or self.posY > self.height or self.posY < 0:
			return 1

		for bodyPart in self.body[1:]:

			if self.posX == bodyPart[0] and self.posY == bodyPart[1]:
				return 1

		return 0



class Food:

	def __init__(self):
		self.width, self.height = pygame.display.get_surface().get_size()
		self.pos = [self.height/2,self.width/2]
		self.isFood = True

	def newFood(self):

		if not self.isFood:

			self.pos = [random.randrange(1,self.width // 10)*10, random.randrange(1,self.height // 10)*10]
			self.isFood = True
		return self.pos

snake = Snake()
food = Food()

def gameOver():
	
	text = font.render('Game Over! You scored: ' + str(score), True, red) 
	textRect = text.get_rect() 
	textRect.center = (width // 2, height // 2) 
	screen.blit(text, textRect)
	pygame.display.update() 
	pygame.time.wait(3000)
	pygame.quit()
	sys.exit()

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameOver()
		elif event.type == pygame.KEYDOWN:

			if event.key == pygame.K_RIGHT:
				snake.changeDirTo("RIGHT")

			elif event.key == pygame.K_LEFT:
				snake.changeDirTo("LEFT")

			elif event.key == pygame.K_UP:
				snake.changeDirTo("UP")

			elif event.key == pygame.K_DOWN:
				snake.changeDirTo("DOWN")

	foodPos = food.newFood()

	if snake.move(foodPos) == 1:
		score += 1
		food.isFood = False

	screen.fill(black)

	for pos in snake.body:
		pygame.draw.rect(screen, red, pygame.Rect(pos[0], pos[1], 10, 10))

	pygame.draw.rect(screen, blue, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

	
	if snake.checkCollision() == 1:
		gameOver()

	pygame.display.set_caption('Snake | Score: ' + str(score))

	pygame.display.flip()
	fps.tick(16)


