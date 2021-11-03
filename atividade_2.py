
# Atividade 2
# Desenvolva uma calculadora científica com Tkinter que deve possuir, além das operações
# aritméticas básicas (adição, subtração, divisão e multiplicação), a possibilidade de calcular raiz
# quadrada, potenciação de números, funções trigonométricas (seno, cosseno, tangente).

from tkinter import *

# É necessário importar a biblioteca de "math" para a calculadora poder fazer o "evaluate" das
# funções (tan/sin/sqrt/cos)
from math import *

# Espaço dos botões na horizontal
spaceSizeX = 50
# Espaço dos botões na vertical
spaceSizeY = 40


# Insere um dígito no texto
def inserir_digito(digito):
    lbl_resultado['text'] += str(digito)


# Remove o ultimo carácter do texto
def remover_ultimo():
    lbl_resultado['text'] = lbl_resultado['text'][0:len(str(lbl_resultado['text'])) - 1]


# Criar um botão padrão
def novo_btn(texto, comando, tamanho):
    btn = Button(calculadora, width=tamanho, text=f'{texto}', font=('arial', 12), command=comando, relief='groove',
                 activebackground='white')
    return btn


# Mapa com todas os operadores da calculadora
mapa_de_operadores = {
    "+": lambda: inserir_digito(' + '),
    "-": lambda: inserir_digito(' - '),
    "÷": lambda: inserir_digito(' ÷ '),
    "×": lambda: inserir_digito(' × '),
    "^": lambda: inserir_digito(' ^ '),
    "√": lambda: inserir_digito('sqrt('),
    "sin": lambda: inserir_digito('sin('),
    "cos": lambda: inserir_digito('cos('),
    "tan": lambda: inserir_digito('tan('),
    "(": lambda: inserir_digito('('),
    ")": lambda: inserir_digito(')'),
    "←": lambda: remover_ultimo()
}

# Mapa com todas os numeros da calculadora
mapa_de_numeros = {
    "0": lambda: inserir_digito('0'),
    "1": lambda: inserir_digito('1'),
    "2": lambda: inserir_digito('2'),
    "3": lambda: inserir_digito('3'),
    "4": lambda: inserir_digito('4'),
    "5": lambda: inserir_digito('5'),
    "6": lambda: inserir_digito('6'),
    "7": lambda: inserir_digito('7'),
    "8": lambda: inserir_digito('8'),
    "9": lambda: inserir_digito('9'),
    "e": lambda: inserir_digito('e'),
    "π": lambda: inserir_digito('π')

}


# Mede qual é a altura do mapa na interface
def comprimento_do_mapa_y(mapa):
    return (len(mapa) / 3) * spaceSizeY


# Cria todos os itens de dentor de um mapa
def criar_itens_de_mapa(mapa, origemX, origemY):
    count = 0
    spaceX = 0
    spaceY = 0
    for item in mapa:
        btn_item_do_mapa = novo_btn(str(item), mapa[item], 4)
        if count % 3 == 0:
            spaceY += 1
            spaceX = 0
        else:
            spaceX += 1
        btn_item_do_mapa.place(x=spaceX * spaceSizeX + origemX, y=spaceY * spaceSizeY + origemY)
        count += 1


# Botões básicos
def criar_botoes_basicos():
    # butão para mostrar o resultado
    btn_igual = novo_btn("=", comando=comando_resultado, tamanho=15);
    btn_igual.place(x=0, y=comprimento_do_mapa_y(mapa_de_operadores) + spaceSizeY)

    # butão para limpar
    btn_limpar = novo_btn("limpar", comando=comando_limpar, tamanho=15)
    btn_limpar.place(x=150, y=comprimento_do_mapa_y(mapa_de_operadores) + spaceSizeY)


# Traduz os caractéres especiais e calcula o valor com base na string
def traduzir(texto):
    try:
        texto = texto.replace('π', 'pi').replace('÷', '/').replace('×', '*')
        return str(eval(texto))
    except SyntaxError:
        return 'Erro de syntax.'
    except ValueError:
        return 'Valor inválido.'
    except:
        return "Erro desconhecido."


# Exibe o valor do resultado
def comando_resultado():
    lbl_resultado['text'] = traduzir(lbl_resultado['text'])


# Limpa o texto da conta/resultado
def comando_limpar():
    lbl_resultado['text'] = ''


# Cria todos os botões da calculadora
def criar_btns_principais():
    criar_itens_de_mapa(mapa_de_operadores, 0, 0)
    criar_itens_de_mapa(mapa_de_numeros, spaceSizeX * 3, 0)
    criar_botoes_basicos()


calculadora = Tk()
calculadora.title("Calculadora (Atividade 2)")
calculadora.geometry("300x250")
calculadora.resizable(False, False)

# Texto da conta/resultado
lbl_resultado = Label(calculadora, text='', width=41, justify=CENTER)
lbl_resultado.place(x=0, y=10)

criar_btns_principais()

calculadora.mainloop()
