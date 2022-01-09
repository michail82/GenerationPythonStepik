n = int(input())
last_number = 0
while n != 0:
    last_number = n % 10
    n = n//10
print(last_number)