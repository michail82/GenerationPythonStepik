# put your python code here
n = int(input())
last_digit = 0
pre_last_digit = 0
count_more_less = 1
CountingDigits = 0
flag = True
while n >0:
    CountingDigits += 1
    last_digit = n % 10
    n = n//10
    pre_last_digit = n % 10
    if last_digit < pre_last_digit or last_digit == pre_last_digit:
        count_more_less += 1
if count_more_less == CountingDigits:
    print ('YES')
else: print ('NO')
   # print (last_digit)
   # print (pre_last_digit)
   #print(count_more_less)
   #print (CountingDigits)