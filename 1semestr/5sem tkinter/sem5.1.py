from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        res = eval(vvod.get())  
        output.set(res)  
    except:
        output.set("ЧИСЛА ПОДАВАЙ ИЛИ НЕ ДЕЛИ НА 0)")

root = Tk()
root.title("КАЛЬКУЛЯТОР")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

vvod = StringVar()
entry_vvod = ttk.Entry(mainframe, width=20, textvariable=vvod)
entry_vvod.grid(column=2, row=1, sticky=(W, E))

output = StringVar()
ttk.Label(mainframe, textvariable=output).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="ПОСЧИТАТЬ", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="ВВОД").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="ОТВЕТ:").grid(column=1, row=2, sticky=E)

root.bind("<Return>", calculate)
entry_vvod.focus()

root.mainloop()
