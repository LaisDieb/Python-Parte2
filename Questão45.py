#45. Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
escolha = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0,2)
print("\033[4;30;43m-=-=-=-=-= JO-KEN-PÔ -=-=-=-=-=\033[m")
print('''É a sua vez. Escolha:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input("Qual é a sua jogada?"))
print("JO...")
sleep(1)
print("KEN...")
sleep(1)
print("PÔ!")
print("-="*15)
print("O computador escolheu \033[4;30;43m{}\033[m".format(escolha[comp]))
print("O jogador escolheu \033[4;30;45m{}\033[m".format(escolha[jogador]))
print("-="*15)
if (comp == 0 and jogador == 0) or (comp == 1 and jogador == 1) or (comp == 2 and jogador == 2):
    print("EMPATE")
elif (comp == 0 and jogador == 1) or (comp == 1 and jogador == 2) or (comp == 2 and jogador == 0):
    print("Parabéns! Você VENCEU o computador.")
elif (comp == 0 and jogador == 2) or (comp == 1 and jogador == 0) or (comp == 2 and jogador == 1):
    print("Não foi dessa vez. Você PERDEU.")
else:
    print("Opção inválida. Tente novamente.")