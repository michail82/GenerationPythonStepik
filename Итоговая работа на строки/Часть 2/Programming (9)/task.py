s = input()      #'affectfive'
count_f = 0
flag = 0
for i in s:
    if i == 'f': count_f +=1
    if  count_f == 1:
        flag = -1
    if count_f == 0:
        flag = -2
    else:
        flag =  (s.replace('f', '_', 1).find('f'))
print (flag)



