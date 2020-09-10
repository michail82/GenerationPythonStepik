# put your python code here
n = int(input())
s = 0
t = 0
for i in range (n):
    if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8:
        s += i
    else:
        s + t
print (s)
