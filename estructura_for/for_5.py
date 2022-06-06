"""Hacer el diagrama de flujo y el programa de python que genere 1000 numero aleatorios y que averigue e imprima cuantos son pares y cuantos son impares"""
import random
# input



pares = 0
impares = 0
# processing
for i in range(n): 
    num_aleatroria = random.randint(1,200)
    if num_aleatroria%2 == 0:
        pares += 1
    else:
        impares += 1
    if i < n-1:
         rta = rta + str(num_aleatroria) + ","
    else:
           rta = rta + str(num_aleatroria) + ","
rta = rta + ")"

# output
print("--resultados--")
print(rta)
print(f"cantidades de pares = ¨{pares}")
print(f"cantidad de impares = {impares}")
