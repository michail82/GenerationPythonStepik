# put your python code here
first_digit = 0
last_digit = 0
last_digit += a % 10
sum_firstLast = 0
while a > 0:
    sum_numbers += a % 10
    CountingDigits += 1
    product_numbers *= a % 10
    arithmetic_mean = sum_numbers/CountingDigits
    if a > 0:
        first_digit = a
    a = a // 10
sum_firstLast = first_digit + last_digit
print (sum_numbers)
print (CountingDigits)
print (product_numbers)
print (arithmetic_mean)
print (first_digit)
print (sum_firstLast)


