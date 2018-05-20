from tkinter import Tk, Canvas, Button, FLAT, CENTER, Radiobutton, StringVar
from PIL import Image, ImageTk
from tkinter.messagebox import showerror
import os, sys
try:
    from files.Game import Game
except ImportError:
    sys.path.append("files")
    from Game import Game

versionConfig = "2.0"

def SelectGirl(CHOICE, event= ""):
    game = ""
    if event.x >= 39 and event.x <= 149:
        if event.y >= 92 and event.y <= 190:
            game = Game("Natsuki")
        elif event.y >= 208 and event.y <= 340:
            game = Game("Yuri")
    elif event.x >= 250 and event.x <= 355:
        if event.y >= 92 and event.y <= 190:
            game = Game("Monika")
        elif event.y >= 208 and event.y <= 340:
            game = Game("Sayori")
    if game != "":
        CHOICE.destroy()
        game.launch()
        Main()


def SelectFen(FENETRE):
    FENETRE.destroy()
    CHOICE = Tk()

    CHOICE.title("DDLC's Friends")
    CHOICE.geometry("406x360")

    canvasWidth=600
    canvasHeight=400
    canvas=Canvas(CHOICE,width=canvasWidth,height=canvasHeight)
    backgroundImage=ImageTk.PhotoImage(Image.open("files/images/frame.png"))
    canvas.create_image(203, 180, image = backgroundImage)
    canvas.create_text(200, 20, text="Choisis ton amie de compagnie", font=("Times New Roman", 20, "bold"), fill = '#000000')
    nImage=ImageTk.PhotoImage(Image.open("files/images/natsuki.png").resize((100,114)))
    canvas.create_image(100, 140, image = nImage)
    mImage=ImageTk.PhotoImage(Image.open("files/images/monika.png").resize((100,141)))
    canvas.create_image(300, 130, image = mImage)
    yImage=ImageTk.PhotoImage(Image.open("files/images/yuri.png").resize((100,143)))
    canvas.create_image(100, 280, image = yImage)
    sImage=ImageTk.PhotoImage(Image.open("files/images/sayori.png").resize((100,142)))
    canvas.create_image(300, 280, image = sImage)
    canvas.bind("<Button-1>", lambda x: SelectGirl(CHOICE, x))
        
    canvas.pack()

    CHOICE.mainloop()

def Parametres(FENETRE):
    FENETRE.destroy()

    Param = Tk()
    Param.title("DDLC's Friends")
    Param.geometry("550x400")

    canvasWidth=600
    canvasHeight=400
    canvas=Canvas(Param,width=canvasWidth,height=canvasHeight)
    backgroundImage=ImageTk.PhotoImage(Image.open("files/images/frame.png").resize((550,400)))
    canvas.create_image(275, 200, image = backgroundImage)
    canvas.create_text(272, 30, text="Paramètres", font=("Times New Roman", 35, "bold"), fill = '#000000')
    canvas.create_text(100, 80, text="Image de mort", font=("Times New Roman", 15, "bold"), fill = '#000000')
    vals = ['0', '1']
    etiqs = ['Soft', 'Hard']
    varGr = StringVar()
    with open("files/config.txt", "r") as fichier:
        info = fichier.read().split("\n")
        mort = int(info[1].split(" : ")[1])
    varGr.set(vals[mort])
    for i in range(2):
        b = Radiobutton(Param, activebackground = "#ffe6f4", bg = "#ffe6f4",variable=varGr, text=etiqs[i], value=vals[i])
        canvas.create_window(65+i*70, 110, window = b)
    iExit = ImageTk.PhotoImage(Image.open("files/images/buttonQ.png"))
    bExit = Button(Param, command = lambda: PExit(Param,[varGr]), relief = FLAT, image = iExit)
    canvas.create_window(275, 370, window=bExit)
    
    canvas.pack()

    Param.mainloop()

def PExit(fenetre, valeurs):
    mort = valeurs[0].get()
    debug = valeurs[1].get()
    if mort == '1':
        showerror("ERREUR", "Ce type de mort n'a pas encore été implémenté")
    else:
        fenetre.destroy()
        with open("files/config.txt", "w") as fichier:
            texte = versionConfig+"\n"
            texte += "Image de Mort : "+mort+"\n"
            texte += "Debug : "+debug
            fichier.write(texte)
        Main()

def Main():
    FENETRE = Tk()
    FENETRE.title("DDLC's Friends")
    FENETRE.geometry("406x360")


    canvasWidth=600
    canvasHeight=400
    canvas=Canvas(FENETRE,width=canvasWidth,height=canvasHeight)
    backgroundImage=ImageTk.PhotoImage(Image.open("files/images/frame.png"))
    canvas.create_image(203, 180, image = backgroundImage)
    canvas.create_text(200, 50, text="DDLC's Friends", font=("Times New Roman", 35, "bold"), fill = '#000000')
    iJouer = ImageTk.PhotoImage(Image.open("files/images/buttonJ.png"))
    bJouer = Button(FENETRE, command = lambda: SelectFen(FENETRE), relief = FLAT, image = iJouer)
    canvas.create_window(200, 130, window=bJouer)
    iConfig = ImageTk.PhotoImage(Image.open("files/images/buttonP.png"))
    bConfig = Button(FENETRE, command = lambda: Parametres(FENETRE), relief = FLAT, image = iConfig)
    canvas.create_window(200, 200, window=bConfig)
    iExit = ImageTk.PhotoImage(Image.open("files/images/buttonQ.png"))
    bExit = Button(FENETRE, command = FENETRE.destroy, relief = FLAT, image = iExit)
    canvas.create_window(200, 270, window=bExit)
    nImage=ImageTk.PhotoImage(Image.open("files/images/natsuki.png").resize((100,114)))
    canvas.create_image(50, 190, image = nImage)
    mImage=ImageTk.PhotoImage(Image.open("files/images/monika.png").resize((100,141)))
    canvas.create_image(350, 180, image = mImage)
    canvas.create_text(200, 320, justify = CENTER, text="ATTENTION : \nCe jeu n'est pas affilié à Doki Doki Literature Club\nni à la Team Salvato", font=("Times New Roman", 12, "bold"), fill = '#ff0000')
    

    canvas.pack()

    FENETRE.mainloop()

if os.path.isdir('files/saves') == False:
    os.mkdir("files/saves")
try:
    with open("files/config.txt", "r") as fichier:
        if fichier.read().split("\n")[0] != versionConfig:
            raise FileExistsError
except:
    with open("files/config.txt", "w") as fichier:
        texte = versionConfig+"\n"
        texte += "Image de Mort : 0\n"
        texte += "Debug : 0"
        fichier.write(texte)
Main()