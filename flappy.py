import sys, pygame, random, math

pygame.init()
screen = pygame.display.set_mode((200,270))
pygame.display.set_caption("Schloppy Bird")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

score = 0
hs = 0
surface = pygame.image.load('background.jpg')
surface = pygame.transform.scale(surface, (200, 270))
text_surface = font.render(str(score), False, 'White')
highscore = font.render("Highscore: " + str(hs), False, 'White')


bird = pygame.image.load("pp.png").convert_alpha()
bird = pygame.transform.scale(bird, (35, 35))
bird_rect = bird.get_rect(topleft = (50,100))

pipe = pygame.image.load("pipe.png").convert_alpha()
pipe = pygame.transform.scale(pipe,(49, 175))
invertedpipe = pygame.transform.rotate(pipe, 180)
pipe_rect = pipe.get_rect(topleft = (100,150))
invertedpipe_rect = invertedpipe.get_rect(topleft = (100,-120))


allowed_events = [
    pygame.K_SPACE, pygame.KEYUP, pygame.KEYDOWN, pygame.K_r, pygame.QUIT

]
pygame.event.set_allowed(allowed_events)

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                bird_rect.y -= 40

    text_surface = font.render(str(score), False, 'White')
    screen.blit(surface,(0,0))

    score += 1

    pipe_rect.x -= 10
    invertedpipe_rect.x -= 10

    if pipe_rect.right <= 0: 
        pipe_rect.left = 200
        invertedpipe_rect.left = 200
        pipe_rect.y = random.randrange(120,220)
        invertedpipe_rect.y = pipe_rect.y - 270


    bird_rect.y += 10
# freefall formula


    if bird_rect.bottom >= 225 or bird_rect.top <= 0 or bird_rect.colliderect(pipe_rect) or bird_rect.colliderect(invertedpipe_rect):
        bird_rect.y = 50
        pipe_speed = 10
        if score > hs:
            hs = score 
        highscore = font.render("Highscore: " + str(hs), False, 'White')
        score = 0
        
    screen.blit(bird, bird_rect)

    screen.blit(pipe, pipe_rect)
    screen.blit(invertedpipe, invertedpipe_rect)
    screen.blit(text_surface,(10, 10))
    screen.blit(highscore, (10, 245))
    pygame.display.update()
    clock.tick(10)

pygame.quit()

