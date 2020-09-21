x1 = 14
v1 = 4
x2 = 98
v2 = 2

jump = 100
k1 = [x for x in range(x1,x1 + v1 * jump + 1,v1)]
k2 = [x for x in range(x2,x2 + v2 * jump + 1,v2)]

if len([k1[x] for x in range(jump) if k1[x] == k2[x]]) > 0:
    print('YES')
else:
    print('NO')
