import pygame, random
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
        self.screen = pygame.display.set_mode((400, 500))

        self.clock = pygame.time.Clock()
        pygame.display.set_caption("DDLC's Friends - "+self.girl.name)

    def launch(self):
        while self.played:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.played = False
                if event.type == pygame.QUIT:
                    self.played = False
            self.screen.fill((0, 0, 0))
            for i in self.girlGroup:
                i.move()
                if self.timeDirection == 0:
                    i.direction = random.randint(1,8)
                    self.timeDirection = 20
                else:
                    self.timeDirection -= 1
            self.girlGroup.draw(self.screen)
            self.clock.tick(60)
            pygame.display.update()
        pygame.quit()