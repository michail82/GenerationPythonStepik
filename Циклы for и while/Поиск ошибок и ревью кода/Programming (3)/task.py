n = int(input())
last_number = 0
max_3_number = -1
while n > 0:
    last_number = n % 10
    if last_number % 3 == 0 and last_number > max_3_number:
       max_3_number = last_number
    n = n // 10
#print (max_3_number)
if max_3_number == -1:
     print ('NO')
else:
     print (max_3_number)