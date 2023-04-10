'''
    Exercício 6:
    Solicite vários números ao usuário (até que ele digite o número zero) e informe o 
    somatório dos números digitados
'''

i = 1
somatorio = 0

while i != 0:
    i = int(input("Informe um número inteiro (digite 0 para sair): "))
    somatorio += i

print(f"O somatório dos números digitados é: {somatorio}")