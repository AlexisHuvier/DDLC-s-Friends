import pygame, random, threading, time, datetime
from tkinter.messagebox import askquestion, showinfo

class Save():
    def __init__(self, girl):
        self.girl = girl
        self.load()
    
    def load(self):
        try:
            with open("files/saves/"+self.girl.name+".txt", "r") as fichier:
                pass
        except:
            self.create("load")
        else:
            if askquestion("Saves", "Une sauvegarde a été trouvé.\nVoulez-vous la charger ?") == "yes":
                with open("files/saves/"+self.girl.name+".txt", "r") as fichier:
                    listSave = fichier.read().split("\n")
                    self.girl.vie = int(listSave[0].split(" : ")[1])
                    self.girl.fun = int(listSave[1].split(" : ")[1])
                    self.girl.faim = int(listSave[2].split(" : ")[1])
                    self.girl.soif = int(listSave[3].split(" : ")[1])
                    self.girl.coin = int(listSave[4].split(" : ")[1])
                    annee, mois, jour, heure = listSave[5].split(" : ")[1].split("-")
                    now = datetime.datetime.now()
                    past = datetime.datetime(int(annee), int(mois), int(jour), int(heure))
                    difference = now - past
                    if difference.days >= 15:
                        self.girl.vie = 0
                        self.girl.faim = 0
                        self.girl.soif = 0
                        self.girl.fun = 0
                    else:
                        for i in range((difference.days*24+(int(heure)-now.hour))//5):
                            self.girl.modif("faim", -2)
                            self.girl.modif("soif", -3)
                            self.girl.modif("fun", -3)
                    for i in self.girl.game.inventory:
                        if i.type == "Cookie":
                            i.nombre = int(listSave[6].split(" : ")[1])
                        elif i.type == "Thé":
                            i.nombre = int(listSave[7].split(" : ")[1])
                        elif i.type == "Cupcake":
                            i.nombre = int(listSave[8].split(" : ")[1])
                        elif i.type == "Jus de pomme":
                            i.nombre = int(listSave[9].split(" : ")[1])
                        elif i.type == "Gâteau":
                            i.nombre = int(listSave[10].split(" : ")[1])
                        elif i.type == "Soda":
                            i.nombre = int(listSave[11].split(" : ")[1])
    
    def create(self, loadGo = ""):
        texte = ""
        texte += "Vie : "+str(self.girl.vie)+"\n"
        texte += "Fun : "+str(self.girl.fun)+"\n"
        texte += "Faim : "+str(self.girl.faim)+"\n"
        texte += "Soif : "+str(self.girl.soif)+"\n"
        texte += "Coin : "+str(self.girl.coin)+"\n"
        now = datetime.datetime.now()
        texte += "Time : "+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"-"+str(now.hour)+"\n"
        for i in self.girl.game.inventory:
            if i.type == "Cookie":
                 texte += "Cookie : "+str(i.nombre)+"\n"
            elif i.type == "Thé":
                texte += "Thé : "+str(i.nombre)+"\n"
            elif i.type == "Cupcake":
                texte += "Cupcake : "+str(i.nombre)+"\n"
            elif i.type == "Jus de pomme":
                texte += "Jus de pomme : "+str(i.nombre)+"\n"
            elif i.type == "Gâteau":
                texte += "Gâteau : "+str(i.nombre)+"\n"
            elif i.type == "Soda":
                texte += "Soda : "+str(i.nombre)
        with open("files/saves/"+self.girl.name+".txt", "w") as fichier:
            fichier.write(texte)
        if loadGo != "":
            self.load()
            

class Personnage(pygame.sprite.Sprite):
    def __init__(self, game):
        super(Personnage, self).__init__()
        self.name = "Personnage"
        self.game = game
        self.image = pygame.image.load("files/images/natsuki.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.xMin = 10
        self.xMax = 210
        self.yMin = 50
        self.yMax = 200
        self.coin = 0
        self.direction = 1
        self.time = 0
        self.vie = 65
        self.faim = 65
        self.soif = 65
        self.timeHappy = 0
        self.fun = 65
        self.die = False
    
    def update(self):
        if self.vie == 0 and self.die == False:
            self.image = pygame.transform.rotate(self.image, 90)
            self.die = True
        if self.faim == 0 or self.fun == 0 or self.soif == 0:
            self.modif("vie", -1)
        return self.die
    
    def move(self):
        if self.vie > 0:
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
        
    def pay(self, nombre):
        if self.coin - nombre < 0:
            return True
        self.coin -= nombre
        return False

    def addMoney(self, nombre):
        self.coin+=nombre


class Natsuki(Personnage):
    def __init__(self, game):
        super(Natsuki, self).__init__(game)
        self.name = "Natsuki"
        self.image = pygame.image.load("files/images/natsuki.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.save = Save(self)
    
    def update(self):
        if self.timeHappy > 1:
            self.timeHappy -= 1
        elif self.timeHappy == 1:
            self.image = pygame.image.load("files/images/natsuki.png")
            self.timeHappy = 0
        return super(Natsuki, self).update()
    
    def modif(self, value, nombre):
        super(Natsuki, self).modif(value, nombre)
        if nombre > 0:
            self.image = pygame.image.load("files/images/natsuki_happy.png")
            self.timeHappy = 20

class Monika(Personnage):
    def __init__(self, game):
        super(Monika, self).__init__(game)
        self.name = "Monika"
        self.image = pygame.image.load("files/images/monika.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.save = Save(self)
    
    def update(self):
        if self.timeHappy > 1:
            self.timeHappy -= 1
        elif self.timeHappy == 1:
            self.image = pygame.image.load("files/images/monika.png")
            self.timeHappy = 0
        return super(Monika, self).update()
    
    def modif(self, value, nombre):
        super(Monika, self).modif(value, nombre)
        if nombre > 0:
            self.image = pygame.image.load("files/images/monika_happy.png")
            self.timeHappy = 20

class Yuri(Personnage):
    def __init__(self, game):
        super(Yuri, self).__init__(game)
        self.name = "Yuri"
        self.image = pygame.image.load("files/images/yuri.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.save = Save(self)
    
    def update(self):
        if self.timeHappy > 1:
            self.timeHappy -= 1
        elif self.timeHappy == 1:
            self.image = pygame.image.load("files/images/yuri.png")
            self.timeHappy = 0
        return super(Yuri, self).update()
    
    def modif(self, value, nombre):
        super(Yuri, self).modif(value, nombre)
        if nombre > 0:
            self.image = pygame.image.load("files/images/yuri_happy.png")
            self.timeHappy = 20

class Sayori(Personnage):
    def __init__(self, game):
        super(Sayori, self).__init__(game)
        self.name = "Sayori"
        self.image = pygame.image.load("files/images/sayori.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.save = Save(self)
    
    def update(self):
        if self.timeHappy > 1:
            self.timeHappy -= 1
        elif self.timeHappy == 1:
            self.image = pygame.image.load("files/images/sayori.png")
            self.timeHappy = 0
        return super(Sayori, self).update()
    
    def modif(self, value, nombre):
        super(Sayori, self).modif(value, nombre)
        if nombre > 0:
            self.image = pygame.image.load("files/images/sayori_happy.png")
            self.timeHappy = 20
    
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
        self.offsetTY = 40
        self.offsetShopX = 0
        self.offsetShopY = 0
        self.o = 0

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
        self.strImage = "files/images/cookie.png"
        self.imageShop = pygame.image.load(self.strImage[:-4]+"x2"+self.strImage[-4:])
        self.rectShop = self.imageShop.get_rect()
        self.image = pygame.image.load("files/images/cookie.png")
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.o = 5
        self.rect.y = 370
        self.xShop = 20
        self.yShop = 100
        self.offsetTX = 11
        self.price = 10
        self.description1 = "Adoré de Sayori, ce sont"
        self.description2 = "des simples cookies"
    
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
        self.strImage = "files/images/the.png"
        self.imageShop = pygame.image.load(self.strImage[:-4]+"x2"+self.strImage[-4:])
        self.rectShop = self.imageShop.get_rect()
        self.image = pygame.image.load("files/images/the.png")
        self.rect = self.image.get_rect()
        self.rect.x = 90
        self.rect.y = 370
        self.offsetTX = 9
        self.xShop = 260
        self.yShop = 100
        self.price = 10
        self.description1 = "Une bonne tasse de thé"
        self.description2 = "préparée par Yuri"
    
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
        self.strImage = "files/images/juspomme.png"
        self.imageShop = pygame.image.load(self.strImage[:-4]+"x2"+self.strImage[-4:])
        self.rectShop = self.imageShop.get_rect()
        self.image = pygame.image.load("files/images/juspomme.png")
        self.rect = self.image.get_rect()
        self.rect.x = 220
        self.rect.y = 370
        self.xShop = 260
        self.yShop = 235
        self.price = 30
        self.offsetTX = 2
        self.description1 = "Contre les bosses à la tête"
        self.description2 = "venant des étagères"
        self.offsetShopX = 15
    
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
        self.strImage = "files/images/cupcake.png"
        self.imageShop = pygame.image.load(self.strImage[:-4]+"x2"+self.strImage[-4:])
        self.rectShop = self.imageShop.get_rect()
        self.image = pygame.image.load("files/images/cupcake.png")
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 370
        self.o = 5
        self.xShop = 20
        self.yShop = 235
        self.price = 30
        self.offsetTX = 11
        self.description1 = "Un cupcake adorable"
        self.description2 = "décoré par Natsuki"
    
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
        self.strImage = "files/images/gateau.png"
        self.imageShop = pygame.image.load(self.strImage[:-4]+"x2"+self.strImage[-4:])
        self.rectShop = self.imageShop.get_rect()
        self.image = pygame.image.load("files/images/gateau.png")
        self.rect = self.image.get_rect()
        self.rect.x = 270
        self.rect.y = 370
        self.xShop = 20
        self.yShop = 370
        self.o = 5
        self.price = 50
        self.offsetTX = 13
        self.offsetShopY = 15
        self.description1 = "Un gateau au chocolat"
        self.description2 = "préparé par Natsuki"
    
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
        self.strImage = "files/images/soda.png"
        self.imageShop = pygame.image.load(self.strImage[:-4]+"x2"+self.strImage[-4:])
        self.rectShop = self.imageShop.get_rect()
        self.image = pygame.image.load("files/images/soda.png")
        self.rect = self.image.get_rect()
        self.rect.x = 330
        self.rect.y = 370
        self.xShop = 260
        self.yShop = 370
        self.price = 50
        self.offsetTX = 4
        self.description1 = "Un bon vieux soda"
        self.description2 = "acheté par Monika"
        self.offsetShopX = 15
    
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
    
class Quitter(pygame.sprite.Sprite):
    def __init__(self):
        super(Quitter, self).__init__()
        self.type = "Quitter"
        self.image = pygame.image.load("files/images/buttonQ2.png")
        self.rect = self.image.get_rect()
        self.rect.x = 470-self.rect.width
        self.rect.y = 450

class Activites(pygame.sprite.Sprite):
    def __init__(self):
        super(Activites, self).__init__()
        self.type = "Activités"
        self.image = pygame.image.load("files/images/buttonA.png")
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 450

class TimeThread(threading.Thread):
    def __init__(self, girl):
        threading.Thread.__init__(self)
        self.girl = girl
    
    def run(self):
        while self.go:
            time.sleep(1)
            self.girl.time += 1
            if self.girl.time == 5:
                self.girl.modif("faim", -2)
                self.girl.modif("soif", -3)
                self.girl.modif("fun", -3)
                self.girl.time = 0
    
    def stopThread(self):
        self.go = False