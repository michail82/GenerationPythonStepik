s = input()
n = len(s)
count = 0
for i in range (0,n-1):
        if s[i] == s[i + 1]:
            count += 1
print (count)