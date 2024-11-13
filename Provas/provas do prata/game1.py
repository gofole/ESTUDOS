import random
numero_secreto =random.randint(1,20)
print('Agora Começa OS JOGOS DO JOGOS MORTAIS 😨🩸🔪')
numero = int(input('Digite sua tentativa Jogador'))
while numero != numero_secreto:
    print('Digite sua proxima tentativa jogador, Nao esqueça que sua vida esta em Jogo!')
    numero = int(input('Digite sua tentativa Jogador'))
    if numero == numero_secreto:
        print(f'Parabens Voce ESCAPOU DA MORTE DESSA VEZ,Numero secreto é  {numero_secreto}🎃')
    elif numero < numero_secreto:
        print('O Numero esta Abaixo do Numero Secreto Cuidado sua vida esta correndo Risco😨')
    elif numero > numero_secreto:
        print('O Numero esta alto demais do Numero secreto Sua vida esta em Risco😨')