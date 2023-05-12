def fizzbuzz(num):
    for num in range(1,num+1):
        if num%3==0 and num%5==0:
            print(f'fizz buzz')
        elif num%3==0:
            print(f'fizz')
        elif num%5==0:
            print(f'buzz')
        else:
            print(num)
        
fizzbuzz(50)



