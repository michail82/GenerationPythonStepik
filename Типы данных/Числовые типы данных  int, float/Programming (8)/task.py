# put your python code here
# put your python code here
a,b,c = int(input()),int(input()),int(input())
max = max (a,b,c)
min = min (a,b,c)
midl = int()
# Равенство
if a == b == c:
    print (a,b,c,sep='\n')
# a == b
elif a == b < c:
    print(c, a, b,sep='\n')
elif a == b > c:
    print(a, b, c,sep='\n')
# b == c
elif a > b == c:
    print(a, b, c,sep='\n')
elif a < b == c:
    print(b, c, a,sep='\n')
# a == c
elif b > a == c:
    print(b, a, c,sep='\n')
elif b < a == c:
    print(a, c, b,sep='\n')
#***********************
elif max > a > min:
    midl = a
    print(max)
    print(midl)
    print(min)
elif max > b > min:
    midl = b
    print(max)
    print(midl)
    print(min)
elif max > c > min:
    midl = c
    print (max)
    print (midl)
    print (min)




