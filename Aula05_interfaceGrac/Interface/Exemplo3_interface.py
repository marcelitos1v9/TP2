from tkinter import *

tela = Tk()
tela.title("Aula de interface")
tela.configure(background="#1e3743")

largura = 800
altura = 600

# Definir que a tela comece de forma centralizada
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx = (largura_screen // 2) - (largura // 2)
posy = (altura_screen // 2) - (altura // 2)

tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

lbl_nome = Label(tela, text="Nome: ", font="Arial 25 bold italic")
lbl_nome.place(x=10,y=10)

lbl_endereco = Label(tela,text="Endereço",font=("Comic Sans MS",'20','bold'))
lbl_endereco.place(x=50,y=60)
                     
tela.mainloop()
