'''
    Exercício 11:
    Escreva um programa que solicita ao usuário o valor de N e calcule o valor de S
    na série presente no PDF em documentacao.
'''

N = int(input("Informe um valor inteiro qualquer: "))
i = 1
resultado = 1

while i <= N:
    resultado *= 1 / i 
    i += 1

print(f"O S de {N} é {resultado}")
