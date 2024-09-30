from tkinter import *

tela = Tk()

tela.title("Exemplo Checkbox")
tela.geometry("700x600")

def mostrar():
    Label(tela, text=var.get()).pack()

var = StringVar()

chk_button = Checkbutton(tela, text="CheckBox", variable=var, onvalue="ON", offvalue="OFF")
chk_button.deselect()
chk_button.pack(anchor=CENTER)

Button(tela, text="Mostrar", command=mostrar).pack()

tela.mainloop()
