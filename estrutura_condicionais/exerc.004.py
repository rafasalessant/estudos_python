# Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.

x = int(input("Digite um número inteiro:"))
y = int(input("Digite mais um número inteiro diferente do primeiro:"))
z = int(input("Digite outro numero inteiro diferente dos anteriores:"))

if x > y > z:
    print(f"A ordem crescente é: {x}, {y}, {z}")
elif x > z > y:
    print(f"A ordem crescente é: {x}, {z}, {y}")
elif y > x > z:
    print(f"A ordem crescente é: {y}, {x}, {z}")
elif y > z > x:
    print(f"A ordem crescente é: {y}, {z}, {x}")
elif z > x > y:
    print(f"A ordem crescente é: {z}, {x}, {y}")
elif z > y > x:
    print(f"A ordem crescente é: {z}, {y}, {z}")
else:
    print("Você digitou numeros iguais")
