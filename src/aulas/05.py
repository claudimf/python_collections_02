aparicoes = dict(Guilherme = 1, cachorro = 1)
print(aparicoes)

# Adicionar valores
aparicoes['Carlos'] = 1
print(aparicoes)

# editar
aparicoes['Carlos'] = 2
print(aparicoes)

# remover
del aparicoes['Carlos']
print(aparicoes)

# verificar
print('cachorro' in  aparicoes)
print('Carlos' in  aparicoes)

# iterar
for elemento in aparicoes:
    print(elemento)

for elemento in aparicoes.keys():
    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

for elemento in aparicoes.items():
    print(elemento)

for chave, valor in aparicoes.items():
    print(chave, valor)
