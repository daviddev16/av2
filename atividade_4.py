# Atividade 4:
# Tomando como base o paradigma orientado a objetos, faça o que se pede:
# Classe Bichinho Virtual: Crie uma classe que modele um Tamagoshi (Bichinho Eletrônico):
# a. Atributos: Nome, Fome, Saúde e Idade
# b. Métodos: Alterar_Nome, Fome, Saúde e Idade; Retornar_Nome, Fome, Saúde e Idade e
# Imprimir (deve apresentar os valores de todos os atributos)
# Após a criação da classe, instancie dois Tamagoshis e altere seus atributos e depois os imprima.

class Tamagoshi:

    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, nova_fome):
        self.fome = nova_fome

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def alterar_saude(self, nova_saude):
        self.saude = nova_saude

    def mostar_dados(self):
        return f"\nNome: {self.nome}, Saúde: {self.saude}, Fome: {self.fome}, Idade: {self.idade}"


tm1 = Tamagoshi(nome="Tama1", fome=20, saude=42, idade=12)
tm1.alterar_nome("tamagoshi-1")
tm1.alterar_fome(32)
tm1.alterar_saude(99)
tm1.alterar_idade(13)

tm2 = Tamagoshi(nome="Tama2", fome=34, saude=64, idade=55)
tm2.alterar_nome("tamagoshi-2")
tm2.alterar_fome(10)
tm2.alterar_saude(87)
tm2.alterar_idade(56)

print(tm1.mostar_dados())
print(tm2.mostar_dados())
