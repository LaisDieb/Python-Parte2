#37. Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário;
#2 para octal;
#3 para hexadecimal.
num = int(input("Informe um número inteiro: "))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

opção = int(input("Sua opção: "))

if opção == 1:
    print("O número {} em binário é: {}".format(num,bin(num)[2:]))
elif opção == 2:
    print("O número {} em octal é: {}".format(num,oct(num)[2:]))
elif opção == 3:
    print("O número {} em hexadecimal é: {}".format(num,hex(num)[2:]))
else:
    print("Erro. Digite um número válido.\n1 para binário.\n2 para octal.\n3 para hexadecimal.")