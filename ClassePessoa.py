# Definindo a classe
class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")

    def fazer_aniversario(self):
        self.idade += 1
        print(f"Parabéns {self.nome}! Agora você tem {self.idade} anos.")

# Criando Objetos (instâncias)
p1 = Pessoa("Andréa", 53)
p2 = Pessoa("Ronaldo", 52)

# Chamando os métodos
p1.apresentar()
p1.fazer_aniversario
p1.apresentar

print("---")

p2.apresentar()
p2.fazer_aniversario
p2.apresentar