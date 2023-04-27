import requests
from tkinter import *
import tkinter as tk

#COLOCAR A DEF NOVA_JANELA
#Janela de cadastro
janela2 = Tk()
janela2.attributes('-fullscreen', True)
janela2.title('Área de Cadastro')
#janela2.geometry('1280x720')
janela2.resizable(False, False)
janela2.configure(background='#FFCC00')

def retornar():
    janela2.destroy()
    #janela.deiconify()
    janela2.withdraw()

botao_return = Button(janela2, text='RETORNAR', command=retornar, font=('Arial Black', 10), foreground='#FFCC00')
botao_return.place(x=400, y=100, width=110, height=35)
botao_return.configure(background='black', relief=GROOVE)

botao_cadastrar = Button(janela2, text='CADASTRAR', font=('Arial Black', 10), foreground='#FFCC00')
botao_cadastrar.place(x=400, y=150, width=110, height=35)
botao_cadastrar.configure(background='black', relief=GROOVE)

caixa_nome = tk.Text(janela2, wrap='word', width=40, height=2, font=('Arial', 10))
caixa_nome.place(x=100, y=100)

caixa_cpf = tk.Text(janela2, wrap='word', width=40, height=2, font=('Arial', 10))
caixa_cpf.place(x=100, y=150)

caixa_email = tk.Text(janela2, wrap='word', width=40, height=2, font=('Arial', 10))
caixa_email.place(x=100, y=200)

caixa_telefone = tk.Text(janela2, wrap='word', width=40, height=2, font=('Arial', 10))
caixa_telefone.place(x=100, y=250)

caixa_endereco = tk.Listbox(janela2, width=40, font=('Arial', 10), relief=GROOVE)
caixa_endereco.insert(1, 'CALABRESA')
caixa_endereco.insert(2, 'FRANGO C/ CATUPIRY')
caixa_endereco.insert(3, '4 QUEIJOS')
caixa_endereco.insert(4, 'PORTUGUESA')
caixa_endereco.insert(5, 'ROMEU E JULIETA')
caixa_endereco.insert(6, 'BRIGADEIRO')
caixa_endereco.place(x=100, y=300)

pizza = PhotoImage(file='IMG\pizza.png')
img_pizza = Label(janela2, image=pizza, background='#FFCC00')
img_pizza.place(x=700, y=30)

janela2.mainloop()
