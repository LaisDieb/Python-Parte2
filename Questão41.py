#41. A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
#e mostre sua categoria, de acordo com a idade:
#Até 9 anos: Mirim;
#Até 14 anos: Infantil;
#Até 19 anos: Júnior;
#Até 20 anos: Sênior;
#Acima: Master.
anoatual = int(input("Informe o ano atual: "))
anonasc = int(input("Informe o ano de nascimento: "))
idade = anoatual - anonasc

if idade <= 9:
    print("Mirim.")
elif idade > 9 and idade <= 14:
    print("Infantil.")
elif idade > 14 and idade <= 19:
    print("Júnior.")
elif idade > 19 and idade <= 20:
    print("Sênior.")
else:
    print("Master.")