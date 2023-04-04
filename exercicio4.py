'''
    Exercício 4:
    Escreva um algoritmo que solicite 10 números e informe quantos números entre 100 e 200 foram 
    digitados.
'''

i = 1
numeros = 0

while i <= 10:
    num = int(input("Informe um número inteiro: "))
    if (num >= 100 and num <= 200):
        numeros += 1
    i += 1

print(f"A quantidade de números digitados entre 100 e 200 foram {numeros}")

