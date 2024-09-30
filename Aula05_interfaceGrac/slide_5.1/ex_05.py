from tkinter import *

tela = Tk()
tela.title("Gerenciador de Contatos")
tela.configure(background="#1e3743")

largura = 700
altura = 400

# Definir que a tela comece de forma centralizada
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx = (largura_screen // 2) - (largura // 2)
posy = (altura_screen // 2) - (altura // 2)

tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

lbl_titulo = Label(text="Gerenciador de Contatos", font="bold 20", bg="#1e3743", fg="white")
lbl_titulo.pack(pady=20)

def exibir_contato():
    nome = txt_nome.get()
    telefone = txt_telefone.get()
    endereco = txt_endereco.get()
    cidade = txt_cidade.get()
    
    lbl_resultado.config(text=f"Dados do Contato:\nNome: {nome}\nTelefone: {telefone}\nEndereço: {endereco}\nCidade: {cidade}")

lbl_nome = Label(text="Nome:", font="bold 14", bg="#1e3743", fg="white")
lbl_nome.place(x=40, y=80)

txt_nome = Entry(tela, width=30, borderwidth=5, fg="blue", bg="white")
txt_nome.place(x=250, y=80)

lbl_telefone = Label(text="Telefone:", font="bold 14", bg="#1e3743", fg="white")
lbl_telefone.place(x=40, y=120)

txt_telefone = Entry(tela, width=15, borderwidth=5, fg="blue", bg="white")
txt_telefone.place(x=250, y=120)

lbl_endereco = Label(text="Endereço:", font="bold 14", bg="#1e3743", fg="white")
lbl_endereco.place(x=40, y=160)

txt_endereco = Entry(tela, width=30, borderwidth=5, fg="blue", bg="white")
txt_endereco.place(x=250, y=160)

lbl_cidade = Label(text="Cidade:", font="bold 14", bg="#1e3743", fg="white")
lbl_cidade.place(x=40, y=200)

txt_cidade = Entry(tela, width=30, borderwidth=5, fg="blue", bg="white")
txt_cidade.place(x=250, y=200)

btn_exibir = Button(text="Exibir Contato", font="bold 14", command=exibir_contato, bg="blue", fg="white")
btn_exibir.place(x=240, y=240)

lbl_resultado = Label(tela, width=50, font="bold 14", fg="blue", bg="white")
lbl_resultado.place(x=40, y=280)

tela.mainloop()
