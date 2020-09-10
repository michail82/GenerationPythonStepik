# put your python code here
# put your python code here
n = int(input())
average = 0
a = n % 10
b = n % 100 // 10
c = n // 100
average = ((a+b+c) -(max(a, b, c)+min(a, b, c)))
max = (max(a,b,c))
min = (min(a,b,c))
if max - min == average:
    print ('Число интересное')
else:
    print ('Число неинтересное')



