from tkinter import*

tela = Tk()

tela.title("Exemplo Radio button")
tela.geometry("700x600")

var = StringVar()

var.set("m")

rdb_buttonM = Radiobutton(tela, text="Masculino", variable=var, value="m")
rdb_buttonM.place(x=20,y=40)

rdb_buttonF = Radiobutton(tela, text="Feminino", variable=var, value="f")
rdb_buttonF.place(x=20,y=70)

tela.mainloop()