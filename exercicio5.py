'''
    Exercício 5:
    Escreva um algoritmo que solicite 15 números e informe o somatório de todos os números ímpares 
    digitados.
'''

i = 1
somatorio = 0

while i <= 15:
    num = int(input("Informe um número inteiro: "))
    if num % 3 == 0:
        somatorio += 1
    i += 1

print(f'O somatório de números ímpares é {somatorio}')