m = int(input())
n = int(input())
if m < n:
    for n in range (m,n+1,1):
        print (n)
elif n < m:
    for n in range (m,n-1,-1):
        print (n)
elif m == n:
        print (m)
