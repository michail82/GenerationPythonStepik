# put your python code here
n = int(input())
count = 0
for _ in range (0,n):
    s = input()
    if s.count('11') >= 3:
        count +=1
print (count)



