
from tkinter import *
master = Tk()
canvas_width = 800
canvas_height = 60
canvas  = Canvas(master, width=canvas_width, height = canvas_height)
splitX = 88
splitY = 6
gapx = int (canvas_width // splitX)
gapy = int(canvas_height // splitY)

for idx in range(1, splitY):
    canvas.create_line(0, idx * gapy, canvas_width, idx * gapy, fill='#476042')

for idx in range(1, splitX):
    canvas.create_line(idx * gapx, 0, idx *gapx, canvas_height, dash=1)
canvas.pack()

def mouseRight(event):
    localx = event.x
    #localy = event.y
    idx = localx // gapx
    piano_play(idx)

import Piano
def piano_play(idx):
    pianoPlay = Piano.Player() 
    pianoPlay.play(idx)

canvas.bind("<Button-1>", mouseRight)
mainloop()