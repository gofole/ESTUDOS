import random
opcoes =["pedra","papel","tesoura"]
escolha = random.choice(opcoes)
while True:
        jogador = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar o game): ")
        
        if jogador == "sair":
            print("O game foi encerrado.")
            break
        
        
        if jogador not in opcoes:
            print("Escolha inválida. Tente novamente.")
            continue
                
        computador = random.choice(opcoes)
        print(f"O computador escolheu: {computador}")               #AI E FODA EM PRATA!!!NUNCA MAIS! 14HORAS PRA FAZER ISSO

        if jogador == computador:
            print("Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or (jogador == "papel" and computador == "pedra") or (jogador == "tesoura" and computador == "papel"):
            print("Você ganhou!")
        else:
            print("Você perdeu!")

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        