# put your python code here
# put your python code here
city1 = input()
city2 = input()
city3 = input()
n_city1 = len(city1)
n_city2 = len(city2)
n_city3 = len(city3)
if  n_city2 > n_city1 <  n_city3 and n_city2 < n_city3:
    print (city1)
    print (city3) # При этой комбинации 1 наименьшее 3 наибольше
elif  n_city1 > n_city3 <  n_city2 and n_city2 < n_city1:
    print (city3)
    print (city1) # При этой комбинации 3 наименьшее 1 наибольше


elif  n_city1 > n_city2 <  n_city3 and n_city3 < n_city1:
    print (city2)
    print (city1) # При этой комбинации 2 наименьшее 1 наибольше
elif  n_city3 > n_city1 <  n_city2 and n_city3 < n_city2:
    print (city1)
    print (city2) # При этой комбинации 1 наименьшее 2 наибольше


elif  n_city1 > n_city2 <  n_city3 and n_city1 < n_city3:
    print (city2)
    print (city3) # При этой комбинации 2 наименьшее 3 наибольше
elif  n_city1 > n_city3 <  n_city2 and n_city1 < n_city2:
    print (city3)
    print (city2) # При этой комбинации 3 наименьшее 2 наибольше
else:
    print ('test')



