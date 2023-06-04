def perfect_square(A,B):
    list1=[]
    for num in range(A,B+1):
        if (num**(0.5))==int(num**(0.5)):
            square=num
            list1.append(square)
            count=len(list1)
    print(count)
n1=int(input("enter any number"))
n2=int(input("enter any number"))
perfect_square(n1,n2)
