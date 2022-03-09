import forca
import adivinhacao

def escolhe_jogo():
    print("*******************")
    print("Escolha seu o jogo!")
    print("*******************")

    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual jogo?"))

    if jogo == 1:
        print("Jogando forca")
        forca.jogar_forca()
    else:
        print("Jogando advinhação")
        adivinhacao.jogar_advinhacao()


if __name__ == "__main__":
    escolhe_jogo()
