#49. Faça um programa que mostre uma tabuada de um número que o usuário escolher utilizando um laço for.
n = int(input("Você gostaria de gerar a tabuada de qual número?  "))
print("=-=-=-=-=-=-=-TABUADA-=-=-=-=-=-=-=")
for c in range (0,11):
    print("{} x {} = {}".format(n, c, n*c))
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")