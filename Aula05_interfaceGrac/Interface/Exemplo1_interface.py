#importação da biblioteca tkinter interface grafica
from tkinter import *
#tela = variavel ultilizada para receber a interface grafica
tela = Tk()
#titulo da tela
tela.title("Aula de interface")
#configure background para a cor de fundo
tela.configure(background="#1e3743")
#largura e altura
tela.geometry("700x300")
#redimensionar a tela
tela.resizable(True,True)
#dimensionar tamanho maximo
tela.maxsize(width=800,height=600)
tela.minsize(width=300,height=300)
#execute a tela
tela.mainloop()

