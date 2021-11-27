# put your python code here
a = int(input())
minn = 9
maxx = 0
while a > 0:
    if a % 10  < minn:
        minn = a % 10
    if a % 10 > maxx:
        maxx = a % 10
    a = a // 10
print ('Максимальная цифра равна',maxx)
print('Минимальная цифра равна', minn)
