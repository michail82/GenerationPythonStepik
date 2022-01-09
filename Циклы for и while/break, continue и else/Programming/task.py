# put your python code here
n = int(input())
result = 0
for i in range (2, n + 1):
    if n % i == 0 and i > 1:
     print (i)
     break

