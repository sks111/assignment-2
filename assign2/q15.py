set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {1, 2, 3}

set3 = set1.intersection(set2)

if set3 == set2:
 print("set2:",set2,"is a subset of set1:",set1)
else:
 print("set2 not a subset of set1")