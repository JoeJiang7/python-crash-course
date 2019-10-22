import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
c = {'c': 'E'}

m1 = collections.ChainMap(a, b)
m2 = collections.ChainMap(c,*m1)

print(m1)
print(m1.maps)
print(*m1.maps)

print(m1.maps.pop())
print(m2)
print('m1["c"] = {}'.format(m1['c']))
print('m2["c"] = {}'.format(m2['c']))