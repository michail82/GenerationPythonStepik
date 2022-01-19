# put your python code here
s = input()
n = len(s)
count = 0
for i in range(n):
   if s[i] != s[i].upper():
    count +=1
print (count)