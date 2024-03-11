import random

def jogar_advinhacao(min_rand, max_rand, limite_tentativas):
    print("#### BEM VINDO AO JOGO DA ADVINHAÇÃO ####")
    print(f"Tente acertar o número de {min_rand} à {max_rand} em {limite_tentativas} tentativas")
    
    sorteio = random.randint(min_rand, max_rand)
    tentativas = 1

    while tentativas <= limite_tentativas:
        chute = int(input("Digite o valor do seu chute: "))
        
        if chute == sorteio:
            print("Parabéns! Você acertou!!!")
        elif chute > sorteio:
            print("O número que você digitou é maior")
        else:
            print("O número que você digitou é menor")
        
        tentativas += 1

    print("#### FIM DO JOGO ####")

print("Escolha o nível de dificuldade:")
print("1. Fácil (números de 0 a 10, 8 tentativas)")
print("2. Médio (números de 0 a 20, 6 tentativas)")
print("3. Difícil (números de 0 a 50, 4 tentativas)")

opcao = int(input("Digite o número da opção desejada: "))

if opcao == 1:
    min_rand, max_rand, limite_tentativas = 0, 10, 8
elif opcao == 2:
    min_rand, max_rand, limite_tentativas = 0, 20, 6
elif opcao == 3:
    min_rand, max_rand, limite_tentativas = 0, 50, 4
else:
    print("opção invalida")
    exit()

jogar_advinhacao(min_rand, max_rand, limite_tentativas)
           