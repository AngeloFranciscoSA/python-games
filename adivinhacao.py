import ramdom

def jogar_advinhacao():
    print("********************************")
    print("Bem vindo ao jogo de Advinhação!")
    print("********************************")

    numero_secreto = ramdom.randrange(1, 101)
    numero_tentativas = 0
    pontos = 1000

    print("Escolha a Dificuldade:")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível:"))

    if nivel == 1:
        numero_tentativas = 20
    elif nivel == 2:
        numero_tentativas = 10
    else:
        numero_tentativas = 5

    for rodada in range(0, numero_tentativas):
        chute = int(input("Digite o seu numero: "))

        if numero_secreto == chute:
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if numero_secreto < chute:
                print("Você chutou o numero muito para cima")
            elif numero_secreto > chute:
                print("Você chutou o numero muito para baixo")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do Jogo")


if __name__ == "__main__":
    jogar_advinhacao()
