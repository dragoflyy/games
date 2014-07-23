
import time, Tkinter, os, random
from Tkinter import *
# here is a 

print("Bite")
#J'ai perdu toutes mes notions en python :o




  # first prog.
  # click on the square to make a rond with random color
def change_c(canvas) :
  global color     # made a random color :3
  couleurs=["blue","red","green","grey","yellow", "light yellow"]
  i = random.randint(0,4)
  color = couleurs[i]
  canvas.itemconfig(cercle, fill=color)
  
  
def get_pos(event) :
  can.coords(cercle,event.x-r,event.y-r,event.x+r,event.y+r)
  change_c(can)

  
def create(x,y,r,color) :
  can.create_oval(x-r,y-r,x+r,y+r,fill=color)

def create_new():
  x = random.randint(1,300)
  y = random.randint(1,300)
  r = 20
  change_c(can)
  create(x,y,r,color)

def rond_color() :
  global x,y,r,fen,can,cercle
  x,y,r=10,10,10
  fen = Tkinter.Tk()
  fen.title("Color clic")
  quit = Button(text="quit", command=fen.destroy, height=3, width=5 )
  aleat = Button(text="add", command=create_new, height=3, width=5 )
  can = Canvas(fen, width=300, height=300, bg="black" )
  color="white"
  cercle = can.create_oval(x, y, x+30, y+30, width=2, fill=color)
  change_c(can)
  can.bind("<Button-1>",get_pos)
  can.pack()
  quit.pack(side=LEFT)
  aleat.pack(side=RIGHT)
  fen.mainloop()
  menu()
  
  
def start_rond() :
  home.destroy()
  present = Tkinter.Tk()
  present.title("Color clic")
  text = Label(present, text="cliquez sur le carré pour faire apparaitre un rond de couleur aléatoire... /n click on the black squarel to made a rond with a random color...")
  contin = Button(present, text="continue", command=present.destroy, height=2, width=4 )
  text.pack()
  contin.pack()
  present.mainloop()
  rond_color()
# ...

def menu() : # home of games :3
  global home
  home = Tkinter.Tk()
  home.title("Home")
  quit = Button(text="Quit", command=home.destroy, width=10, height=5)
  rond = Button(text="random rond", command=start_rond, width=10, height=5)
  quit.pack(side=RIGHT)
  rond.pack(side=LEFT)
  home.mainloop()

menu()










