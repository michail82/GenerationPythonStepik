# put your python code here
a = int(input())
b = int(input())
c = str(input())
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print (a*b)
elif c == '/' and b == 0:
    print ('На ноль делить нельзя!')
elif c == '/':
    print (a/b)
else:
    print ('Неверная операция')