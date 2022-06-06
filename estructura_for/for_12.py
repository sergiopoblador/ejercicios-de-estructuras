"""genera la siguiente serie: 1,1/2,1/3,1/4,1/5,1/6...."""

#input
n = int(input("digite el valor de n: "))
#processing
s = "serie: "
for i in range(1,n+1):
    t = i
    if i < n:
         s = s + "1/" +  str(t) + ", "
    else:
        s = s + "1/" +  str(t)     
    
#output
print(s)