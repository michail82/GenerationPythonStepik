n = int(input())
max1 = 0
max2 = 0
for i in range (0,n):
    s = int(input())
    if s > max1:
        max2 = max1
        max1 = s
    if s < max1 and s > max2:
        max2 = s
print (max1)
print (max2)



