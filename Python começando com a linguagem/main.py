import random
def jogar_adivinhacao():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    print(numero_secreto)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual nivel de dificultade?")
    print("(1)facil (2)medio (3)dificil")
    nivel = int(input("Digite aqui o nivel de dificuldade:"))

    if(nivel == 1):
        total_de_tentativas = 10
    elif(nivel == 2):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite o  numero entre 1 e 100:"))
        print("você digitou", chute)

        if(chute < 1 or chute > 100):
            print("Digite um numero entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("voce acertou!!!")
            break
        else:
            if(maior):
                print("voce errou! o seu chute foi maior que o numero secreto")
            elif(menor):
                print("voce errou! o seu chute foi menor que o numero secreto")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
    print("fim do jogo e fez {} pontos".format(pontos))

if(__name__=="__main__"):
    jogar_adivinhacao()