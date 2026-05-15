from tkinter import *
from Botons import * 

# Iniciair janela com
janela = Tk()
largura_tela = janela.winfo_screenwidth()

x = largura_tela + 500

# Colocar título
janela.title("Calculadora")

# Largura e altura da janela e onde começa a janela tipo
# (a primeira parte e largura e altura) 500x200+200+200
janela.geometry(f"+{x}+250")

# Definir se pode aumentar ou não a largura e altura
janela.resizable(False, False)

conteudo = StringVar()
conteudo.set("0")

historico = StringVar()
historico.set("0")

entrada_atras = Label(janela, textvariable=historico, relief="solid")
entrada_atras.grid(row=0, ipadx=30, columnspan=4, sticky=E)


entrada = Label(janela, textvariable=conteudo, relief="solid")
entrada.grid(row=1, ipadx=30, columnspan=4, sticky=E)
buttons(janela, conteudo)

# Evento de janela

def tecla(event): 

    tecla = event.char

    if tecla in "123456789+=-*/": 
        clique(tecla, conteudo, historico)

    elif event.keysym == "BackSpace":
        conteudo.set(conteudo.get()[:-1])
    
    elif event.keysym == "Return":
        clique("=", conteudo, historico)

    print(event.keysym)


janela.bind("<Key>", tecla)

janela.mainloop()
