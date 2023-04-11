'''
    Exercício 9:
    Faça um algoritmo que solicite N números e calcule a média dos números pares e a 
    média dos números ímpares (o valor de N deve ser solicitado ao usuário no início do 
    programa).
'''

i = 1;
i2 = int(input("Informe a quantidade de números que deseja inserir: "))

# Variáveis para pegar pares e ímpares
pares = 0
impares = 0

# Terminar amanhã
while i <= i2:
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0: # Vai somar todos os números pares para fazer a média 
        pares += 1
        pares / num
    elif num % 2 != 0:
        impares += 1
        impares / num
    i += 1

print(f"A média de números pares é de {pares}")
print(f"A média de números ímpares é de {impares}")