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
    
    def modif(self, value, nombre):
        if value == "vie":
            self.vie += nombre
            if self.vie >= 65:
                self.vie = 65
            elif  self.vie < 0:
                self.vie = 0
        elif value == "faim":
            self.faim += nombre
            if self.faim >= 65:
                self.faim = 65
            elif  self.faim < 0:
                self.faim = 0
        elif value == "fun":
            self.fun += nombre
            if self.fun >= 65:
                self.fun = 65
            elif  self.fun < 0:
                self.fun = 0
        elif value == "soif":
            self.soif += nombre
            if self.soif >= 65:
                self.soif = 65
            elif  self.soif < 0:
                self.soif = 0


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
    
class Item(pygame.sprite.Sprite):
    def __init__(self):
        super(Item, self).__init__()
        self.type = ""
        self.image = pygame.image.load("files/images/natsuki.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.nombre = 0
        self.offsetTX = 0
        self.offsetTY = 32

    def add(self, nombre):
        self.nombre+=nombre
    
    def remove(self, nombre):
        self.temp = self.nombre - nombre
        if self.temp>=0:
            self.nombre = self.temp
            return True
        return False

class Cookie(Item):
    def __init__(self):
        super(Cookie, self).__init__()
        self.type="Cookie"
        self.image = pygame.image.load("files/images/cookie.png")
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 370
        self.offsetTX = 8
    
    def consomme(self, girl):
        if self.remove(1):
            girl.modif("faim", 10)
            girl.modif("vie" , 5)
            girl.modif("soif", -2)
            return False
        else:
            return True


class The(Item):
    def __init__(self):
        super(The, self).__init__()
        self.type="Thé"
        self.image = pygame.image.load("files/images/the.png")
        self.rect = self.image.get_rect()
        self.rect.x = 90
        self.rect.y = 370
        self.offsetTX = 6
    
    def consomme(self, girl):
        if self.remove(1):
            girl.modif("faim", -2)
            girl.modif("vie" , 5)
            girl.modif("soif", 10)
            return False
        else:
            return True

class JusPomme(Item):
    def __init__(self):
        super(JusPomme, self).__init__()
        self.type="Jus de pomme"
        self.image = pygame.image.load("files/images/juspomme.png")
        self.rect = self.image.get_rect()
        self.rect.x = 220
        self.rect.y = 370
    
    def consomme(self, girl):
        if self.remove(1):
            girl.modif("vie", 7)
            girl.modif("soif", 20)
            return False
        else:
            return True

class Cupcake(Item):
    def __init__(self):
        super(Cupcake, self).__init__()
        self.type="Cupcake"
        self.image = pygame.image.load("files/images/cupcake.png")
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 370
        self.offsetTX = 8
    
    def consomme(self, girl):
        if self.remove(1):
            girl.modif("vie", 7)
            girl.modif("faim", 20)
            return False
        else:
            return True

class Gateau(Item):
    def __init__(self):
        super(Gateau, self).__init__()
        self.type="Gâteau"
        self.image = pygame.image.load("files/images/gateau.png")
        self.rect = self.image.get_rect()
        self.rect.x = 270
        self.rect.y = 370
        self.offsetTX = 10
    
    def consomme(self, girl):
        if self.remove(1):
            girl.modif("vie", 10)
            girl.modif("faim", 32)
            return False
        else:
            return True

class Soda(Item):
    def __init__(self):
        super(Soda, self).__init__()
        self.type="Soda"
        self.image = pygame.image.load("files/images/soda.png")
        self.rect = self.image.get_rect()
        self.rect.x = 330
        self.rect.y = 370
        self.offsetTX = 2
    
    def consomme(self, girl):
        if self.remove(1):
            girl.modif("vie", 10)
            girl.modif("soif", 32)
            return False
        else:
            return True

class Shop(pygame.sprite.Sprite):
    def __init__(self):
        super(Shop, self).__init__()
        self.type = "Shop"
        self.image = pygame.image.load("files/images/shop.png")
        self.rect = self.image.get_rect()
        self.rect.x = 406
        self.rect.y = 370