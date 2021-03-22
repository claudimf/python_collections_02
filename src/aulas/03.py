usuarios = {1, 5, 76, 34, 52, 13, 17}
print(len(usuarios))

usuarios.add(13)
print(len(usuarios))

usuarios.add(765)
print(len(usuarios))

# Congelando o conjunto
usuarios = {1, 5, 76, 34, 52, 13, 17}
usuarios = frozenset(usuarios)

# usuarios.add(765)

# Trabalhando com textos
meu_texto = 'Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro'

meu_texto = set(meu_texto.split())

print(meu_texto)
