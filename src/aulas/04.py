# Utilizando Dicionários(Mapas, etc)
meu_texto = 'Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro'

meu_texto = set(meu_texto.split())

aparicoes = {
    'tenho': 1,
    'vindo': 1,
    'Guilherme': 1,
    'nome': 2,
    'gosto': 1,
    'cachorro': 2,
    'nomes': 1,
    'é': 1,
    'meu': 1,
    'eu': 1,
    'e': 1,
    'o': 1,
    'de': 1,
    'muito': 1,
    'Bem': 1
}

print(aparicoes)
print(aparicoes['Guilherme'])

print(aparicoes.get('xpto', 0))


aparicoes = dict(Guilherme = 1, cachorro = 1)
print(aparicoes)
