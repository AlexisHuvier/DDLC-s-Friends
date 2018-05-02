import pygame, random
import tkinter
from PIL import Image
from tkinter.messagebox import showerror
try:
    from files.Class import Monika, Yuri, Natsuki, Sayori, Cookie, Soda, JusPomme, The, Cupcake, Gateau, Shop
except ImportError:
    from Class import Monika, Yuri, Natsuki, Sayori

class Game():
    def __init__(self, girlChoosed):
        pygame.init()
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
        self.inventory = [Cookie(), The(), Cupcake(), JusPomme(), Gateau(), Soda(), Shop()]
        self.font=pygame.font.SysFont("Times New Roman",22,bold=True,italic=False)
        self.played = True
        self.screen = pygame.display.set_mode((500, 500))

        self.clock = pygame.time.Clock()
        pygame.display.set_caption("DDLC's Friends - "+self.girl.name)

    def launch(self):
        while self.played:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    for i in self.inventory:
                        if i.type != "Shop":
                            i.add(1)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                    self.girl.vie = 10
                    self.girl.faim = 10
                    self.girl.fun = 10
                    self.girl.soif = 10
                if event.type == pygame.QUIT:
                    self.played = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouseEvent(event.button, event.pos)
            self.screen.fill((0, 0, 0))
            for i in self.girlGroup:
                i.move()
                if self.timeDirection == 0:
                    i.direction = random.randint(1,8)
                    self.timeDirection = 20
                else:
                    self.timeDirection -= 1
            self.showImage()
            self.clock.tick(60)
            pygame.display.update()
        pygame.quit()

    def mouseEvent(self, button, pos):
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
                            print("SHOP")

    def showImage(self):
        self.girlGroup.draw(self.screen)
        content = pygame.image.load("files/images/barre_contenu.png")
        self.screen.blit(pygame.transform.scale(content, (self.girl.vie, 6)), (25, 21))
        self.screen.blit(pygame.transform.scale(content, (self.girl.fun, 6)), (25, 51))
        self.screen.blit(pygame.transform.scale(content, (self.girl.faim, 6)), (411+(65-self.girl.faim), 21))
        self.screen.blit(pygame.transform.scale(content, (self.girl.soif, 6)), (411+(65-self.girl.soif), 51))
        text=self.font.render(self.girl.name,1,(250, 240, 230))
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
                text=self.font.render(str(i.nombre),1,(0, 0,0))
                self.screen.blit(text, (i.rect.x + i.offsetTX, i.rect.y + i.offsetTY))
        pygame.draw.rect(self.screen,(255, 189, 225),(380,360,4,70))