n = int(input())
num1, num2, num3, num4 = 0, 0, 0, 0
while n // 25 != 0:
    num1 += 1
    n -= 25
#print ('Остаток 25 = ',n)
#print('num1 = ',num1)
while n // 10 != 0:
    num2 += 1
    n -= 10
#print('Остаток 10 = ',n)
#print('num2 = ',num2)
while n // 5 != 0:
    num3 += 1
    n -= 5
#print('Остаток 5 =',n)
#print('num3 = ',num3)
while n // 1 != 0:
     num4 += 1
     n -= 1
#print('Остаток 1 =',n)
#print('num4 = ',num4)
s = num1+num2+num3+num4
print (s)