#36. Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input("Informe o valor da casa: R$ "))
sal = float(input("Informe seu salário: R$ "))
anos = int(input("Informe em quantos anos pretende quitar o imóvel: "))
prestacao = casa / (anos * 12)
condicao = sal * 30 /100
if prestacao<=condicao:
    print("Empréstimo aprovado!\n Valor das parcelas mensais:R$ {}. ".format(prestacao))
else:
    print("Empréstimo negado.")
