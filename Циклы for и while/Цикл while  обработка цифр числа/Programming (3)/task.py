# put your python code here
a = int(input())
sum_numbers = 0
CountingDigits = 0
#******the sum of the number begin
while a > 0:
    sum_numbers += a % 10
    a = a // 10
    CountingDigits += 1
print (CountingDigits)
print ('Sum = ',sum_numbers)
#******the sum of the number end
#******Counting digits begin
#******Counting digits end
