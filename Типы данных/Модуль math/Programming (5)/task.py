# put your python code here
from math import *
a,b,c = float(input()),float(input()),float(input())
d = (b**2)-(4*a*c) #Дискриминант
if d > 0:
    x1 = (-b + sqrt((b**2)-(4*a*c)))/(2*a)
    x2 = (-b - sqrt((b**2)-(4*a*c)))/(2*a)
    if x1 > x2:
        print (x2)
        print (x1)
    elif x2 > x1:
        print (x1)
        print (x2)
elif d == 0:
    x1 = x2 = (-(b/(2*a)))
    print (x1)
if d < 0:
    print ('Нет корней')

