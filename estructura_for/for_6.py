import random

n= int(input("ingrse la cantidad de dados: "))

cara1= 0
cara2= 0 
cara3= 0
cara4= 0
cara5= 0
cara6= 0
rta= "lanzamiento = ("

for i in range(n):
    dados= random(1,6)
    if dados ==1:
        cara1 +=1
    elif dados == 2:
        cara2 +=1
    elif dados == 3:
        cara3 += 1
    elif dados == 4:
        cara4 +=1
    elif dados == 5:
        cara5 +=1
    elif dados == 6:
        cara6 += 1

if i < n-1:
    rta= rta + str(dados)+ ", "
else:
    rta= rta + str(dados)

rta= rta+ " )\ncara 1: "

for i in range(cara1):
    rta= rta + "*"
    


