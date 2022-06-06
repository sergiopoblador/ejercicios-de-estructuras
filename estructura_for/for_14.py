"""genera la siguiente serie: 2,6,12,20,30,42,56...."""

#input
n = int(input("digite el valor de n: "))
#processing
s = "serie: "
for i in range(1,n+1):
    t = i**2 + i
    if i < n:
         s = s + str(t) + ", "
    else:
        s = s +  str(t)     
    
#output
print(s)