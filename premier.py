# tests ici
import time, Tkinter, os, random
from Tkinter import *
# a completer x)
# Bon fait ce que tu veut  moi j'fais un jeu de carte avec python :3 je te montrerais si tu veut P.S: suprimme cette ligne.
# Propose qq chose je sait pas quoi faire :/
# Et fait autre chose :) moi je viens de faire qq chose montre moi c que tu peut faire



  # ca fait un rond d'une couleur aléatoire la ou tu clique :3
def change_c(canvas) :
  global color     # choix d'une couleurs aléatoire :3
  couleurs=["blue","red","green","grey","yellow", "light yellow"]
  i = random.randint(0,4)
  color = couleurs[i]
  canvas.itemconfig(cercle, fill=color)
  
  
def get_pos(event) :
  can.coords(cercle,event.x-r,event.y-r,event.x+r,event.y+r)
  change_c(can)

  
def create(x,y,r,color) :
  can1.create_oval(x-r,y-r,x+r,y+r,outline=color) # creation du cercle avec les couleurs et la position pre-definit...
  

def rond_color() :
  global x,y,r,fen,can,cercle
  x,y,r=10,10,10
  fen = Tkinter.Tk()
  fen.title("Color clic")
  can = Canvas(fen, width=300, height=300, bg="black" )
  color="white"
  cercle = can.create_oval(x, y, x+30, y+30, width=2, fill=color)
  change_c(can)
  can.bind("<Button-1>",get_pos)
  can.pack()
  fen.mainloop()
  
  
def start_rond() :
  home.destroy()
  present = Tkinter.Tk()
  present.title("Color clic")
  text = Label(present, text="cliquez sur le carré pour faire apparaitre un rond de couleur aléatoire...")
  contin = Button(present, text="continuer", command=present.destroy, height=2, width=4 )
  text.pack()
  contin.pack()
  present.mainloop()
  rond_color()
# voila...

# menu des jeux :3
global home
home = Tkinter.Tk()
home.title("Home")
quit = Button(text="Quitter", command=home.destroy, width=10, height=5)
rond = Button(text="Rond aléatoire", command=start_rond, width=10, height=5)
quit.pack(side=RIGHT)
rond.pack(side=LEFT)
home.mainloop()




