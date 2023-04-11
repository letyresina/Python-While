'''
    Exercício 10:
    Chico tem 1,50m e cresce 2 centímetros por ano, enquanto Juca tem 1,10m e cresce 5 centímetros
    por ano. Considerando que Chico e Juca continuem crescendo constantemente, escreva um 
    algoritmo que calcule quantos anos seriam necessários para Juca ser mais alto que Chico
'''

# Alturas iniciais 
alturaChico = 1.50
alturaJuca = 1.10 

# Contador (para mostrar o ano) 
i = 1 

while alturaJuca <= alturaChico:
    alturaChico += 0.02
    alturaJuca += 0.05
    i += 1

print(f"A quantidade de anos para que Juca seja mais alto que Chico é de {i}")


