# a = [1,2,3]
# queries = [0,1,2]
# k = 1
# while x + 1 > 0:
#     if x == 0: print([a[x] for x in queries])
#     a = [a[-1]] + a[:-1]
#     x -= 1

k = 66957

with open('a.txt') as f:
    a = [int(x) for x in f.read().strip('\n').split(' ')]

with open('queries.txt') as f:
    queries = [int(x) for x in f.read().strip('\n').split('\n')]

x = k % len(a)
a = a[-x:] + a[:-x]
print([a[x] for x in queries])
