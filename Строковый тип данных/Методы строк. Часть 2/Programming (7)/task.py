# put your python code here
s = input()
#print (s.find('h'))
#print (s.rfind('h'))
#print (s.rindex('h'))
#print(s.replace('h',''))
#print(s[s.find('h')])
#print(s[s.rfind('h')])
cut = (s[s.find('h'):s.rfind('h')+1])
#print(cut)
print(s.replace(cut,''))



