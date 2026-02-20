from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        col = color.get()
        color_mach = '#'
        for i in range(1,6,2):
            x = int(col[i:i+2], 16)
            y = (hex(255-x))[2:]
            color_mach += y
        output.set(color_mach)
        print(color_mach)
    except:
        output.set("ОШИБКА")

    root2 = Tk()
    root2.title("КОМПЛЕМЕНТАРГАЯ ПАРА")
    root2.geometry('400x200')
    c = Canvas(root2,width=400,height=200, bg='white')
    c.pack()
    c.create_rectangle(0,0,200,200,fill=col)
    c.create_rectangle(200,200,400,0,fill=color_mach)    

root = Tk()
root.title("ПОДБОР ЦВЕТОВ")

mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

color = StringVar()
entry_color = ttk.Entry(mainframe, width=20, textvariable=color)
entry_color.grid(column=2, row=1, sticky=(W, E))

output = StringVar()
ttk.Label(mainframe, textvariable=output).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Подобрать цвет", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Введи код цвета").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Код комплементарного цвета:").grid(column=1, row=2, sticky=E)

root.bind("<Return>", calculate)
entry_color.focus()


root.mainloop()


