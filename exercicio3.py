'''
    Exercício 3:
    Escreva um algoritmo que solicite a idade de 15 pessoas e informe a quantidade de pessoas com 
    idade inferior a 18 anos.
'''

i = 1

while i <= 15:
    idade = int(input("Digite a idade da pessoa desejada: "))
    if (idade < 18):
        print(idade)
    i += 1
