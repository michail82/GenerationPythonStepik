# put your python code here
s = input()
count_f = 0
for i in s:
    if i == "f":
        count_f +=1
if count_f == 1:
        print (s.find('f'))
elif count_f > 1:
        print(s.find('f'), end=' ')
        print (s.rindex('f'))
else:
        print ('NO')



