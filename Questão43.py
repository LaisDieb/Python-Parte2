#43. Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
#Abaixo de 18.5:Abaixo do peso;
#Entre 18.5 e 25: Peso ideal;
#25 até 30: Sobrepeso;
#30 até 40: Obesidade;
#Acima de 40: Obesidade mórbida.
peso = float(input("Informe seu peso em kg: "))
altura = float(input("Informe sua altura em m: "))
imc = peso/(altura**2)
print("IMC: {:.2f}".format(imc))
if imc < 18.5:
    print("Abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("Peso normal.")
elif imc >= 25 and imc < 30:
    print("Sobrepeso.")
elif imc >= 30 and imc < 40:
    print("Obesidade.")
else:
    print("Obesidade mórbida.")