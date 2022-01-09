even_number_sum = 0
for i in range(0, 7):
    n = int (input())
    if n % 2 == 0:
        even_number_sum +=n
if even_number_sum > 0:
    print (even_number_sum)
else: print (0)
