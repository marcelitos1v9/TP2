from tkinter import *

tela = Tk()
tela.title("Cálculo de Velocidade")
tela.configure(background="#FF5500")  # Fundo vermelho

largura = 700
altura = 400

# Definir que a tela comece de forma centralizada
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx = (largura_screen // 2) - (largura // 2)
posy = (altura_screen // 2) - (altura // 2)

tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

lbl_titulo = Label(text="VELOCIDADE CARRO", font="bold 20", bg="#FF5500", fg="white")
lbl_titulo.pack(pady=20)

def calcular_velocidade():
    nome = txt_nome.get()
    distancia = float(txt_distancia.get())
    tempo = float(txt_tempo.get())
    
    # Cálculo da velocidade
    velocidade = (distancia * 1000) / (tempo * 60)  # Converter para m/s

    # Exibir resultados
    lbl_resultado.config(text=f"O carro: {nome}\nPercorreu: {distancia} metros\nem um tempo de: {tempo} segundos\nem uma velocidade de: {velocidade:.2f} m/s")
    txt_velocidade.delete(0, END)
    txt_velocidade.insert(0, f"{velocidade:.2f}")

lbl_nome = Label(text="Nome Carro:", font="bold 14", bg="#FF5500", fg="white")
lbl_nome.place(x=40, y=80)

txt_nome = Entry(tela, width=30, borderwidth=5, fg="blue", bg="white")
txt_nome.place(x=250, y=80)

lbl_distancia = Label(text="Distância Percorrida em metros:", font="bold 14", bg="#FF5500", fg="white")
lbl_distancia.place(x=40, y=120)

txt_distancia = Entry(tela, width=10, borderwidth=5, fg="blue", bg="white")
txt_distancia.place(x=300, y=120)

lbl_tempo = Label(text="Tempo em segundos:", font="bold 14", bg="#FF5500", fg="white")
lbl_tempo.place(x=40, y=160)

txt_tempo = Entry(tela, width=10, borderwidth=5, fg="blue", bg="white")
txt_tempo.place(x=250, y=160)

lbl_velocidade = Label(text="Velocidade do Carro:", font="bold 14", bg="#FF5500", fg="white")
lbl_velocidade.place(x=40, y=200)

txt_velocidade = Entry(tela, width=10, borderwidth=5, fg="blue", bg="white")
txt_velocidade.place(x=250, y=200)

btn_calcular = Button(text="CALCULAR VELOCIDADE", font="bold 14", command=calcular_velocidade, bg="blue", fg="white")
btn_calcular.place(x=200, y=240)

lbl_resultado = Label(tela, width=50, font="bold 14", fg="blue", bg="white")
lbl_resultado.place(x=40, y=280)

tela.mainloop()
