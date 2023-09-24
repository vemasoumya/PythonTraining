def squarefunc(item):
    return item * item 

func = lambda x: x * x
print(func(10))

l1 = [1,3,5,9]
l2 = [squarefunc(i) for i in l1]
l3 = [func(i) for i in l1]
l4 = [i*i  for i in l1]
print(l1)
print(l2)
print(l3)
print(l4)



