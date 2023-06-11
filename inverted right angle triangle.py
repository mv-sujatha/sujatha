N=int(input("enter any number"))
s=0
for i in range(1,N+1):
    s=s+i
for r in range(N):
    for c in range(N):
        if r<=c:
            print(str(s),end=' ')
            s=s-1
        else:
            print(' ',end=' ')
    print()
