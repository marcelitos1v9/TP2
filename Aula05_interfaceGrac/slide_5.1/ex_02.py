from tkinter import *

tela = Tk()
tela.title("Calculadora de Soma")
tela.configure(background="#1e3743")

largura = 700
altura = 500

# Definir que a tela comece de forma centralizada
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx = (largura_screen // 2) - (largura // 2)
posy = (altura_screen // 2) - (altura // 2)

tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

lbl_titulo = Label(text="Calculadora de Soma", font="bold 20", bg="#1e3743", fg="white")
lbl_titulo.pack(pady=20)

def calcular_soma():
    num1 = txt_num1.get()
    num2 = txt_num2.get()
    
    if num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit():
        resultado = float(num1) + float(num2)
        lbl_resultado.config(text=f"{resultado:.2f}")
    else:
        lbl_resultado.config(text="Por favor, insira números válidos.")

lbl_num1 = Label(text="Digite o primeiro número:", font="bold 14", bg="#1e3743", fg="white")
lbl_num1.place(x=40, y=80)

txt_num1 = Entry(tela, width=15, borderwidth=5, fg="blue", bg="white")
txt_num1.place(x=300, y=80)

lbl_num2 = Label(text="Digite o segundo número:", font="bold 14", bg="#1e3743", fg="white")
lbl_num2.place(x=40, y=140)

txt_num2 = Entry(tela, width=15, borderwidth=5, fg="blue", bg="white")
txt_num2.place(x=300, y=140)

btn_calcular = Button(text="Calcular Soma", font="bold 14", command=calcular_soma, bg="blue", fg="white")
btn_calcular.place(x=240, y=200)

lbl_resultado_titulo = Label(text="Resultado:", font="bold 14", bg="#1e3743", fg="white")
lbl_resultado_titulo.place(x=40, y=260)

lbl_resultado = Label(tela, width=20, font="bold 14", fg="blue", bg="white")
lbl_resultado.place(x=180, y=260)

tela.mainloop()
