M=int(input("enter rows"))
N=int(input("enter colons"))
list1=[]
for i in range(1,M*N+1):
    list1.append(i)
    if i%N==0:
        print(*list1,sep=' ')
        list1=[]
