from random import choice

with open('dicionario.txt') as arquivo:
    linhas = arquivo.read()
    lista_de_palavras = linhas.split('\n')

palavra = choice(lista_de_palavras).upper()

def forca(num_erros):
    if num_erros == 1:
        print(" ----")
        print("|  |")
        print("|  o")
        print("|  ")
        print("|  ")
        print("|_  ")
    elif num_erros == 2:
        print(" ----")
        print("|  |")
        print("|  o")
        print("|  |")
        print("|  ")
        print("|_  ")
    elif num_erros == 3:
        print(" ----")
        print("|  |")
        print("|  o")
        print("|  |\ ")
        print("|  ")
        print("|_  ")
    elif num_erros == 4:
        print(" ----")
        print("|  |")
        print("|  o")
        print("| /|\ ")
        print("|  ")
        print("|_  ")
    elif num_erros == 5:
        print(" ----")
        print("|  |")
        print("|  o")
        print("| /|\ ")
        print("|   \ ")
        print("|_  ")
    elif num_erros == 6:
        print(" ----")
        print("|  |")
        print("|  o")
        print("| /|\ ")
        print("| / \ ")
        print("|_  ")

opcao = ''

while opcao != 's':
    lista_de_palpites = []
    num_erros = 0
    num_acertos = 0

    tamanho_da_palavra_secreta = len(palavra)

    print("*** Jogo da Forca ***")
    print(f"A palavra tem {tamanho_da_palavra_secreta} letras.")

    while num_erros < 6 and num_acertos != tamanho_da_palavra_secreta:
        for letra in palavra:
            if letra in lista_de_palpites:
                print(letra, end=' ')    
            else:
                print("_", end=' ')
        print()    

        letra = input("Digite uma letra: ").upper()

        if letra in lista_de_palpites:
            print(f"A letra {letra} já foi utilizada! O_O")
        else:
            lista_de_palpites.append(letra)
            if letra in palavra:
                print("Acertou! UwU")
                num_acertos += palavra.count(letra)
            else:
                print("Errou! -_-")
                num_erros += 1
                forca(num_erros)
            
    if num_erros == 6:
        print("Você perdeu! T.T")
    elif num_acertos == tamanho_da_palavra_secreta:
        print("Você ganhou! >.<")
    
    opcao = input("Digite `s` para sair ou qualquer coisa para jogar novamente => ").lower()
