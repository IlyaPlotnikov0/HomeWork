from tkinter import *
from tkinter import ttk
from random import randint

WIDTH = 300
HEIGHT = 200


class Ball:
    def __init__(self, color = "#"+('%06x'%randint(0,16777215))):
        self.R = randint(10, 50) 
        self.x = randint(self.R, WIDTH - self.R) 
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx, self.dy = (10, 10) 
        self.ball_id = canvas.create_oval(self.x - self.R,
                                     self.y - self.R,
                                     self.x + self.R,
                                     self.y + self.R, fill=color) 

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > canvas.winfo_width() or self.x - self.R <= 0: 
            self.dx = -self.dx
        if self.y + self.R > canvas.winfo_height() or self.y - self.R <= 0: 
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def click_handler(event):
    print('Hello World! x=', event.x, 'y=', event.y)
    balls.append(Ball(color = "#"+('%06x'%randint(0,16777215))))
    


def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(100, tick)


root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
canvas = Canvas(root)
canvas.pack(fill = BOTH,expand = True)

canvas.bind('<Button-1>', click_handler)
balls = [Ball() for i in range(5)]
tick()
root.mainloop()
