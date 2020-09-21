period = [0,1,2,3,4,5]
height = [1,2,3,6,7,14]

def utopianTree(tree):
    n = 0
    h = list()
    for x in range(61):
        if x == 0 or x == 1:
            n += 1
            h.append((x,n))
        if x % 2 == 0 and x != 0:
            n += 1
            h.append((x,n))
        if x % 2 != 0 and x != 1:
            r = n * 2
            n = r
            h.append((x,n))

    for i in h:
        if tree == i[0]:
            return i[1]


for x in range(6):
    result = utopianTree(x)
    print(result)
