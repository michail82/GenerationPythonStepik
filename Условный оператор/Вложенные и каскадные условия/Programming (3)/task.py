# put your python code here
m = int (input())
if m % 2 == 1 and not m == 9 and not m == 11 or m == 8 or m == 10 or m == 12:
    print ('31')
elif m == 2:
    print ('28')
else:
    print ('30')

# кому лень:
# 1, 3, 5, 7, 8, 10, 12 месяцы - 31 день
# 4, 6, 9, 11 - 30
# 2 - 28