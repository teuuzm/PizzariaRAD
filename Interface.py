import requests
from tkinter import *
import tkinter as tk
import sqlite3
import time
import threading
import mysql.connector
import tabulate
from tkinter.ttk import Combobox


#Cores: Branco (#F0F4F5) Mostarda (#FFCC00) Vermelho (#9B111E) Preto (#0a0a0a)

janela_inicial = Tk()
janela_inicial.attributes ('-fullscreen', True)
janela_inicial.configure (background='#FFCC00')
janela_inicial.title ('Pizzaria RAD')
janela_inicial.resizable (False, False)

texto_vazio = Label (janela_inicial, background='#FFCC00')
texto_vazio.grid (column=0, row=4)

texto_boasvindas = Label (janela_inicial, text='      PIZZARIA RAD      ')
texto_boasvindas.configure (font=('Eras Bold ITC', 35), background='#9B111E', foreground='#F0F4F5')
texto_boasvindas.grid (column=0, row=6, padx=40, pady=40)

texto_vazio2 = Label (janela_inicial, background='#FFCC00')
texto_vazio2.grid (column=0, row=8)

botao_cadastro = Button(janela_inicial, text='      ÁREA DE CADASTRO      ', font=('Arial Black', 15), foreground='#FFCC00')
botao_cadastro.grid(column=0, row=10, padx=30, pady=30)

botao_localizar = Button(janela_inicial, text='      LOCALIZAR CLIENTE      ', font=('Arial Black', 15), foreground='#FFCC00')
botao_localizar.grid(column=0, row=12, padx=30, pady=30)

botao_sair = Button(janela_inicial, text='      SAIR      ', font=('Arial Black', 15), foreground='#FFCC00')
botao_sair.grid(column=0, row=14, padx=30, pady=30)

pizza = PhotoImage(file='Projeto-Pizzaria\IMG\pizza.png')
img_pizza = Label(janela_inicial, image=pizza, background='#FFCC00')
img_pizza.place(x=700, y=30)

