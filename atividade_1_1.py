
# Atividade 1 - Parte 1
# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros
# formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e
# custo, que é o custo de um item antes do imposto. A função "altera" o valor de custo para incluir
# o imposto sobre vendas


# Aplicar imposto
# taxa_imposto: É a quantia de imposto sobre vendas
# custo: é o custo de um item antes do imposto
def alterar(taxa_imposto, custo):
    return custo + ((taxa_imposto / 100.0) * custo)


# Apenas receber um input válido.
# mensagem: mensagem antes de receber o input
# resultado: tipo "float"
def input_numerico_valido(mensagem):
    print(mensagem)
    try:

        valor_input = float(input())
        if valor_input <= -1:
            raise ValueError()

    except ValueError:
        print("Valor inválido, você só pode inserir um valor numérico positivo.")
        return input_numerico_valido(mensagem)

    return valor_input


# Função principal
def main():

    custo = input_numerico_valido("Digite o valor do produto (valor numérico): ")
    taxa_imposto = input_numerico_valido("Digite o valor do imposto (valor numérico): ")
    valor_final = alterar(taxa_imposto, custo)

    print(f"\nValor inicial: R$ {custo}")
    print(f"Valor final: R$ {valor_final} | Imposto: {taxa_imposto}%")


main()
