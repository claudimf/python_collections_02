from collections import defaultdict, Counter

# Testando o uso de diversas coleções
texto1 = """ 
    Existem várias questões que podem levar o profissional a considerar uma transição de carreira, e uma delas é ter insatisfações com o seu rumo profissional ou cargo atual e está tudo bem se isso acontecer, mudar faz parte da nossa existência.

A baixa produtividade pode ser uma das características das pessoas insatisfeitas que permanecem em seu cargo indesejado. Seja qual for a sua motivação ou propósito, deve haver cuidado para as consequências não refletirem diretamente na vida pessoal do profissional.

A transição de carreira é uma ótima opção para as pessoas que desejam desfrutar de novos desafios, que estão em busca de maior satisfação ou até mesmo estabilidade financeira. Muitos jovens fazem curso superior antes mesmo de ter alguma experiência no mercado de trabalho, isso pode também ocasionar uma transição, pois com a experiência profissional essas pessoas passam a ter contato com novas áreas.
"""

texto2 = """ 
    Para te apoiar ainda mais nessa jornada, durante a Imersão, nossos instrutores e instrutoras estarão disponíveis para responder dúvidas em nosso canal do Discord.

O canal também é uma porta aberta para conhecer outras pessoas que estão no seu mesmo nível de conhecimento e compartilhar experiências!
"""

aparicoes = Counter(texto1.lower())
print(aparicoes)
total_de_caracteres = sum(aparicoes.values())
print(total_de_caracteres)

for letra, frequencia in aparicoes.items():
    tupla = (letra, frequencia / total_de_caracteres)
    print(tupla)

proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
print(proporcoes)

proporcoes = dict(proporcoes)
print(proporcoes)
proporcoes = Counter(proporcoes)
print(proporcoes.most_common(10))


def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())
    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        # print(caractere, " => ", proporcao)

        print("{} => {:.2f}%".format(caractere, proporcao*100))


print('\n texto1: \n')
analisa_frequencia_de_letras(texto1)

print('\n texto2: \n')
analisa_frequencia_de_letras(texto2)
