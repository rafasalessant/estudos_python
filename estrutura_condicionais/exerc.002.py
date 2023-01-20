# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa
# Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida
# fórmula: IMC = peso / (altura)²

altura = float(input("Qual sua altura?"))
peso = float(input("Qual seu peso?"))

seu_imc = peso / (altura ** 2)
print(f"Seu IMC é {seu_imc:.2f}")

if seu_imc < 18.5:
    print(f"Você está abaixo do peso")
elif seu_imc >= 18.5 and seu_imc <= 24.9:
    print(f"Você está no peso ideal")
elif 25 <= seu_imc <= 29.9:
    print(f"Você está com sobrepeso")
elif 30 <= seu_imc <= 39.9:
    print(f"Você está com obesidade")
else:
    print(f"Você está com obesidade mórbida")
