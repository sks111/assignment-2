l=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
m=[]
for i in range(0,len(l)):
 if len(l[i])==0:
    continue
 else:
     m.append(l[i])
print(m)