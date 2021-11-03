# Atividade 1 - Parte 2
# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por
# exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
# Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre
# a informação A.M./P.M. como um valor "A" para A.M. e "P" para P.M. Assim, a função para
# efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop
# que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que
# desejar.


# Apenas receber um input válido.
# mensagem: mensagem antes de receber o input
# resultado: tipo "int"
def input_numerico_valido(mensagem):
    print(mensagem)
    try:

        valor_input = int(input())
        if valor_input <= -1:
            raise ValueError()

    except ValueError:
        print("Valor inválido, você só pode inserir um valor numérico positivo.")
        return input_numerico_valido(mensagem)

    return valor_input


# Perguntar o usuário se ele deseja repetir o processo
def converter_de_novo(mensagem):
    print(mensagem)
    try:

        valor_input = str(input()).lower();
        if valor_input == "sim":
            return True
        elif valor_input == "não":
            return False
        else:
            raise ValueError()

    except ValueError:
        print("Valor inválido, Tente: (sim ou não).")
        return converter_de_novo(mensagem)


# Recebe uma lista sobre o horário informado
# [index 0]: horas
# [index 1]: minutos
def input_notacao_24h():
    try:
        horas = input_numerico_valido("Digite o valor das horas (valor numérico): ")
        minutos = input_numerico_valido("Digite o valor dos minutos (valor numérico): ")

        if horas > 24:
            raise ValueError("Número de horas maior que 24.")
        elif minutos > 60:
            raise ValueError("Número de minutos maior que 60.")
        elif horas >= 24:
            horas = 0

        print(" ")
        return [horas, minutos]

    except ValueError as erro:
        print(str(erro))
        return input_notacao_24h()


# Retorna a string "AM" ou "PM" referente as horas.
def string_am_ou_pm(horas):
    if 12 <= horas < 24:
        return "PM"
    else:
        return "AM"


# Retorna as horas no formato AM/PM.
def horas_ampm(horas_em_24h):
    if 12 < horas_em_24h < 24:
        return horas_em_24h - 12
    else:
        return horas_em_24h


# Converte as horas/minutos do sistema 24h para horas/minutos do sistema AM-PM.
def converter_24h_para_ampm(valores_em_24h):
    # Formato string "AM" ou "PM"
    formato_ampm = string_am_ou_pm(valores_em_24h[0])
    # Horas em AM/PM
    horas = horas_ampm(valores_em_24h[0])
    # Os minutos continuam os mesmos.
    minutos = valores_em_24h[1]
    # Retorna o formato HH:MM (AM/PM)
    return f"{horas}:{minutos} {formato_ampm}"


# Função principal
def main():

    while True:
        valores_em_24h = input_notacao_24h()
        valor_em_ampm = converter_24h_para_ampm(valores_em_24h);
        print(f"{valores_em_24h[0]}:{valores_em_24h[1]} -> {valor_em_ampm}")

        if not converter_de_novo("Deseja converter de novo?"):
            break


main()
