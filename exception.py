def exception(s):
        try:
            a, b = map(int, (s.split()))
            print(a//b)
        except ZeroDivisionError as e:
            print ("Error Code:",e)
        except ValueError as e:
            print("Error Code:",e)

array = []
n = int(input("Please input number of test cases: "))
for _ in range(n):
    array.append(input("Please input space separted two values: "))

for str in array:
    exception(str)
