# Crie um programa que leia duas notas de um aluno e calcule sua média mostrando uma mensagem no final,
# de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

primeira_prova = float(input("Nota da primeira avaliação:"))
segunda_prova = float(input("Nota da segunda avaliação:"))

media = (primeira_prova + segunda_prova) / 2

print(f"A media do aluno é: {media}")

if media < 4.9:
    print("Aluno REPROVADO!")
elif 5 <= media <= 6.49:
    print("Aluno em RECUPERAÇÃO")
else:
    print("Aluno APROVADO")
