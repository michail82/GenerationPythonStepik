# put your python code here
d_age = float(input())
h_age = float()
year = 4
if d_age == 1:
    h_age = 10.5
elif d_age == 2:
    h_age = 2*10.5
elif d_age >= 3:
    h_age = (21 + (year * (d_age - 2)))
print (h_age)