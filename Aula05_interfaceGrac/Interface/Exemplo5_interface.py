from tkinter import *

tela = Tk()

tela.title("Cálculo Soma")
tela.geometry("700x500")  # Corrigido para definir o tamanho da janela

lbl_num1 = Label(tela, text="Digite um número: ", font="Arial 15 bold")
lbl_num1.place(x=50, y=45)

txt_num1 = Entry(tela, width=20, borderwidth=10, fg="blue", bg="white")
txt_num1.place(x=280, y=45)

lbl_num2 = Label(tela, text="Digite outro número: ", font="Arial 15 bold")
lbl_num2.place(x=50, y=85)

txt_num2 = Entry(tela, width=20, borderwidth=10, fg="blue", bg="white")
txt_num2.place(x=350, y=85)

lbl_resul = Label(tela, text="Resultado: ", font="Arial 15 bold")
lbl_resul.place(x=50, y=150)

txt_resul = Entry(tela, width=20, borderwidth=10, fg="blue", bg="white")
txt_resul.place(x=350, y=150)

def calcular_soma():
    soma = float(txt_num1.get())+float(txt_num2.get())
    txt_resul.insert(0, soma)
    
    lbl_soma = Label(tela, text="Resultado: "+str(soma))
    lbl_soma.place(x=205,y=235)
    
    
btn_resultado = Button(tela,text="Somar",command=calcular_soma)
btn_resultado.place(x=50,y=200)
tela.mainloop()
