# put your python code here
n = int(input())
total = 0
for i in range(1,n+1):
    for j in range(i):
        total += 1
        print(total,'', end='')
    print()



