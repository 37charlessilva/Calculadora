from tkinter import *

buttonList = [
    ["(", ")", "%", "C"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

def clique(v, conteudo, historico):
    # Escreve os números na label
    atual = conteudo.get()

    if v == "C":
        conteudo.set("0")

    elif v == "=":
        resultado = eval(atual)
        historico.set(f"{atual} = {resultado}")
        conteudo.set(resultado)

    else:
        if atual == "0":
            atual = ""
        if len(atual) < 28:
            conteudo.set(atual + v)



def buttons(janela, conteudo):
    for row, line in enumerate(buttonList, start=2):
        for column, valor in enumerate(line): 
            Button(janela, text=valor, command=lambda v = valor: clique(v, conteudo, conteudo)).grid(
                column=column, ipadx=30, row=row, padx=1, pady=1)
