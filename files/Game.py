import pygame, random
import tkinter
from PIL import Image
from tkinter.messagebox import showerror, askquestion
try:
    from files.Class import Monika, Yuri, Natsuki, Sayori, Cookie, Soda, JusPomme, The, Cupcake, Gateau, Shop
except ImportError:
    from Class import Monika, Yuri, Natsuki, Sayori

class Game():
    def __init__(self, girlChoosed):
        pygame.init()
        self.inventory = [Cookie(), The(), Cupcake(), JusPomme(), Gateau(), Soda()]
        if girlChoosed == "Monika":
            self.girl = Monika(self)
        elif girlChoosed == "Yuri":
            self.girl = Yuri(self)
        elif girlChoosed == "Sayori":
            self.girl = Sayori(self)
        elif girlChoosed == "Natsuki":
            self.girl = Natsuki(self)
        else:
            raise Exception
        self.girlGroup = pygame.sprite.Group()
        self.fen = "Game"
        self.girlGroup.add(self.girl)
        self.timeDirection = 20
        self.debug = False
        self.fontName=pygame.font.SysFont("Times New Roman",22,bold=True,italic=False)
        self.fontDesc=pygame.font.SysFont("Times New Roman",15,bold=False,italic=False)
        self.fontDesc2=pygame.font.SysFont("Times New Roman",12,bold=False,italic=False)
        self.played = True
        self.screen = pygame.display.set_mode((500, 500))

        self.clock = pygame.time.Clock()
        pygame.display.set_caption("DDLC's Friends - "+self.girl.name)

    def launch(self):
        while self.played:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a and self.debug:
                    for i in self.inventory:
                        if i.type != "Shop":
                            i.add(1)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_g and self.debug:
                    self.girl.addMoney(10)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_l and self.debug:
                    self.girl.vie = 10
                    self.girl.faim = 10
                    self.girl.fun = 10
                    self.girl.soif = 10
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d: 
                    tk = tkinter.Tk()
                    if self.debug:
                        if askquestion("Debug", "Voulez-vous quitter le mode debug ?") == "yes":
                            self.debug = False
                    else:
                        if askquestion("Debug", "Voulez-vous passer en mode debug ?") == "yes":
                            self.debug = True
                    tk.destroy()
                if event.type == pygame.QUIT:
                    self.played = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.fen == "Game":
                        self.mouseEventGame(event.button, event.pos)
                    elif self.fen == "Shop":
                        self.mouseEventShop(event.button, event.pos)
            self.screen.fill((0, 0, 0))
            if self.fen == "Game":
                for i in self.girlGroup:
                    i.move()
                    if self.timeDirection == 0:
                        i.direction = random.randint(1,8)
                        self.timeDirection = 20
                    else:
                        self.timeDirection -= 1
                self.showImageGame()
            elif self.fen == "Shop":
                self.showImageShop()
            self.clock.tick(60)
            pygame.display.update()
        pygame.quit()

    def mouseEventShop(self, button, pos):
        if button==1:
            posX = pos[0]
            posY = pos[1]
            find = ""
            objet = None
            for i in self.inventory:
                if i.type != "Shop":
                    if posX >= i.xShop and posX<= i.xShop+i.rectShop.width:
                        if posY >= i.yShop and posY<= i.yShop+i.rectShop.height:
                            find = i.type
                            objet = i
            if find != "":
                if self.girl.pay(objet.price):
                    temp = tkinter.Tk()
                    showerror("ERREUR", "Vous n'avez pas assez de monnaie ("+str(objet.price)+").")
                    temp.destroy()
                else:
                    objet.add(1)
            else:
                self.fen = "Game"
        
    def showImageShop(self):
        backgroundImage=pygame.image.load("files/images/frame.png")
        self.screen.blit(pygame.transform.scale(backgroundImage, (500, 500)), (0, 0))
        text=self.fontName.render("Shop",1,(0, 0, 0))
        text_rect = text.get_rect(center=(500/2, 20))
        self.screen.blit(text, text_rect)
        argent=self.fontDesc.render(str(self.girl.coin),1,(0, 0,0))
        argent_rect = argent.get_rect(center=(500/2, 50))
        self.screen.blit(argent, (argent_rect.x-8, argent_rect.y))
        self.screen.blit(pygame.image.load("files/images/coin.png"), (argent_rect.x+2+argent_rect.width, argent_rect.y))
        for i in self.inventory:
            self.screen.blit(i.imageShop, (i.xShop+i.offsetShopX, i.yShop+i.offsetShopY))
            nom=self.fontDesc.render(i.type,1,(0, 0,0))
            self.screen.blit(nom, (i.xShop + 70, i.yShop))
            description=self.fontDesc2.render(i.description1,1,(0, 0,0))
            self.screen.blit(description, (i.xShop + 70, i.yShop+20))
            description2=self.fontDesc2.render(i.description2,1,(0, 0,0))
            self.screen.blit(description2, (i.xShop + 70, i.yShop+35))
            price=self.fontDesc.render(str(i.price),1,(0, 0,0))
            self.screen.blit(price, (i.xShop-8+i.o+i.offsetShopX+i.rectShop.width/4, i.yShop+70))
            self.screen.blit(pygame.image.load("files/images/coin.png"), (i.xShop+13+i.o+i.offsetShopX+i.rectShop.width/4, i.yShop+70))
            possede=self.fontDesc.render("Possédé : "+str(i.nombre),1,(0, 0,0))
            self.screen.blit(possede, (i.xShop + 70, i.yShop+70))



    def mouseEventGame(self, button, pos):
        if button==1:
            posX = pos[0]
            posY = pos[1]
            for i in self.inventory:
                if posX >= i.rect.x and posX<= i.rect.x+i.rect.width:
                    if posY >= i.rect.y and posY<= i.rect.y+i.rect.height:
                        if i.type != "Shop":
                            if i.consomme(self.girl):
                                temp = tkinter.Tk()
                                showerror("ERREUR", "Vous n'avez pas de "+i.type+".")
                                temp.destroy()
                        else:
                            self.fen = "Shop"

    def showImageGame(self):
        self.girlGroup.draw(self.screen)
        content = pygame.image.load("files/images/barre_contenu.png")
        self.screen.blit(pygame.transform.scale(content, (self.girl.vie, 6)), (25, 21))
        self.screen.blit(pygame.transform.scale(content, (self.girl.fun, 6)), (25, 51))
        self.screen.blit(pygame.transform.scale(content, (self.girl.faim, 6)), (411+(65-self.girl.faim), 21))
        self.screen.blit(pygame.transform.scale(content, (self.girl.soif, 6)), (411+(65-self.girl.soif), 51))
        text=self.fontName.render(self.girl.name,1,(250, 240, 230))
        text_rect = text.get_rect(center=(500/2, 20))
        self.screen.blit(text, text_rect)
        frame = pygame.image.load("files/images/frame.png")
        self.screen.blit(pygame.transform.scale(frame, (500, 70)), (0,430))
        self.screen.blit(pygame.transform.scale(frame, (500, 70)), (0,360))
        self.screen.blit(pygame.image.load("files/images/barre_vie.png"), (10, 10))
        self.screen.blit(pygame.image.load("files/images/barre_fun.png"), (10, 40))
        self.screen.blit(pygame.image.load("files/images/barre_faim.png"), (406, 10))
        self.screen.blit(pygame.image.load("files/images/barre_soif.png"), (406, 40))
        for i in self.inventory:
            self.screen.blit(i.image, (i.rect.x, i.rect.y))
            if i.type !="Shop":
                text=self.fontDesc.render(str(i.nombre),1,(0, 0,0))
                self.screen.blit(text, (i.rect.x + i.offsetTX, i.rect.y + i.offsetTY))
        pygame.draw.rect(self.screen,(255, 189, 225),(380,360,4,70))