def lists(num):
    list1=[]
    for i in range(num):
        cmd,*n=input().split()
        arr=list(map(int,n))
        if cmd=='insert':
            list1.insert(arr[0],arr[1])
        elif cmd=='print':
            print(list1)
        elif cmd=='remove':
            list1.remove(arr[0])
        elif cmd=='append':
            list1.append(arr[0])
        elif cmd=='sort':
            list1.sort()
        elif cmd=='pop':
            list1.pop()
        elif cmd=='reverse':
            list1.reverse()
num=int(input("enter any number"))
lists(num)
            
