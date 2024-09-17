from tkinter import *

tela = Tk()
tela.title("Aula de interface")
tela.configure(background="#1e3743")

largura = 800
altura = 300

# Definir que a tela comece de forma centralizada
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx = (largura_screen // 2) - (largura // 2)
posy = (altura_screen // 2) - (altura // 2)

tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

#definindo as entradas
txt_nome = Entry(tela,width=40,borderwidth=5,fg="blue",bg="white")

txt_nome.pack()
#define o que será escrito na caixa de texto
txt_nome.insert(0,"")

def mostrar_msg():
    lbl_msg = Label(tela,text="Bem vindo "+txt_nome.get())
    lbl_msg.place(x=80,y=100)
    
#criando boto que chama a função
btn_button = Button(tela,text="Aperte aqui!",command=mostrar_msg)
btn_button.pack()

tela.mainloop()
