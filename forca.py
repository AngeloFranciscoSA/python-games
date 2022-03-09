
def jogar_forca():
    print("***************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************")

    palavra_secreta = "banana".upper()
    letra_acertada = ["_", "_", "_", "_", "_", "_"]

    acertou = False
    enforcou = False
    erros = 0

    print(letra_acertada)

    # Loop, enquanto não enforcar ele continua e se não acertar continua também
    while not acertou and not enforcou:
        chute = input("Qual letra?").strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letra_acertada[index] = letra

                index += 1
        else:
            print("Letra não encontrada!")  # Se não acertar a letra, ele vai imprimir essa mensagem
            erros += 1

        enforcoum = erros == 6
        print(letra_acertada)

    print("Fim do Jogo")


if __name__ == "__main__":
    jogar_forca()
