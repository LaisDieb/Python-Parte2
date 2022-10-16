#38. Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é maior;
#O segundo valor é maior;
#Não existe valor maior.Os dois são iguais.
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

if a>b:
    print("O primeiro valor, {}, é maior que o segundo, {}.".format(a,b))
elif a<b:
    print("O segundo valor, {}, é maior que o primeiro, {}.".format(b,a))
else:
    print("Os valores são iguais.")
