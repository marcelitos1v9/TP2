
from tkinter import *
from PIL import Image, ImageTk


tela = Tk()
tela.title("BOTÕES")
tela.geometry("600x300")

tela.iconbitmap(r"C:/Users/fatec-dsm3/Pictures/icone.ico")
foto_salvar = PhotoImage(file = r"icones\salvar.png")
foto_excluir = PhotoImage(file = r"icones\excluir.png")
foto_alterar = PhotoImage(file = r"icones\alterar.png")
foto_consultar = PhotoImage(file = r"icones\consultar.png")
foto_sair = PhotoImage(file = r"icones\sair.png")

btn_salvar =  Button(tela, text="Salvar", image= foto_salvar ,compound=TOP )
btn_salvar.place(x=130,y=30)  
btn_excluir = Button(tela, text="Excluir", image=foto_excluir, compound=TOP)
btn_excluir.place(x=200,y=30)
btn_alterar =  Button(tela, text="Alterar", image= foto_alterar ,compound= TOP )
btn_alterar.place(x=270,y=30)  
btn_consultar = Button(tela, text="Consultar", image=foto_consultar, compound=TOP)
btn_consultar.place(x=340,y=30)
btn_sair = Button(tela, text="Sair", image=foto_sair, compound=RIGHT)
btn_sair.place(x=420,y=30)

tela.mainloop()