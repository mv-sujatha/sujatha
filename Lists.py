N = int(input())
    list1=[]
    for i in range(N):
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
            
            
