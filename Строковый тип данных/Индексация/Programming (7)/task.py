# put your python code here
s = input ()
plus = 0
star = 0
for i in s:
     if i in '*':
      star += 1
     if i in '+':
      plus += 1
print ('Символ + встречается',plus,'раз')
print  ('Символ * встречается',star,'раз')