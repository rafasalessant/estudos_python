# Mostre a tabuada de um número que o usuário escolher, só que agora utilizando um laço **for**.

numero = int(input("Digite um número:"))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
