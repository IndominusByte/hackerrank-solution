# revenue = [1,2,3,1,6,10]
# k = 2
# revenue = [5,6,4,2,10,8,4]
# k = 3
# revenue = [1,2,3,4,5]
# k = 4
revenue = [16,28,37,8,47,30,36,6,0,37]
k = 3

for x in range(len(revenue)):
    for i in range(len(revenue)):
        tmp = None
        if revenue[x] > revenue[i]:
            tmp = revenue[x]
            revenue[x] = revenue[i]
            revenue[i] = tmp

result = list()
for j in range(1,k + 1):
    result.append(revenue[:k])
    del revenue[:k]

revenue = list()
for r in result:
    if len(r) == k:
        revenue.append(r)

last = list()
for t in revenue:
    for w in t:
        last.append(w)

print(last)
print(sum(last))
# [10, 6, 3, 2,      1, 1] = 2
# [10, 8, 6, 5, 4, 4,   2] = 3
# [5, 4, 3, 2,          1] = 4
