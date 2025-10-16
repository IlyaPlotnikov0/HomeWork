import tkinter as tk
from tkinter import ttk

def calculate():
   try:
        w = float(weight.get())
        h = float(height.get())
        bmi = round(w/(h**2),1)

        if bmi <= 16:
            res = "Выраженный дефицит массы тела"
        elif bmi <= 18.5:
            res = "Недостаточная масса тела"
        elif bmi <= 25:
            res = "Норма"
        elif bmi <= 30:
            res = "Предожирение"
        elif bmi <= 35:
            res = "Ожирение 1 степени"
        elif bmi <= 40:
            res = "Ожирение 2 степени"
        else:
            res = "Ожирение 3 степени"
        result.config(text=f"ИМТ = {bmi} \n {res}")
   except:
        result.config(text="ОШИБКА")

root = tk.Tk()
root.title("Калькулятор ИМТ")
root.geometry("400x200")

tk.Label(root, text="Вес, кг:").pack()
weight = tk.Entry(root)
weight.pack()

tk.Label(root, text="Рост, м:").pack()
height = tk.Entry(root)
height.pack()

tk.Button(root, text="Узнать результат", command=calculate).pack(pady=15)

result = tk.Label(root, text="", fg='black', font='Montserrat 12 bold')
result.pack()

weight.focus()

root.mainloop()
