# 0 a 2000 - isento
# 2000,01 a 3000 - 8%
# 3000,01 a 4500 - 18%
# 4500,01 - 28%

salario = float(input("Qual seu salário?"))

valor_maximo_taxa_1 = (1000 * 8) / 100
valor_maximo_taxa_2 = (1500 * 18) / 100

if salario <= 2000:
    print(f"Isento")
elif 2000.01 <= salario <= 3000:
    print(f"Seu imposto é: R$ {((salario - 2000) * 8) / 100:.2f}")
elif 3000.01 <= salario <= 4500:
    print(f"Seu imposto é: R$ {valor_maximo_taxa_1 + ((salario - 3000) * 18) / 100:.2f}")
else:
    print(f"Seu imposto é: R$ {valor_maximo_taxa_1 + valor_maximo_taxa_2 + ((salario - 4500) * 28) / 100:.2f}")
