import pygame
import random
pygame.init()
basket=pygame.image.load("images/basket.png")
bowl_image = pygame.transform.scale(basket , ( 200 , 200))
apple=pygame.image.load("images/apple.png")
pear=pygame.image.load("images/pear.png")
pear=pygame.transform.scale(pear , (120 , 120))
font_score=pygame.font.Font("Fonts/Light.ttf",20)
text_surface_score = font_score.render("example" , True , "black")
# pygame setup
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
class player():
    def __init__(self):
        self.color = 'lightblue'
        self.height = 200
        self.width = 200
        self.speed = 5
        self.x = 100
        self.y = 450
        self.score = 0
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

class Fruit():
    def __init__(self , color):
        self.color = color
        self.random = random.choice(["yellow"])
        self.width = 100
        self.height = 100
        self.speed = 5
        self.x = 100
        self.y = 20
    def movement(self):
        self.y += self.speed
        if self.y >  600:
            self.y = 20
            self.x = random.randint(10,1000)
            self.random = random.choice([1,2])
    def collision(self,player):
            

            if ( self.x + self.width > player.x and self.x < player.x + player.width ):
                if ( self.y + self.height > player.y ) :
                    player.score += 10
                    print(player.score) 
                    self.y = 700
                    
                 
Player = player()
fruit1 = Fruit("lightblue")


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("lightblue")
    Player.move()

    fruit1.collision(Player)
    fruit1.movement()

    Score="Your score is:",Player.score
    pygame.draw.rect(screen,Player.color,[Player.x,Player.y,Player.width,Player.height])
    pygame.draw.rect(screen,fruit1.color,[fruit1.x,fruit1.y,fruit1.width,fruit1.height])
    pygame.draw.rect(screen,"#7a4f38",[0,600,2000,1000]) # ground surface

    text_surface = font_score.render( str(Score), True , "black")
    screen.blit(text_surface , ([100,120,00,100]))


    screen.blit(bowl_image , (Player.x , Player.y))

    if fruit1.random == 2:
        Apple = pygame.transform.scale(apple , ( fruit1.width , fruit1.height))
        screen.blit(Apple , (fruit1.x , fruit1.y))
    if fruit1.random == 1:
        Pear = pygame.transform.scale(pear , ( fruit1.width , fruit1.height))
        screen.blit(pear , (fruit1.x , fruit1.y))
 
    pygame.display.flip()

    clock.tick(50)

pygame.quit()