from tkinter import *

# Iniciair janela com
janela = Tk()
# Colocar título
janela.title("Calculadora")
# Largura e altura da janela e onde começa a janela tipo
# (a primeira parte e largura e altura) 500x200+200+200
janela.geometry("+500+250")
# Definir se pode aumentar ou não a largura e altura
janela.resizable(False, False)

"""Funções dos botons, Provavelmente vai virar um classe"""


def calculo(n):
    if conteudo.get() == "0":
        conteudo.set(str(n))

    else:
        if len(conteudo.get()) < 28:
            conteudo.set(conteudo.get() + str(n))


"""Onde vai ficar os números e resultados"""

conteudo = StringVar()
conteudo.set("0")

"""Aprender sobre os espaços da label para definir um tamanho de pelomenos alguns números"""
"""Criar um git pra esse projeto"""
""", anchor=E"""
entrada = Label(janela, textvariable=conteudo, relief="solid")
entrada.grid(row=0, ipadx=30, columnspan=3, sticky=E)

botao0 = Button(janela, text="7", command=lambda: calculo("7"))
botao0.grid(column=0, ipadx=30, row=1)

botao1 = Button(janela, text="8", command=lambda: calculo("8"))
botao1.grid(column=1, ipadx=30, row=1)

botao2 = Button(janela, text="9", command=lambda: calculo("9"), width=0)
botao2.grid(column=2, ipadx=30, row=1)

botao3 = Button(janela, text="4", command=lambda: calculo("4"))
botao3.grid(column=0, ipadx=30, row=2)

botao4 = Button(janela, text="5", command=lambda: calculo("5"))
botao4.grid(column=1, ipadx=30, row=2)

botao5 = Button(janela, text="6", command=lambda: calculo("6"))
botao5.grid(column=2, ipadx=30, row=2)

botao6 = Button(janela, text="3", command=lambda: calculo("3"))
botao6.grid(column=0, ipadx=30, row=3)

botao7 = Button(janela, text="2", command=lambda: calculo("2"))
botao7.grid(column=1, ipadx=30, row=3)

botao8 = Button(janela, text="1", command=lambda: calculo("1"))
botao8.grid(column=2, ipadx=30, row=3)

botao9 = Button(janela, text="0", command=lambda: calculo("0"))
botao9.grid(column=0, ipadx=30, row=4)

botao10 = Button(janela, text="+")
botao10.grid(column=1, ipadx=30, row=4)

botao11 = Button(janela, text="-")
botao11.grid(column=2, ipadx=30, row=4)

botao12 = Button(janela, text="*")
botao12.grid(column=0, ipadx=30, row=5)

botao13 = Button(janela, text="/")
botao13.grid(column=1, ipadx=30, row=5)

botao14 = Button(janela, text="=")
botao14.grid(column=2, ipadx=30, row=5)

janela.mainloop()
