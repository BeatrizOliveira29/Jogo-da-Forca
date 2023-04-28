from random import choice

with open('dicionario.txt') as arquivo:
    linhas = arquivo.read()
    lista_de_palavras = linhas.split('\n')

palavra = choice(lista_de_palavras).upper()

forca = """

_____
     |
     |
     -
"""
vazio = """

"""
cabeça = """
     0
"""

tronco = """
     0
     |
"""
braço_esquerdo = """
     0
    /|
"""
braço_direito = """
     0
    /|\
"""
perna_esquerda = """
     0
    /|\
    /
"""
perna_direita = """
     0
    /|\
    / \
"""
chances = [vazio, cabeça, tronco, braço_esquerdo, braço_direito, perna_esquerda, perna_direita]

acertos = 0
erros = 0
letras_acertadas = ''
letras_erradas = ''

while acertos != len(palavra) and erros != 6:
    mensagem = ''
    for letra in palavra:
        if letra in letras_acertadas:
            mensagem += f'{letra} '
        else:
            mensagem += '_ '
    print(forca+chances[erros])
    print(mensagem)

    letra = input('Digite uma letra: ').upper()

    if letra in letras_acertadas+letras_erradas:
        print('Você já tentou essa letra! >_<')
        continue

    if letra in palavra:
        print('Você acertou a letra! UwU')
        letras_acertadas += letra
        acertos += 1
    else:
        print('Você errou a letra! T.T')
        letras_erradas += letra
        erros += 1
