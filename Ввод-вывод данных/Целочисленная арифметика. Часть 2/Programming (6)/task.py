# put your python code here
n = int(input())
print('Сумма цифр =', (n // 100) + (n % 100) // 10 + n % 10)
print('Произведение цифр =', (n // 100) * ((n % 100) // 10) * (n % 10))
