import pygame

from player1 import Player
from pogonec import Pogonec

window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()

bacground = pygame.transform.scale(
    pygame.image.load("optimys_prime/background.png"),(700,500)

)
roma = Player(100,100,50,50, "optimys_prime/sprite1.png", 3)
sofia = Pogonec(100,100,50,50, "optimys_prime/sprite2.png", 3)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    roma.move2()
    roma.move()
    roma.move3()
    roma.move4()
    sofia.move2()
    sofia.move()
    sofia.move3()
    sofia.move4()
    window.blit(bacground,(5,5))
    roma.draw(window)
    sofia.draw(window)
    pygame.display.flip()
    fps.tick(120)