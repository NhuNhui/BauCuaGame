# add library pygame
import pygame, sys, random
pygame.init ()

#caption
pygame.display.set_caption("Bầu Cua")

#backgound
bg = pygame.image.load(r'Image\BackGround.jpg')


#create screen game
screen = pygame.display.set_mode((1200,675))

dia = pygame.image.load(r'Image\Dia.png')
dia = pygame.transform.scale(dia,(600,600))
dia_rectangle = dia.get_rect(center=(600,674/2))

nai = pygame.image.load(r'Image\Nai.png')
nai = pygame.transform.scale(nai,(100,100))

ga = pygame.image.load(r'Image\Ga.png')
ga = pygame.transform.scale(ga,(100,100))

bau = pygame.image.load(r'Image\Bau.png')
bau = pygame.transform.scale(bau,(100,100))

cua = pygame.image.load(r'Image\Cua.png')
cua = pygame.transform.scale(cua,(100,100))

tom = pygame.image.load(r'Image\Tom.png')
tom = pygame.transform.scale(tom,(100,100))

ca = pygame.image.load(r'Image\Ca.png')
ca = pygame.transform.scale(ca,(100,100))

lac1 = pygame.image.load(r'Image\Lac_1.png')
lac1 = pygame.transform.scale(lac1,(100,50))

lac2 = pygame.image.load(r'Image\Lac_2.png')
lac2 = pygame.transform.scale(lac2,(100,50))

xong = pygame.image.load(r'Image\Xong.png')
xong = pygame.transform.scale(xong,(180,100))

Nhui = pygame.image.load(r'Image\Nhui.png')
Nhui = pygame.transform.scale(Nhui,(100,100))

Nhi = pygame.image.load(r'Image\Nhi.png')
Nhi = pygame.transform.scale(Nhi,(100,100))

Lai = pygame.image.load(r'Image\Lai.png')
Lai = pygame.transform.scale(Lai,(100,100))

lst_girl = [Nhui,Nhi,Lai]
lst_choose = [nai,bau,tom,ca,cua,ga]
random_one = random.choice(lst_girl)
random_two = random.choice(lst_girl)
random_there = random.choice(lst_girl)

check = False

timer = pygame.USEREVENT
pygame.time.set_timer(timer,200)
time = 0

run = True
while run:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False
        if(event.type == timer and check):
            if(time < 10):
                time+= 1
            else:
                check = False
                
            if(check):
                random_one = random.choice(lst_girl)
                random_two = random.choice(lst_girl)
                random_there = random.choice(lst_girl)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            if(mouse_x > 200 and mouse_x <400 and mouse_y > 350 and mouse_y < 400):
                check = True
                time = 0
                
        

        
    screen.blit(bg,(0,0))
    screen.blit(dia,dia_rectangle)
    screen.blit(random_one,(480,220))
    screen.blit(random_two,(630,220))
    screen.blit(random_there,(550,370))
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if(mouse_x > 200 and mouse_x <400 and mouse_y > 350 and mouse_y < 400):
        screen.blit(lac2,(200,350))
    else:
        screen.blit(lac1,(200,350))
    
    if(time > 9):
        screen.blit(xong,(900,300))
    
    pygame.display.update()