# put your python code here
a = int(input())
b = int(input())
counter = 0
for i in range (a,b+1):
    if i**3%10 == 4 or i**3%10 == 9:
        counter = counter + 1
print (counter)

