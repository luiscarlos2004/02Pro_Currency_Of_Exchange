from re import L
import tkinter
from tkinter import *
from turtle import bgcolor, width
from funcion import porcentaje
from tkinter import messagebox

app = Tk()
app.title('App for calc')
app.geometry('700x600')
app.config(bg='#BFD9C9')
img = PhotoImage(file = "cambio2.png", width=255, height=250)
label = Label(app, image=img)
label.place(x = 200, y = 30)
amount = Entry(app, width=32)
amount.place(x = 180, y=340)
def limpiar():
    amount.delete(0,'end')
   
types = ('Usd','Cls')
types_var = StringVar(value=types)
listBox = Listbox(app,listvariable=types_var,height=2,selectmode='extended')
listBox.place(x = 240, y = 400)

def mensaje():
    amount1 = amount.get()
    precio = int(amount1) * 5
    labelprecio = Label(app, text=precio)
    labelprecio.place(x = 200 , y = 600)
    alerta = messagebox.askretrycancel(message="Desea continuar", title="Título")
    if alerta == True:
        limpiar()
        index = listBox.curselection()
        selected = listBox.get(index)
        valor = porcentaje(selected,amount1)
        la = Label(app,text=valor)
        la.place(x = 300, y = 550)
    # limpiar()

send = Button(app,text="Send", command=mensaje)

send.place(x = 250, y= 490, width=150)

app.mainloop()