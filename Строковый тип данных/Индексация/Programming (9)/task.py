# put your python code here
s = input ()
vowels = 0
consonants = 0
for i in s:
     if i in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
      vowels += 1
     if i in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
      consonants += 1
print (f'Количество гласных букв равно {vowels}')
print  (f'Количество согласных букв равно {consonants}')