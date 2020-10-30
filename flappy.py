import pygame, sys, random 


pygame.init()
screen = pygame.display.set_mode((500,1000))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)


floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_surface_x = 0
floor_surface_y = 800



bird_midflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png').convert_alpha())
bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100,512))


pipe_surface = pygame.image.load('assets/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [400,600,800]

gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0


def draw_floor():
	screen.blit(floor_surface,(floor_surface_x,floor_surface_y))
	screen.blit(floor_surface,(floor_surface_x + 500,floor_surface_y))


def create_pipe():
	random_pipe_pos = random.choice(pipe_height)
	bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos))
	top_pipe = pipe_surface.get_rect(midbottom = (700,random_pipe_pos - 300))
	return bottom_pipe,top_pipe


def move_pipes(pipes):
	for pipe in pipes:
		pipe.centerx -= 5
	return pipes

def draw_pipes(pipes):
	for pipe in pipes:
		if pipe.bottom >= 1024:
			screen.blit(pipe_surface,pipe)
		else:
			flip_pipe = pygame.transform.flip(pipe_surface,False,True)
			screen.blit(flip_pipe,pipe)

def check_collision(pipes):
	for pipe in pipes:
		if bird_rect.colliderect(pipe):
            # death_sound.play()
			return False

	if bird_rect.top <= -100 or bird_rect.bottom >= 900:
		return False

	return True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 6
        
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    screen.blit(bg_surface,(0,0))
    
    floor_surface_x -= 1
    draw_floor()

    if floor_surface_x <= -500:
        floor_surface_x = 0


    if game_active:
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        screen.blit(bird_surface,bird_rect)
        game_active= check_collision(pipe_list)
        bird_movement += gravity
        bird_rect.centery += bird_movement

    


     


    
    

    pygame.display.update()
    clock.tick(120)