import random
numero_secreto = random.randrange(1,101)
print("bem vindo ao jogo da adivinhação")
print("Qual nível você quer jogar?", numero_secreto)
print("(1) Fácil (2) Médio (3) Difícil")

total_de_tentativas = 3




pontos = 1000

nivel = int(input("Defina o nível: "))


if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um numero entre 1 e 100")
        continue
    

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você fez {} pontos".format(pontos))
        break
    else:
        if(maior):
            print("Seu chute foi maior do que o numero secreto")
        elif(menor):
            print("Seu chute foi menor do que o numero secreto")
    pontos_perdidos = abs(numero_secreto - chute)
    pontos = pontos - pontos_perdidos

print("Fim do jogo")

        
    

    

    


