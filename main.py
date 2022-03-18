import pygame
import random
pygame.init()
W = 1000
H = 500
screen = pygame.display.set_mode((W,H))
def score(counter):
    font = pygame.font.SysFont(None,40)
    text = font.render("Score: "+ str(counter),True,(255,0,0))
    screen.blit(text,(10,0))
def time(sec):
    font = pygame.font.SysFont(None,40)
    text = font.render("Time left:"+ str(sec),True,(255,0,255))
    screen.blit(text,(W-200,0))
def load_image(name):
    return pygame.image.load(f"assets/{name}.png")
def load_sound(name):
    return pygame.mixer.Sound(f"assets/{name}.wav")
background = load_image("background")
aim = load_image("aim_pointer")
gun = load_image("gun")
blood = load_image("zombie_blood")
zombie_1 = load_image("zombie_1")
zombie_2 = load_image("zombie_2")
zombie_3 = load_image("zombie_3")
zombie_4 = load_image("zombie_4")
shoot = load_sound("shot_sound")
back = load_sound("background")
def over():
    font = pygame.font.SysFont(None,40)
    text = font.render("Game over!",True,(255,255,0))
    screen.blit(text,(W/2-40,H/2-40))
    pygame.display.update()
def game():
    sec = 10000
    zlist = [zombie_1,zombie_2,zombie_3,zombie_4]
    zimg = random.choice(zlist)
    zx = random.randint(0,W-200)
    zy =  random.randint(0,H-300)
    counter = 0
    TIMEREVENT = pygame.USEREVENT+1
    pygame.time.set_timer(TIMEREVENT,1000)
    while True:
        mx,my = pygame.mouse.get_pos()
        zrect = pygame.Rect(zx,zy,zimg.get_width(),zimg.get_height())
        pointer_rect = pygame.Rect(mx,my,aim.get_width(),aim.get_height())
        for event in pygame.event.get():
            if event.type == TIMEREVENT:
                sec -= 1 
            elif event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                shoot.play()
                if zrect.colliderect(pointer_rect):
                    zimng = random.choice(zlist)
                    zx = random.randint(0,W-200)
                    zy =  random.randint(0,H-300)
                    counter += 1
        if sec == 0:
            over()
            break
        screen.blit(background,(0,0)) 
        screen.blit(zimg,(zx,zy))    
        screen.blit(aim,(mx-48,my-48))
        screen.blit(gun,(mx,H-250))
        time(sec)
        score(counter)
        pygame.display.update()
game()
