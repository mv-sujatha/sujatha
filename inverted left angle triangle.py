n=int(input("enter any number"))
for r in range(n,0,-1):
    for c in range(1,r+1):
        print(c,end=' ')
    print()
