
# Atividade 3:
# Utilizando a biblioteca gráfica Tkinter, o aluno deve construir uma interface que simule uma tela
# de login de usuário contendo o campo de login, senha e um botão de autenticação. Uma
# mensagem deve ser exibida caso o login e senha estejam corretos (“Usuário autenticado!”). No
# entanto, ao digitar login e senha incorretos, o programa deverá mostrar a mensagem (“login
# e/ou senha incorretos”)

# Senha: 123
# Usuário: admin

import tkinter.messagebox
from tkinter import *


def login_command():
    if nome.get() == "admin" and senha.get() == "123":
        tkinter.messagebox.showinfo(message="Usuário autenticado!")
        return
    tkinter.messagebox.showerror(message="login e/ou senha incorretos")


login = Tk()
login.geometry('250x100')
Label(login, text="Nome de usuário:").grid(row=0)
Label(login, text="Senha:").grid(row=1)

nome = Entry(login)
senha = Entry(login, show='*')

btn1 = Button(login, text="Login", command=login_command)

nome.grid(row=0, column=1)
senha.grid(row=1, column=1)
btn1.grid(row=2, column=1)

login.mainloop()
