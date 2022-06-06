"""genera la siguiente serie: 1,2,3,4,5,6,7,8,9....n"""

#input
n = int(input("digite el valor de n: "))
#processing
s = "serie: "
for i in range(1,n+1):
    if i < n:
         s = s + str(i) + ", "
    else:
        s = s + str(i)     
    
    


#output
print(s)