negative_number = 0
count_positive_numbers = 0
max_negative_number = -10**6 - 1
for i in range(1, 11):
    x = int(input())
    if x >= 0: 
        count_positive_numbers += 1
    if x < 0: 
        negative_number += x  
#***********************************
    if x < 0 and x > max_negative_number: 
             max_negative_number = x
#***********************************  
if count_positive_numbers == i: 
    print ('NO')
else:
    print (negative_number)
    print (max_negative_number)