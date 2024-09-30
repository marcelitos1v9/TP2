from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

tela = Tk()

tela.title("Exemplo Combo Box")
tela.geometry("250x250")

def mostrar():
    messagebox.showwarning("Titulo da mensagem", combo.get())

combo = Combobox(tela)
combo['values'] = ("Iguape", "Balneário", "Florianópolis", "São José")
combo.current(3) 
combo.pack()

Button(tela, text="Selecionar", command=mostrar).pack()

tela.mainloop()


