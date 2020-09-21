viral = [(1,5,2,2)]

for x in range(1,51):
    shared = int(viral[x - 1][1] / 2) * 3
    liked = int(shared / 2)
    cumulative = liked + viral[x - 1][-1]
    viral.append((x + 1,shared,liked,cumulative))

n = 4
print(viral)
print([x for x in viral if x[0] == n][0][-1])
