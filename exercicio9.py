'''
    Exercício 9:
    Faça um algoritmo que solicite N números e calcule a média dos números pares e a 
    média dos números ímpares (o valor de N deve ser solicitado ao usuário no início do 
    programa).
'''

i = 1;
i2 = int(input("Informe a quantidade de números que deseja inserir: "))

# Variáveis para somar os pares e contar cada um deles para a média 
somaPares = 0
contaPares = 0

# Variáveis para somar os ímpares e contar cada um deles para a média 
somaImpares = 0
contaImpares = 0

# Estrutura de repetição (enquanto o contador for menor ou igual a quantidade que o usuário deseja colocar de números)
while i <= i2:
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0: # Vai somar todos os números pares para fazer a média 
        contaPares += 1
        somaPares += num
    elif num % 2 != 0:
        contaImpares += 1
        somaImpares += num
    i += 1

if contaPares > 0:
    mediaPares = somaPares / contaPares
    print(f"A média de números pares é de {mediaPares}")
else:
    print("Não há números pares.")

if contaImpares > 0:
    mediaImpares = somaImpares / contaImpares
    print(f"A média de números ímpares é de {mediaImpares}")
else: 
    print("Não há números ímpares.")