"""genera la siguiente serie: 1,4,9,16,25,36...."""

#input
n = int(input("digite el valor de n: "))
#processing
s = "serie: "
for i in range(1,n+1):
    t = i*i
    if i < n:
         s = s + str(t) + ", "
    else:
        s = s + str(t)     
    
#output
print(s)