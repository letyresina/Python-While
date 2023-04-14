'''
    Exercício 11:
    Escreva um programa que solicita ao usuário o valor de N e calcule o valor de S
    na série presente no PDF em documentacao.
'''

N = int(input("Informe um valor inteiro qualquer: "))
i = 1
somatorio = 0

while i <= N:
    somatorio += 1 / i 
    i += 1

print(f"O S de {N} é {somatorio}")
