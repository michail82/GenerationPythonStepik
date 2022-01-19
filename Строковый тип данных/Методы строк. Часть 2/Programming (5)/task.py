# put your python code here
s = input()
var1 = 0
var2 = 0
for i in s:
    if s.count(i) >= var1:
        var1 = s.count(i)
        var2 = i
print (var2)