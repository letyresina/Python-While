'''
    Exercício 7:
    Solicite dois números diferentes ao usuário (caso os números sejam iguais, o algoritmo 
    deve solicitar os números novamente) e informe a diferença entre o maior e o menor número. 
'''

num1 = int(input("Informe o primeiro número inteiro: "))
num2 = int(input("Informe o segunda número inteiro: "))

while num1 == num2:
    print("Os números são iguais, digite novamente")
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))

if num1 > num2:
    diferenca = num1 - num2
else:
    diferenca = num2 - num1

print(f"A diferença entre {num1} e {num2} é de {diferenca}")