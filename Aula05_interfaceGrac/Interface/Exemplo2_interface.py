from tkinter import *
tela = Tk()
tela.title("Aula de interface")
tela.configure(background="#1e3743")
tela.geometry("700x500")
#como colocar uma label na tela de interface
lbl_nome = Label(tela,text="Nome",bg="black",fg="white").place(x=10,y=20)
entrada_nome = Entry(tela,width=50).place(x=100,y=20)

lbl_tel = Label(tela,text="Telefone",bg="black",fg="white").place(x=10,y=60)
entrada_tel = Entry(tela,width=50).place(x=100,y=60)
tela.mainloop()

