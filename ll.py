from tkinter import *
from PIL import Image,ImageTk
from random import randint, choices

#main fereastra
root= Tk()
root.title("Rock Scissors Paper")                                   #titlu fereastra
root.configure(background= "purple")                                #schimb culoarea background-ului(pt mov cod #9b59b6)

#pentru poze (instalare pip in terminal)
piatra_img = ImageTk.PhotoImage(Image.open("piatra.png"))
hartie_img = ImageTk.PhotoImage(Image.open("hartie.png"))
foarfeca_img = ImageTk.PhotoImage(Image.open("foarfeca.png"))

#poze prima perspectiva(mai un set de 3 poze pt perspectiva2)
piatra_img_comp = ImageTk.PhotoImage(Image.open("piatra_2.png"))
hartie_img_comp = ImageTk.PhotoImage(Image.open("hartie_2.png"))
foarfeca_img_comp = ImageTk.PhotoImage(Image.open("foarfeca_2.png"))

#inseram pozele
jucator1_label = Label(root, image = piatra_img,bg="purple")                #bg pt fundal mov
jucator2_label = Label(root, image = piatra_img_comp,bg="purple")
jucator2_label.grid(row=1 , column=0)                                   #punem pozele in fereastra(piatra_2.png in stanga)
jucator1_label.grid(row=1, column =4)                                       #piatra.png in dreapta

#pentru scor
jucator1Scor = Label(root,text =0, font =100,bg="purple", fg="white")
jucator2Scor = Label(root, text=0,font =100,bg="purple", fg="white" )
jucator2Scor.grid(row=4,column=1)
jucator1Scor.grid(row=4,column=3)

#indicatori
jucator1_indicator = Label(root, font=50, text ="Jucator 1",bg="purple", fg="white")
jucator2_indicator = Label(root, font=50, text="Jucator 2",bg="purple", fg="white")
jucator1_indicator.grid(row=0 , column=3 )
jucator2_indicator.grid(row=0 , column=1 )

#mesajele
mesaje = Label(root,font =50, bg="purple", fg="white")                     #, text = "Ai pierdut!")
mesaje.grid(row=5, column=2)

#actualizarea mesajului
def actualiz_Mesaj(x):
    mesaje ['text'] = x

#actualizarea PLAYER1

def actualiz_P1scor():                                                       #scorul jucatorului1
     scor = int(jucator1Scor["text"])
     scor = scor+1
     jucator1Scor["text"] = str(scor)

#actualizarea scorului PLAYER2

def actualiz_P2scor():                                                        #scorul /player2
    scor = int(jucator2Scor["text"])
    scor = scor+1
    jucator2Scor["text"] = str(scor)

#verificam castigatorul

def verif_castigator(jucator1, jucator2):
    if jucator1 == jucator2:
        actualiz_Mesaj("Este egalitate!")
    elif jucator1 == "piatra":
        if jucator2 == " hartie":
            actualiz_Mesaj("Jucatorul 1 a pierdut!")
            actualiz_P2scor()
        else:
            actualiz_Mesaj("Jucatorul 1 a castigat!")
            actualiz_P1scor()
    elif jucator1 == "hartie":
        if jucator2 =="foarfeca":
            actualiz_Mesaj("Jucatorul 1 a pierdut!")
            actualiz_P2scor()
        else:
            actualiz_Mesaj("Jucatorul 1 a castigat!")
            actualiz_P1scor()
    elif jucator1 == "foarfeca":
        if jucator2 == "piatra":
            actualiz_Mesaj("Jucatorul 1 a pierdut!")
            actualiz_P2scor()
        else:
            actualiz_Mesaj("Jucatorul 1 a castigat!")
            actualiz_P1scor()
    else:
        pass   # nu vrem sa facem nimic
    if jucator2 == jucator1:
        actualiz_Mesaj("Este egalitate!")
    elif jucator2 == "piatra":
        if jucator1 == " hartie":
            actualiz_Mesaj("Jucatorul 2 a pierdut!")
            actualiz_P1scor()
        else:
            actualiz_Mesaj("Jucatorul 2 a castigat!")
            actualiz_P2scor()
    elif jucator2 == "hartie":
        if jucator1 =="foarfeca":
            actualiz_Mesaj("Jucatorul 2 a pierdut!")
            actualiz_P1scor()
        else:
            actualiz_Mesaj("Jucatorul 2 a castigat!")
            actualiz_P2scor()
    elif jucator2 == "foarfeca":
        if jucator1 == "piatra":
            actualiz_Mesaj("Jucatorul 2 a pierdut!")
            actualiz_P1scor()
        else:
            actualiz_Mesaj("Jucatorul 2 a castigat!")
            actualiz_P2scor()
    else:
        pass



def realege2(y):
    jucator1=["piatra","foarfeca","hartie"]
#realegerea unei optiuni a computerului/player2
    if y == "piatra":
        jucator2_label.configure(image=piatra_img_comp)
    elif y == "hartie":
        jucator2_label.configure(image=hartie_img_comp)
    else:
        jucator2_label.configure(image=foarfeca_img_comp)
    verif_castigator(y, jucator1)

def realege1(x):
#realegerea unei optiuni pt jucator 1
    jucator2=["piatra","foarfeca","hartie"]
    if x=="piatra":
        jucator1_label.configure(image=piatra_img)
    elif x=="hartie":
       jucator1_label.configure(image=hartie_img)
    else:
        jucator1_label.configure(image=foarfeca_img)
    verif_castigator(x, jucator2)


#butoane de selectare
piatra = Button(root,width=20, height=2, text="PIATRA", bg="orange", fg="white",command = lambda:realege1("piatra"))
hartie = Button(root,width=20, height=2, text="HARTIE", bg="green", fg="white",command = lambda:realege1("hartie"))
foarfeca = Button(root,width=20, height=2, text="FOARFECA", bg="blue", fg="white",command = lambda:realege1("foarfeca"))
piatra_2 = Button(root,width=20, height=2, text="PIATRA", bg="orange", fg="white",command = lambda:realege2("piatra"))
hartie_2 = Button(root,width=20, height=2, text="HARTIE", bg="green", fg="white",command = lambda:realege2("hartie"))
foarfeca_2 = Button(root,width=20, height=2, text="FOARFECA", bg="blue", fg="white",command = lambda:realege2("foarfeca"))
piatra.grid(row=2,column=1)
hartie.grid(row=2,column=2)
foarfeca.grid(row=2,column=3)
piatra_2.grid(row=1,column=1)
hartie_2.grid(row=1,column=2)
foarfeca_2.grid(row=1,column=3)


root.mainloop()