import pygame, sys

# CONTANS
WIDTH = 1280
HEIGHT = 720
TITLE = "MY GAMES"
Clock = pygame.time.Clock()

# PYGAME_INITIALIZATION
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# PLAYER CLASS
class Player:
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)
		self.rect = pygame.Rect(x, y, 32, 32)
		self.color = (250, 120, 60)
		self.velX = 0
		self.velY = 0
		self.left_pressed = False
		self.right_pressed = False
		self.up_pressed = False
		self.down_pressed = False
		self.speed = 4
		
	def draw(self, win):
		pygame.draw.rect(win, self.color, self.rect)
		
	def update(self):
		self.velX = 0
		self.velY = 0
		if self.left_pressed and not self.right_pressed:
			self.velX = -self.speed
		if self.right_pressed and not self.left_pressed:
			self.velX = self.speed
		if self.up_pressed and not self.down_pressed:
			self.velY = -self.speed
		if self.down_pressed and not self.up_pressed:
			self.velY = self.speed
			
		self.x += self.velX
		self.y += self.velY
		
		self.rect = pygame.Rect(self.x, self.y, 32, 32)
		

# PLAYER INITIALIZON
player = Player(WIDTH/2, HEIGHT/2)

# MAIN LOOP
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.left_pressed = True
			if event.key == pygame.K_RIGHT:
				player.right_pressed = True
			if event.key == pygame.K_UP:
				player.up_pressed = True
			if event.key == pygame.K_DOWN:
				player.down_pressed = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.left_pressed = False
			if event.key == pygame.K_RIGHT:
				player.right_pressed = False
			if event.key == pygame.K_UP:
				player.up_pressed = False
			if event.key == pygame.K_DOWN:
				player.down_pressed = False
				
	# DRAW
	win.fill((12, 24, 36))
	player.draw(win)
	
	# UPDATE
	player.update()
	pygame.display.flip()
	
	Clock.tick(120)