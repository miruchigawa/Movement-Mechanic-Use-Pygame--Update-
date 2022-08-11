import pygame

pygame.init()

#Game Variable 
player_x = 250
player_y = 250
y_movement = 0
x_movement = 0
player_size = 60


loop = True

while loop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				y_movement -= 5
			if event.key == pygame.K_DOWN:
				y_movement += 5
			if event.key == pygame.K_LEFT:
				x_movement -= 5
			if event.key == pygame.K_RIGHT:
				x_movement += 5
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				y_movement = 0
			if event.key == pygame.K_DOWN:
				y_movement = 0
			if event.key == pygame.K_LEFT:
				x_movement = 0
			if event.key == pygame.K_RIGHT:
				x_movement = 0
			
	screen = pygame.display.set_mode((1280, 720))
	
	screen.fill((255, 255, 255))
	
	player = pygame.draw.rect(screen, (0, 0, 0), [player_x, player_y, player_size, player_size])
	
	player_x = player_x + x_movement
	player_y = player_y + y_movement
	
	pygame.display.update()