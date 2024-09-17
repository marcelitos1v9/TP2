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

tela.title("CADASTRO DE CLIENTES")
lbl_titulo = Label(text="CADASTRO DE CLIENTES",font="bold 25", bg="#1e3743", fg="white")
lbl_titulo.pack()

def cadastrarCliente():
    nome = txt_nome.get()
    email = txt_email.get()
    telefone = txt_telefone.get()
    endereco = txt_end.get()
    
    lbl_mostrar.config(text=f"Nome: {nome}\nEmail: {email}\nTelefone: {telefone}\nEndereço: {endereco}\n")
    
lbl_nome = Label(text="Digite o nome: ",font="bold 18", bg="#1e3743", fg="white")
lbl_nome.place(x=40,y=60)

txt_nome = Entry(tela, width=30, borderwidth=10, fg="blue", bg="white")
txt_nome.place(x=250,y=60)


lbl_email = Label(text="Digite o Email: ",font="bold 18", bg="#1e3743", fg="white")
lbl_email.place(x=40,y=110)

txt_email = Entry(tela, width=30, borderwidth=10, fg="blue", bg="white")
txt_email.place(x=250,y=110)

lbl_telefone = Label(text="Digite o telefone: ",font="bold 18", bg="#1e3743", fg="white")
lbl_telefone.place(x=40,y=160)

txt_telefone = Entry(tela, width=30, borderwidth=10, fg="blue", bg="white")
txt_telefone.place(x=250,y=160)

lbl_end = Label(text="Digite o Endereço: ",font="bold 18", bg="#1e3743", fg="white")
lbl_end.place(x=40,y=210)

txt_end = Entry(tela, width=30, borderwidth=10, fg="blue", bg="white")
txt_end.place(x=250,y=210)

btn_cadastro = Button(text="Cadastrar Cliente", font="bold 18",command=cadastrarCliente)
btn_cadastro.place(x=525,y=60)

lbl_mostrar = Label(tela, width=30, borderwidth=10, fg="blue", bg="white")
lbl_mostrar.place(x=525, y=125)



tela.mainloop()
