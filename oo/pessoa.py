class Pessoa:
    def __init__(self, *filhos, nome=None, idade=43):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)



    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    leofilho = Pessoa(nome='Leo Filho')
    leonardo = Pessoa(leofilho, nome='Gonçalves')
    #print(Pessoa.cumprimentar(p))
    print(leonardo.cumprimentar())
    print(leonardo.nome)
    print(leonardo.idade)
    for filho in leonardo.filhos:
        print(filho.nome)
    leonardo.sobrenome = 'Cordeiro'
    #del leonardo.filhos
    print(leonardo.sobrenome)
    print(leonardo.__dict__)
    print(filho.__dict__)

