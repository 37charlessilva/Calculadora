from tkinter import *
from Botons import * 

# Iniciair janela com
janela = Tk()
janela.configure(bg="#3507f1")

largura_tela = janela.winfo_screenwidth()

x = largura_tela + 500

# Colocar título
janela.title("Calculadora")

# Largura e altura da janela e onde começa a janela tipo
# (a primeira parte e largura e altura) 500x200+200+200
janela.geometry(f"+{x}+250")

# Definir se pode aumentar ou não a largura e altura
janela.resizable(True, True)

conteudo = StringVar()
conteudo.set("0")

historico = StringVar()
historico.set("0")

entrada_atras = Label(janela, textvariable=historico, bg="#3507f1", font=("Arial", 12), anchor="e")
entrada_atras.grid(row=0, ipadx=30, columnspan=4, sticky="we", padx=10)


entrada = Label(janela, textvariable=conteudo, bg="#3507f1", font=("Arial", 28, "bold"),  anchor="e")
entrada.grid(row=1, ipadx=30, columnspan=4, sticky="we", padx=10)
buttons(janela, conteudo, historico)

# Dá peso 1 para todas as linhas para que elas estiquem verticalmente

info = janela.grid_size()

for c in range(info[1]):
    janela.rowconfigure(c, weight=1)

for c in range(info[0]):
    janela.columnconfigure(c, weight=1)

# Evento de janela

def tecla(event): 

    tecla = event.char

    if tecla in "123456789+=-*/": 
        clique(tecla, conteudo, historico)

    elif event.keysym == "BackSpace":
        conteudo.set(conteudo.get()[:-1])
    
    elif event.keysym == "Return":
        clique("=", conteudo, historico)


janela.bind("<Key>", tecla)

janela.mainloop()
