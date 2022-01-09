# put your python code here
import math
n = int (input())
total = 0
for a in range (1,n+1):
    total += math.factorial(a)
print (total)