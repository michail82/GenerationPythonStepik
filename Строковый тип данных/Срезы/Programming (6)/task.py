# put your python code here

s = input() 
even = ''
not_even = ''
n = len(s)
print(s[2])   
print(s[-2]) 
print(s[:5]) 
print(s[:-2:]) 
for i in range (0,n):
    if i % 2 == 0: 
        even += s[i]
    if i % 2 == 1:
        not_even += s[i]
print (even)
print (not_even)
print (s[::-1])
print (s[::-2])


