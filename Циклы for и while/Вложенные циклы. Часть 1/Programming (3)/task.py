# put your python code here
n = int (input())
for i in range(n//2+1):
    for j in range(i+1):
        print('*', end='')
    print()
for i in range(n//2+1,0,-1):
    for j in range(i-1):
        print('*', end='')
    print()
# for i in range(n,0,-1):
#      for j in range(i):
#          print('*', end='')
#      print()
