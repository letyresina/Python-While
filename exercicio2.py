'''
    Exercício 2:
    Escreva um algoritmo que solicite 10 números e exiba o dobro de cada número digitado.
'''

i = 1

while i <= 10:
    num = int(input("Informe um número: "))
    dobro = num * 2
    print(f"O dobro de {num} é {dobro}")
    i += 1