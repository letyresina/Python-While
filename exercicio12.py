'''
    Exercício 12:
    Faça um algoritmo que solicite um número inteiro ao usuário e calcule o fatorial desse número.
     O fatorial de um número N é a multiplicação de N por seus antecessores maiores ou iguais a 1.
'''

num = int(input("Informe um número inteiro maior que 0: "))
i = 1
resultado = 1

while i <= num:
    resultado *= i
    i += 1

print(f"O fatorial de {num}! é {resultado}")