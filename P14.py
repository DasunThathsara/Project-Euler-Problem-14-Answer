t=0
for n in range(1,1000000):
    l=[n]
    while True:
        if n%2==0:
            x=n/2
        else:
            x=3*n+1
        l.append(x)
        n=x
        if n==1:
            break
    if t<len(l):
        t=len(l)
        w=l
print(w[0])
