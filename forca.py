import random


def abrir_arquivo():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    return palavras


def escolha_palavra_secreta(palavras):
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    letra_acertada = ["_" for letra in palavra_secreta]

    return palavra_secreta, letra_acertada


def marca_chute_correto(chute, palavra_secreta, letra_acertada):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letra_acertada[index] = letra
        index += 1


def logica_de_acertar(acertou, enforcou, erros, palavra_secreta, letra_acertada):
    print(letra_acertada)
    # Loop, enquanto não enforcar ele continua e se não acertar continua também
    while not acertou and not enforcou:
        chute = input("Qual letra?").strip().upper()

        if chute in palavra_secreta:
            marca_chute_correto(chute, palavra_secreta, letra_acertada)
        else:
            print("Letra não encontrada!")  # Se não acertar a letra, ele vai imprimir essa mensagem
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letra_acertada
        print(letra_acertada)

    if acertou:
        print("Você ganhou!")
    else:
        print("Você enforcou!")


def jogar():
    print("***************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************")

    palavras = abrir_arquivo()
    palavras_secretas, letras_acertadas = escolha_palavra_secreta(palavras)

    acertou = False
    enforcou = False
    erros = 0

    logica_de_acertar(acertou, enforcou, erros, palavras_secretas, letras_acertadas)

    print("Fim do Jogo")


if __name__ == "__main__":
    jogar()
