from collections import defaultdict, Counter

# Utilizando Dicionários(Mapas, etc)
meu_texto = 'Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro'
meu_texto.lower()

# utilizando o defaultdict
aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    aparicoes[palavra] += 1

print(aparicoes)


class Conta:
    def __init__(self):
        print("Criando uma conta nova")


contas = defaultdict(Conta)
print(contas)
contas[15]
print(contas[15])
print(contas[15])

aparicoes = Counter(meu_texto.split())
print(aparicoes)
