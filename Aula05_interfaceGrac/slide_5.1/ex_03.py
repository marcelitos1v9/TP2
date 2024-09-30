from tkinter import *

tela = Tk()
tela.title("Calculadora de Média")
tela.configure(background="#1e3743")

largura = 600
altura = 400

# Definir que a tela comece de forma centralizada
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx = (largura_screen // 2) - (largura // 2)
posy = (altura_screen // 2) - (altura // 2)

tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

lbl_titulo = Label(text="Calculadora de Média", font="bold 20", bg="#1e3743", fg="white")
lbl_titulo.pack(pady=10)

def calcular_media():
    nota1 = txt_nota1.get()
    nota2 = txt_nota2.get()
    nota3 = txt_nota3.get()
    
    if nota1.replace('.', '', 1).isdigit() and nota2.replace('.', '', 1).isdigit() and nota3.replace('.', '', 1).isdigit():
        nota1 = float(nota1)
        nota2 = float(nota2)
        nota3 = float(nota3)
        media = (nota1 + nota2 + nota3) / 3
        
        if media >= 7:
            situacao = "Aprovado"
        elif 3 <= media < 7:
            situacao = "Exame"
        else:
            situacao = "Reprovado"
        
        lbl_resultado.config(text=f"Média: {media:.2f} - {situacao}")
        txt_media.delete(0, END)
        txt_media.insert(0, f"{media:.2f}")
    else:
        lbl_resultado.config(text="Por favor, insira notas válidas.")

lbl_nota1 = Label(text="Digite a primeira nota:", font="bold 14", bg="#1e3743", fg="white")
lbl_nota1.place(x=40, y=50)

txt_nota1 = Entry(tela, width=10, borderwidth=5, fg="blue", bg="white")
txt_nota1.place(x=250, y=50)

lbl_nota2 = Label(text="Digite a segunda nota:", font="bold 14", bg="#1e3743", fg="white")
lbl_nota2.place(x=40, y=100)

txt_nota2 = Entry(tela, width=10, borderwidth=5, fg="blue", bg="white")
txt_nota2.place(x=250, y=100)

lbl_nota3 = Label(text="Digite a terceira nota:", font="bold 14", bg="#1e3743", fg="white")
lbl_nota3.place(x=40, y=150)

txt_nota3 = Entry(tela, width=10, borderwidth=5, fg="blue", bg="white")
txt_nota3.place(x=250, y=150)

btn_calcular = Button(text="Calcular Média", font="bold 14", command=calcular_media, bg="blue", fg="white")
btn_calcular.place(x=200, y=200)

lbl_resultado = Label(tela, width=40, font="bold 14", fg="blue", bg="white")
lbl_resultado.place(x=40, y=240)

lbl_media = Label(text="Resultado:", font="bold 14", bg="#1e3743", fg="white")
lbl_media.place(x=40, y=280)

txt_media = Entry(tela, width=10, borderwidth=5, fg="blue", bg="white")
txt_media.place(x=150, y=280)

tela.mainloop()
