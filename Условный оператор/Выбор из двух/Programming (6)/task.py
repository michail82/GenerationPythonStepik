a = int (input())
b = int(input())
c = int(input())
d = int(input())
ab = 0
cd = 0
#****AB******
if a < b:
    ab = a
if a > b:
    ab = b
if a == b:
    ab = a
#****CD*******
if c < d:
    cd = c
if c > d:
    cd = d
if c == d:
    cd = c
#****ABCD*******
if ab < cd:
    print (ab)
if ab > cd:
    print (cd)
if ab == cd:
    print (cd)