# put your python code here
n = int(input())
if n == 0:
    print ('зеленый')
elif n >= 1 and n <=10 and n % 2 == 1:
    print ('красный')
elif n >= 1 and n <=10 and n % 2 == 0:
    print ('черный')

elif n >= 11 and n <=18 and n % 2 == 1:
    print ('черный')
elif n >= 11 and n <=18 and n % 2 == 0:
    print ('красный')

elif n >= 19 and n <=28 and n % 2 == 1:
    print ('красный')
elif n >= 19 and n <=28 and n % 2 == 0:
    print ('черный')

elif n >= 29 and n <=36 and n % 2 == 1:
    print ('черный')
elif n >= 29 and n <=36 and n % 2 == 0:
    print ('красный')

else:
    print ('ошибка ввода')