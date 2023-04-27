import requests
from tkinter import *
import tkinter as tk

janela = Tk()
janela.attributes('-fullscreen', True)
janela.configure(background='#FFCC00') #Cor de fundo
janela.title ('Pizzaria RAD') #Título da Janela
#janela.geometry('1280x720') #Tamanho Janela
janela.resizable(False, False) #Se a Janela pode ser redimensionada pode usar minsize / maxsize

def nova_janela():
    global janela2
    janela2 = Tk()
    janela2.attributes('-fullscreen', True)
    janela2.title('Área de Cadastro')
    #janela2.geometry('1280x720')
    janela2.resizable(False, False)
    janela2.configure(background='#FFCC00')



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

    pizza1 = PhotoImage(file='IMG\pizza.png')
    img_pizza1 = Label(janela2, image=pizza1, background='#FFCC00')
    img_pizza1.place(x=700, y=30)

#Botão sair do programa
def sair():
    janela.destroy()

def retornar():
    janela2.destroy()
    #janela.deiconify()
    #janela2.withdraw()


#Textos Janela Principal
texto_vazio = Label (janela, background='#FFCC00')
texto_vazio.grid(column=0, row=4)

texto_boasvindas = Label (janela, text='SEJA BEM VINDO A PIZZARIA RAD!')
texto_boasvindas.configure(font=('Arial Black', 15), background='#9B111E', foreground='#F0F4F5')
#texto_boasvindas.place(x=150, y=150, width=400)
texto_boasvindas.grid(column=0, row=6, padx=40, pady=40)
texto_boasvindas2 = Label (janela, text='Realize agora mesmo o seu cadastro e GANHE DESCONTO!')
texto_boasvindas2.configure(font=('Arial Black', 15), background='#989A91')
#texto_boasvindas2.place(x=30, y=250, width=650)
texto_boasvindas2.grid(column=0, row=8, padx=40, pady=40)



#COLOCAR COMAND JANELA2
#Botão cadastro
botao_cadastro = Button(janela, text='ÁREA DE CADASTRO', font=('Arial Black', 15), foreground='#FFCC00')
botao_cadastro.grid(column=0, row=10, padx=30, pady=30)
botao_cadastro.configure(background='black', relief=GROOVE, command=nova_janela)
#botao_cadastro.place(x=220, y=350)

botao_localizar = Button(janela, text='LOCALIZAR CLIENTE', font=('Arial Black', 15), foreground='#FFCC00')
botao_localizar.grid(column=0, row=12, padx=30, pady=30)
botao_localizar.configure(background='black', relief=GROOVE)
#botao_localizar.place(x=220, y=450)

botao_exit = Button(janela, text='SAIR', font=('Arial Black', 15), foreground='#FFCC00', command=sair)
botao_exit.grid(column=0, row=14, padx=30, pady=30)
botao_exit.configure(background='black', relief=GROOVE)
#botao_localizar.place(x=220, y=450)

#Imagem Principal
pizza = PhotoImage(file='IMG\pizza.png')
img_pizza = Label(janela, image=pizza, background='#FFCC00')
img_pizza.place(x=700, y=30)


janela.mainloop()

