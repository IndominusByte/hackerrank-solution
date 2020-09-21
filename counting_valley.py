path = 'DDUUDDUDUUUD'

val = [-1 if x == 'D' else 1 for x in path]
start = [val[0]]

for x in range(1,len(val)):
    start.append(start[x - 1] + val[x])

valley = 0
for x in range(1,len(start)):
    if start[x] == 0 and start[x - 1] < 0:
        valley += 1

print(valley)
