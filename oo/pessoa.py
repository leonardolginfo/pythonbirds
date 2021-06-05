class Pessoa:
    def __init__(self, nome=None, idade=43):
        self.idade = idade
        self.nome = nome


    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    p = Pessoa('Gonçalves')
    #print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Leo'
    print(p.nome)
    print(p.idade)
