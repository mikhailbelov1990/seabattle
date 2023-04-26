from tkinter import *
import time
import field
import belovFleet

root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()
canvas.create_rectangle(0, 0, 500, 500,
                        outline='green', fill='white')
field.drawField(canvas)
field.placeShips()

while not field.isGameOver():
    coord = belovFleet.shoot()
    x = coord[0]
    y = coord[1]
    kill = field.shoot(x, y, canvas)
    belovFleet.observe(x, y, kill)
    canvas.update()
    time.sleep(0.5)#поминяу

field.showGameOver()