def cadastro():
    global janela_cadastro
    janela_cadastro = Tk()
    janela_cadastro.attributes ('-fullscreen', True)
    janela_cadastro.configure (background='#FFCC00')
    janela_cadastro.title ('Área de Cadastro')
    janela_cadastro.resizable (False, False)

    botao_return = Button(janela_cadastro, text='  RETORNAR  ', command=sair, font=('Arial Black', 10), foreground='#FFCC00')
    botao_return.place(x=600, y=100, width=110, height=35)
    botao_return.configure(background='black', relief=GROOVE)

    botao_cadastrar = Button(janela_cadastro, text='  CADASTRAR  ', font=('Arial Black', 10), foreground='#FFCC00', command=cadastro_dados)
    botao_cadastrar.place(x=450, y=100, width=110, height=35)
    botao_cadastrar.configure(background='black', relief=GROOVE)

    nome = Label (janela_cadastro, text='INSIRA O NOME:', font=('Arial Black', 10))
    nome.configure(foreground='#0a0a0a', background='#FFCC00')
    nome.place (x=100, y=80)

    global caixa_nome
    caixa_nome = Entry (janela_cadastro, font=('Arial Black', 13), relief=GROOVE)
    caixa_nome.place (x=100, y=100, width=300, height=40)

    cpf = Label (janela_cadastro, text='INSIRA O CPF:', font=('Arial Black', 10))
    cpf.configure(foreground='#0a0a0a', background='#FFCC00')
    cpf.place (x=100, y=200)

    global caixa_cpf
    caixa_cpf = Entry (janela_cadastro, font=('Arial Black', 13), relief=GROOVE)
    caixa_cpf.place (x=100, y=220, width=300, height=40)
    caixa_cpf.bind('<KeyRelease>', validar_cpf2)


    email = Label (janela_cadastro, text='INSIRA O EMAIL:', font=('Arial Black', 10))
    email.configure(foreground='#0a0a0a', background='#FFCC00')
    email.place (x=100, y=320)

    global caixa_email
    caixa_email = Entry (janela_cadastro, font=('Arial Black', 13), relief=GROOVE)
    caixa_email.place (x=100, y=340, width=300, height=40)

    telefone = Label (janela_cadastro, text='INSIRA O TELEFONE:', font=('Arial Black', 10))
    telefone.configure(foreground='#0a0a0a', background='#FFCC00')
    telefone.place (x=100, y=440)

    global caixa_telefone
    caixa_telefone = Entry (janela_cadastro, font=('Arial Black', 13), relief=GROOVE)
    caixa_telefone.place (x=100, y=460, width=300, height=40)
    caixa_telefone.bind('<KeyRelease>', validar_tel)


    #checkvar1 = IntVar()
    #checkvar2 = IntVar()
    #c1 = Checkbutton(janela_cadastro, text='WHATSAPP', variable=checkvar1, onvalue=1, offvalue=0, background='#F0F4F5')
    #c1.place(x=100, y=500)
    #c2 = Checkbutton(janela_cadastro, text='APENAS CHAMADAS', variable=checkvar2, onvalue=1, offvalue=0, background='#F0F4F5')
    #c2.place(x=200, y=500)

    endereco = Label (janela_cadastro, text='INSIRA O ENDEREÇO:', font=('Arial Black', 10))
    endereco.configure(foreground='#0a0a0a', background='#FFCC00')
    endereco.place (x=100, y=560)

    global caixa_endereco
    caixa_endereco = Entry (janela_cadastro, font=('Arial Black', 13), relief=GROOVE)
    caixa_endereco.place (x=100, y=580, width=300, height=40)

    sabor = Label (janela_cadastro, text='INSIRA A DATA DE NASCIMENTO:', font=('Arial Black', 10))
    sabor.configure(foreground='#0a0a0a', background='#FFCC00')
    sabor.place (x=100, y=680)

    global caixa_nascimento
    caixa_nascimento = Entry (janela_cadastro, font=('Arial Black', 13), relief=GROOVE)
    caixa_nascimento.place (x=100, y=700, width=300, height=40)
    caixa_nascimento.bind('<KeyRelease>', validar_data)


    #caixa_sabor = tk.Listbox(janela_cadastro, width=40, height=6, font=('Arial', 10), relief=GROOVE)
    #caixa_sabor.insert(1, ' CALABRESA')
    #caixa_sabor.insert(2, ' FRANGO C/ CATUPIRY')
    #caixa_sabor.insert(3, ' 4 QUEIJOS')
    #caixa_sabor.insert(4, ' PORTUGUESA')
    #caixa_sabor.insert(5, ' ROMEU E JULIETA')
    #caixa_sabor.insert(6, ' BRIGADEIRO')
    #caixa_sabor.place(x=100, y=740)

    janela_cadastro.mainloop()

def localizar():
    global janela_localizar
    janela_localizar = Tk()
    janela_localizar.attributes ('-fullscreen', True)
    janela_localizar.configure (background='#FFCC00')
    janela_localizar.title ('Localizar Cliente')
    janela_localizar.resizable (False, False)

    botao_return = Button(janela_localizar, text='  RETORNAR  ', command=retornar, font=('Arial Black', 10), foreground='#FFCC00')
    botao_return.place(x=600, y=100, width=110, height=35)
    botao_return.configure(background='black', relief=GROOVE)

    botao_localizar = Button(janela_localizar, text='  LOCALIZAR  ', font=('Arial Black', 10), foreground='#FFCC00', command=ver_dados)
    botao_localizar.place(x=450, y=100, width=110, height=35)
    botao_localizar.configure(background='black', relief=GROOVE)

    nome = Label (janela_localizar, text='DIGITE O CPF:', font=('Arial Black', 10))
    nome.configure(foreground='#0a0a0a', background='#FFCC00')
    nome.place (x=100, y=80)

    global cpf_select
    cpf_select = Entry (janela_localizar, font=('Arial Black', 13), relief=GROOVE)
    cpf_select.place (x=100, y=100, height=40, width=300)
    cpf_select.bind('<KeyRelease>', validar_cpf)

    global result_dados
    result_dados = Label (janela_localizar, text="", font=('Arial Black', 13), foreground='white')
    result_dados.configure(background='black', relief=GROOVE)
    result_dados.place (x=100, y=300, width=1000, height=100)

    janela_localizar.mainloop()


