import pygame

class Player:
    def __init__(self,x,y,w,h,img,speed):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w,h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed


    def draw(self,window):
        pygame.draw.rect(window,(225,0,0),self.hitbox)
        window.blit(self.photo,(self.hitbox.x, self.hitbox.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.hitbox.y -= self.speed

    def move2(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.hitbox.y += self.speed

    def move3(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.hitbox.x += self.speed

    def move4(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed