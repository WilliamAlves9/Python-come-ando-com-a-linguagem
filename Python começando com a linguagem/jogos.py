import forca
import main
def escolhe_jogo():
    print("*********************************")
    print("Escolha o seu Jogo!**************")
    print("*********************************")


    print("(1)jogo da forca (2) jogo da adivinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("jogando adivinhação")
        main.jogar_adivinhacao()

if(__name__ == "__main__"):
    escolhe_jogo()