def formatar_cpf(cpf):
    cpf_formatado = cpf.replace(".", "").replace("-", "")  # Remove pontos e hífens

    if len(cpf_formatado) > 3:
        cpf_formatado = cpf_formatado[:3] + "." + cpf_formatado[3:]  # Insere o primeiro ponto

    if len(cpf_formatado) > 7:
        cpf_formatado = cpf_formatado[:7] + "." + cpf_formatado[7:]  # Insere o segundo ponto

    if len(cpf_formatado) > 11:
        cpf_formatado = cpf_formatado[:11] + "-" + cpf_formatado[11:]  # Insere o hífen

    return cpf_formatado

def validar_cpf(event):
    cpf_digitado = cpf_select.get()
    cpf_formatado = formatar_cpf(cpf_digitado)
    cpf_select.delete(0, 'end')
    cpf_select.insert(0, cpf_formatado)

def validar_cpf2(event):
    cpf_digitado = caixa_cpf.get()
    cpf_formatado = formatar_cpf(cpf_digitado)
    caixa_cpf.delete(0, 'end')
    caixa_cpf.insert(0, cpf_formatado)
    
def formatar_data(data):
    data_formatada = data.replace("/", "").replace("-", "")

    if len(data_formatada) > 2:
        data_formatada = data_formatada[:2] + "/" + data_formatada[2:]

    if len(data_formatada) > 5:
        data_formatada = data_formatada[:5] + "/" + data_formatada[5:]

    return data_formatada

def validar_data(event):
    data_digitada = caixa_nascimento.get()
    data_formatada = formatar_data(data_digitada)
    caixa_nascimento.delete(0, 'end')
    caixa_nascimento.insert(0, data_formatada)

def formatar_tel(tel):
    tel_formatado = tel.replace("(", "").replace(")", "").replace("-", "")

    if len(tel_formatado) > 0:
        tel_formatado = tel_formatado[:0] + "(" + tel_formatado[0:]

    if len(tel_formatado) > 3:
        tel_formatado = tel_formatado[:3] + ")" + tel_formatado[3:]

    if len(tel_formatado) > 3:
        tel_formatado = tel_formatado[:9] + "-" + tel_formatado[9:]

    return tel_formatado

def validar_tel(event):
    tel_digitado = caixa_telefone.get()
    tel_formatado = formatar_tel(tel_digitado)
    caixa_telefone.delete(0, 'end')
    caixa_telefone.insert(0, tel_formatado)

def sair():
    try:
        janela_cadastro.destroy()
    except:
        janela_inicial.destroy()

def retornar():
    janela_localizar.destroy()



def ver_dados():    
    try:
        cpf = cpf_select.get()
        conexao = mysql.connector.connect(host='localhost', database='pizzaria', user='mateusradpython', password='radpython')
        print ("Conectado ao banco de dados!")
        comando_localizar = ("SELECT nome, nascimento, contato, email, endereco FROM cliente WHERE cpf = %s")
        valores = (cpf,)
        
        cursor = conexao.cursor()
        cursor.execute(comando_localizar, valores)
        print ("OK!")
        
        resultado = cursor.fetchall()
        print (resultado)

        texto_resultado = ""
        for resultados in resultado:
            texto_resultado += str(resultados) + "\n"
        result_dados.config(text=texto_resultado)

        conexao.commit()

        conexao.close()

    except:
        print ("ID não encontrado!")


def cadastro_dados():    
    try:
        nome = caixa_nome.get()
        cpf = caixa_cpf.get()
        email = caixa_email.get()
        nascimento = caixa_nascimento.get()
        contato = caixa_telefone.get()
        endereco = caixa_endereco.get()

        conexao = mysql.connector.connect(host='localhost', database='pizzaria', user='mateusradpython', password='radpython')
        print ("Conectado ao banco de dados!")

        comando_inserir = ("INSERT INTO cliente (cpf, nome, nascimento, contato, email, endereco) VALUES (%s, %s, %s, %s, %s, %s)")
        valores = (cpf, nome, nascimento, contato, email, endereco)
        
        cursor = conexao.cursor()
        cursor.execute(comando_inserir, valores)

        conexao.commit()

        conexao.close()

    except:
        print ("Não cadastrado!")

botao_cadastro.configure(background='black', relief=GROOVE, command=cadastro)
botao_localizar.configure(background='black', relief=GROOVE, command=localizar)
botao_sair.configure(background='black', relief=GROOVE, command=sair)

janela_inicial.mainloop()

#dropdown na janela localizar
#organizar em retorno em tabela localizar