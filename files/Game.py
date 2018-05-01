import pygame, random
from PIL import Image
try:
    from files.Class import Monika, Yuri, Natsuki, Sayori
except ImportError:
    from Class import Monika, Yuri, Natsuki, Sayori

class Game():
    def __init__(self, girlChoosed):
        if girlChoosed == "Monika":
            self.girl = Monika()
        elif girlChoosed == "Yuri":
            self.girl = Yuri()
        elif girlChoosed == "Sayori":
            self.girl = Sayori()
        elif girlChoosed == "Natsuki":
            self.girl = Natsuki()
        else:
            raise Exception
        self.girlGroup = pygame.sprite.Group()
        self.girlGroup.add(self.girl)
        self.timeDirection = 20
        self.played = True
        self.screen = pygame.display.set_mode((500, 500))

        self.clock = pygame.time.Clock()
        pygame.display.set_caption("DDLC's Friends - "+self.girl.name)

    def launch(self):
        while self.played:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.played = False
            self.screen.fill((0, 0, 0))
            self.girlGroup.draw(self.screen)
            for i in self.girlGroup:
                i.move()
                if self.timeDirection == 0:
                    i.direction = random.randint(1,8)
                    self.timeDirection = 20
                else:
                    self.timeDirection -= 1
                content = pygame.image.load("files/images/barre_contenu.png")
                self.screen.blit(pygame.transform.scale(content, (i.vie, 6)), (25, 21))
                self.screen.blit(pygame.transform.scale(content, (i.fun, 6)), (25, 51))
                self.screen.blit(pygame.transform.scale(content, (i.faim, 6)), (411+(65-i.faim), 21))
                self.screen.blit(pygame.transform.scale(content, (i.soif, 6)), (411+(65-i.faim), 51))
            frame = pygame.image.load("files/images/frame.png")
            self.screen.blit(pygame.transform.scale(frame, (500, 70)), (0,430))
            self.screen.blit(pygame.transform.scale(frame, (500, 70)), (0,360))
            self.screen.blit(pygame.image.load("files/images/barre_vie.png"), (10, 10))
            self.screen.blit(pygame.image.load("files/images/barre_fun.png"), (10, 40))
            self.screen.blit(pygame.image.load("files/images/barre_faim.png"), (406, 10))
            self.screen.blit(pygame.image.load("files/images/barre_soif.png"), (406, 40))
            self.clock.tick(60)
            pygame.display.update()
        pygame.quit()