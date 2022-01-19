# put your python code here

s = input()
line_length = len(s)
first_part = s[0:line_length - line_length // 2]
last_part =  s[line_length // 2 + line_length % 2:]
#print (first_part)
#print (last_part)
print (last_part+first_part)


