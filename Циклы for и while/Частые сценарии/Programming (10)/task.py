# put your python code here
# Две переменные одня начальное значение другая предыдущее
n = int(input())
if n == 1:
    print (n)
    quit()
num1 = 1
num2 = 1
print (num1,end=' ')
print (num2,end=' ')
for i in range(2,n):
        num1, num2 = num2, num1 + num2
        print (num2, end=" ")



