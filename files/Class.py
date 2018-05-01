import pygame, random

class Personnage(pygame.sprite.Sprite):
    def __init__(self):
        super(Personnage, self).__init__()
        self.name = "Personnage"
        self.image = pygame.image.load("files/images/natsuki.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.xMin = 10
        self.xMax = 210
        self.yMin = 50
        self.yMax = 200
        self.direction = 1
        self.vie = 65
        self.faim = 65
        self.soif = 65
        self.fun = 65
    
    def move(self):
        nb = random.randint(0,5)
        if self.direction == 1:
            self.rect.x += nb
            if self.rect.x > self.xMax:
                self.rect.x = self.xMax
        elif self.direction == 2:
            self.rect.x -= nb
            if self.rect.x < self.xMin:
                self.rect.x = self.xMin
        elif self.direction == 3:
            self.rect.y += nb
            if self.rect.y > self.yMax:
                self.rect.y = self.yMax
        elif self.direction == 4:
            self.rect.y -= nb
            if self.rect.y < self.yMin:
                self.rect.y = self.yMin

class Natsuki(Personnage):
    def __init__(self):
        super(Natsuki, self).__init__()
        self.name = "Natsuki"
        self.image = pygame.image.load("files/images/natsuki.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

class Monika(Personnage):
    def __init__(self):
        super(Monika, self).__init__()
        self.name = "Monika"
        self.image = pygame.image.load("files/images/monika.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

class Yuri(Personnage):
    def __init__(self):
        super(Yuri, self).__init__()
        self.name = "Yuri"
        self.image = pygame.image.load("files/images/yuri.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

class Sayori(Personnage):
    def __init__(self):
        super(Sayori, self).__init__()
        self.name = "Sayori"
        self.image = pygame.image.load("files/images/sayori.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100