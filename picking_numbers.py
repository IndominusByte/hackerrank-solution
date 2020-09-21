# a = [1,1,2,2,4,4,5,5,5]
# a = [4,6,5,3,3,1]
# a = [1,2,2,3,1,2]

with open('test.txt') as f:
    tmp = f.read().strip('\n').split(' ')

a = [int(x) for x in tmp]

print(a)
print("")

a.sort()

s = 1
start = 0
result = list()
while start != len(a):
    pos = list()
    # filter one
    for x in range(s,len(a)):
        if abs(a[start] - a[x]) <= 1:
            if len(pos) == 0:
                pos.append(a[start])
            pos.append(a[x])

    # filter two
    if len(pos) >= 2:
        f_s = 1
        f_start = 0
        while f_start != len(pos):
            for x in range(f_s,len(pos)):
                try:
                    if abs(pos[f_start] - pos[x]) <= 1:
                        if abs(pos[x - 1] - pos[x]) > 1:
                            del pos[x - 1]
                except IndexError:
                    pass
            f_s += 1
            f_start += 1

        result.append(pos)
        print("pos -> ",pos,"--",len(pos))

    s += 1
    start += 1

print("")
print("len all item -> ",[len(x) for x in result])
print("max -> ",max([len(x) for x in result]))
