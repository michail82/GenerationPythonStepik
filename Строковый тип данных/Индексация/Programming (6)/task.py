# put your python code here
s = input ()
n = len(s)
a = 0
for i in range (0,n):
     if s[i] in '0123456789':
         a = 1
if a==1: print ('Цифра')
else: print  ('Цифр нет')