# put your python code here
n = int(input())
CountingDigits = 0
two_digit = 0
while n > 9:
    two_digit = n
    n = n // 10
two_digit %= 10
print (two_digit)




