'''
    Exercício 8:
    Escreva um algoritmo que solicite 10 números e informe qual foi o menor número 
    digitado.
'''

i = 1;
menor = None;

while i <= 10:
    num = float(input("Informe um número inteiro: "))
    if menor is None or num < menor:
        menor = num
    i += 1;

print(f"O menor número foi {menor}")
