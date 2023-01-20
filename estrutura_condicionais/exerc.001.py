primeiro_numero = int(input("Insira o primeiro número para comparação:"))
segundo_numero = int(input("Insira o segundo número para comparação:"))

if primeiro_numero > segundo_numero:
    print(f"{primeiro_numero} é maior que {segundo_numero}")
elif primeiro_numero < segundo_numero:
    print(f"{primeiro_numero} é menor que {segundo_numero}")
else:
    print(f"{primeiro_numero} é igual a {segundo_numero}")
