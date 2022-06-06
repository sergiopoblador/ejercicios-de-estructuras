"""genera la siguiente serie: ,2,4,6,8,10,12...."""

#input
n = int(input("digite el valor de n: "))
#processing
s = "serie: "
for i in range(1,n+1):
    t = 2*i
    if i < n:
         s = s + str(t) + ", "
    else:
        s = s + str(t)     
    
#output
print(s)