# tests ici
import time, Tkinter, os, random
from Tkinter import *
from Tkinter.messagebox import *
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
  global home
  home.destroy
  present = Tkinter.Tk()
  present.title("Color clic")
  text = Label(text="cliquez sur le carré pour faire apparaitre un rond de couleur aléatoire...")
  contin = Button(text="continuer", command=present.destroy )
  text.pack()
  contin.pack()
  present.mainloop()
  rond_color()
# voila...
def quit_home() :
  d = 1
d = 0
while d == 0 :
# menu des jeux :3
global home
home = Tk()
home.title("Home")
quit = Button(text="Quitter", command=quit_home(), width=50, height=20)
rond = Button(text="Rond aléatoire", command=start_rond(), width=50, height=20)





