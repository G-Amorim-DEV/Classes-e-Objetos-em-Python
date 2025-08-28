# Definindo a Classe
class Aluno:
    def __init__(self, nome, notas=None):
        self.nome = nome
        self.notas = [float(nota) for nota in notas] if notas else []

    def adicionar_nota(self, valor):
        self.notas.append(float(valor))

    def media(self):
        if len(self.notas) == 0:
            return 0
        
        soma = 0
        for nota in self.notas:   
            soma += nota          
        
        media = soma / len(self.notas)  
        return media

    def situacao(self):
        media = self.media() 
        if media < 7:
            print(f"{self.nome}, sua média foi {media:.2f} e você foi REPROVADO! 😡")
        else: 
            print(f"{self.nome}, sua média foi {media:.2f} e você foi APROVADO! 😎")
            

aluno = Aluno("Maria", [])

aluno.adicionar_nota(8.0)
aluno.adicionar_nota(6.5)
aluno.adicionar_nota(7.5)
aluno.situacao()
