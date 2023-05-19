def list_comprenssion(x,y,z,n,arr):
    arr=[]
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                if sum([i+j+k!=n]):
                    arr.append([i,j,k])
    print(arr)
a=int(input("enter any number"))
b=int(input("enter any number"))
c=int(input("enter any number"))
d=int(input("enter any number"))
list1=map(int,input("enter the elements").split(','))
list_comprenssion(a,b,c,d,list1)
