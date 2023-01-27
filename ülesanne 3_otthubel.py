# ott hubel
import pygame

screen = pygame.display.set_mode([640, 480]) #ekraani suurus
pygame.display.set_caption("Harjutamine") #ekraani nimi


GREEN = [153, 255, 153] #roheline värv
screen.fill(RED) #taustavärv punane


        y = 1 #funktsioon mis joonistab ruute
        for i in range(35):
            x = 1
            for j in range(38):
                pygame.draw.rect(screen, self.color, [x, y, self.sizea, self.sizeb])
                x += 18
         y += 18


Square.make_square(Square(YELLOW, 15, 15)) #ruudu suurus ja värv

pygame.display.flip()
# jätab avatud akna ekraanile
running = True
while running:
    for event in pygame.event.get():
        # laseb avatud akna kinni panna
        if event.type == pygame.QUIT:
            running = False