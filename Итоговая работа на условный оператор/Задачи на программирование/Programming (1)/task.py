# put your python code here
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
fig1 = str
fig2 = str
# Белые клетки для Фигура 1
if a1 % 2 == 1 and a2 % 2 == 1 or a1 == a2 \
    or a1 % 2 == 0 and a2 % 2 == 0:
        fig1 = ('White') #
      #  print ('White')
# Черные клетки для Фигура 1
elif  a1 % 2 == 1 and a2 % 2 == 0 or a2 % 2 == 0 \
        and a1 % 2 == 1 or a1 % 2 == 0 and a2 % 2 == 1:
        fig1 = ('Black')
       # print ('Black')

# Белые клетки для Фигуры 2
if b1 % 2 == 1 and b2 % 2 == 1 or b1 == b2 \
        or b1 % 2 == 0 and b2 % 2 == 0:
        fig2 = ('White')
      #  print('White')
# Черные клетки для Фигуры 2
elif b1 % 2 == 0 and b2 % 2 == 1 or b2 % 2 == 0 \
        and b1 % 2 == 1 or b1 % 2 == 0 and b2 % 2 == 1:
        fig2 = ('Black')
       # print ('Black')
if fig1 == fig2:
    print ('YES')
else:
    print ('NO')




