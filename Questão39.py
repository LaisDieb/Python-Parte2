#39. Escreva um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar;
#Se é a hora de se alistar;
#Se já passou do tempo de alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que oassou do prazo.
from datetime import date
atual = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}".format(nasc,idade,atual))
if idade == 18:
    print("Você tem que se alistar imediatamente.")
elif idade < 18:
    saldo = 18 - idade
    print("Ainda faltam {} anos para o alistamento.".format(saldo))
elif idade > 18:
    saldo = idade - 18
    print("Você já deveria ter se alistado há {} anos.".format(saldo))