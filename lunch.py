# -*- coding: utf-8 -*-
import time, Tkinter, os, random
from Tkinter import *
# here is a range of programs like the color click (the first programs )
# yeah every where you can see some : :3, :3 I don't now why but it's cool :3 :3
# enjoy. Ho and I done this with the contribution of "mat1991". Fine. Bye :3

print "Bite"

#J'ai perdu toutes mes notions en python :o   Et ba bravo pour le print :P




  # first prog.
  # click on the square to make a rond with random color
def change_c(canvas) :
  global color     # made a random color :3
  couleurs=["blue","red","green","grey","yellow", "light yellow","light green","white","light blue"]
  i = random.randint(0,8)
  color = couleurs[i]
  canvas.itemconfig(cercle, fill=color)
  
  
def get_pos(event) :
  can.coords(cercle,event.x-r,event.y-r,event.x+r,event.y+r)
  change_c(can)

  
def create_round(x,y,r,color) :
  r = random.randint(10,20)
  can.create_oval(x-r,y-r,x+r,y+r,fill=color)
  
def create_square(x,y,r,color) :
  r = random.randint(10,20)
  z = x + r
  w = y + r
  can.create_rectangle(x,y,z,w,fill=color)
  
def create_text(x,y,color) :
  r = random.randint(10,20)
  can.create_text(x,y, text="spam!", font="Arial %i italic"%r, fill=color)

def create_new():
  global form
  x = random.randint(1,300)
  y = random.randint(1,300)
  r = 20
  change_c(can)
  if form == 1 :
    create_round(x,y,r,color)
  elif form == 2 :
    create_square(x,y,r,color)
  elif form == 3 :
    create_text(x,y,color)
  else :
    form = 1
    create_round(x,y,r,color)

def clear() : # this button not work, when you click on it you can't move the cercle
  can.delete(ALL)
  cercle = can.create_oval(x, y, x+30, y+30, width=2, fill=color)
  can.bind("<Button-1>",get_pos)

def change_fo() :
  global form
  form += 1

def rond_color() :
  global x,y,r,fen,can,cercle,form
  x,y,r,form=10,10,10,1
  fen = Tkinter.Tk()
  fen.title("Color clic")
  quit = Button(text="quit", command=fen.destroy, height=3, width=5 )
  aleat = Button(text="add", command=create_new, height=3, width=5 )
  clean = Button(text="clean", command=clear, height=2, width=5)
  change_f = Button(text="change form", command=change_fo, height=3, width=7)
  can = Canvas(fen, width=300, height=300, bg="black" )
  color="white"
  cercle = can.create_oval(x, y, x+30, y+30, width=2, fill=color)
  change_c(can)
  can.bind("<Button-1>",get_pos)
  can.pack()
  quit.pack(side=LEFT)
  aleat.pack(side=RIGHT)
  clean.pack(side=RIGHT)
  change_f.pack(side=LEFT)
  fen.mainloop()
  menu()
  
  
def start_rond() :
  home.destroy()
  present = Tkinter.Tk()
  present.title("Color clic")
  text = Label(present, text="cliquez sur le carré pour faire apparaitre un rond de couleur aléatoire... // click on the black squarel to made a rond with a random color...")
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




















