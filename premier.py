# tests ici
import time, Tkinter, os, random, pygame
from Tkinter import *
# a completer x)
# Bon fait ce que tu veut  moi j'fais un jeu de carte avec python :3 je te montrerais si tu veut P.S: suprimme cette ligne.
# Propose qq chose je sait pas quoi faire :/




  # theoriquement ca fait un rond d'une couleur aléatoire la ou tu clique :3
def change_c() :
  global color     # choix d'une couleurs aléatoire :3
  couleurs=["blue","red","green","grey","black"]
  i = random.randint(0,4)
  color = couleurs[i]
  
def get_pos(event) :
  can.coords(oval,event.x-r,event.y-r,event.x+r,event.y+r) 

  
def create(x,y,r,color) :
  can1.create_oval(x-r,y-r,x+r,y+r,outline=color) # creation du cercle avec les couleurs et la position pre-definit...
  

x,y,r=10,10,10
fen = Tkinter.Tk()
fen.title("Color clic")
can = Canvas(fen, width=100, height=100, bg="black" )
can.bind("<Button-1>",getpos)
change_c()
can.pack()
fen.mainloop() 


