from tkinter import *

tela = Tk()
tela.title("Calculadora de Total de Compras")
tela.configure(background="#1e3743")

largura = 700
altura = 400

# Definir que a tela comece de forma centralizada
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx = (largura_screen // 2) - (largura // 2)
posy = (altura_screen // 2) - (altura // 2)

tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

lbl_titulo = Label(text="Calculadora de Total de Compras", font="bold 20", bg="#1e3743", fg="white")
lbl_titulo.pack(pady=20)

def calcular_total():
    produto = txt_produto.get()
    quantidade = txt_quantidade.get()
    preco = txt_preco.get()
    
    if quantidade.isdigit() and preco.replace('.', '', 1).isdigit():
        quantidade = int(quantidade)
        preco = float(preco)
        total = quantidade * preco
        
        lbl_resultado.config(text=f"Produto: {produto}\nQuantidade: {quantidade}\nPreço: R$ {preco:.2f}\nTotal: R$ {total:.2f}")
    else:
        lbl_resultado.config(text="Por favor, insira valores válidos.")

lbl_produto = Label(text="Nome do Produto:", font="bold 14", bg="#1e3743", fg="white")
lbl_produto.place(x=40, y=80)

txt_produto = Entry(tela, width=30, borderwidth=5, fg="blue", bg="white")
txt_produto.place(x=250, y=80)

lbl_quantidade = Label(text="Quantidade Comprada:", font="bold 14", bg="#1e3743", fg="white")
lbl_quantidade.place(x=40, y=120)

txt_quantidade = Entry(tela, width=10, borderwidth=5, fg="blue", bg="white")
txt_quantidade.place(x=250, y=120)

lbl_preco = Label(text="Preço do Produto:", font="bold 14", bg="#1e3743", fg="white")
lbl_preco.place(x=40, y=160)

txt_preco = Entry(tela, width=10, borderwidth=5, fg="blue", bg="white")
txt_preco.place(x=250, y=160)

btn_calcular = Button(text="Calcular Total", font="bold 14", command=calcular_total, bg="blue", fg="white")
btn_calcular.place(x=240, y=200)

lbl_resultado = Label(tela, width=50, font="bold 14", fg="blue", bg="white")
lbl_resultado.place(x=40, y=260)

tela.mainloop()
