scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]

high = [scores[0]]
low = [scores[0]]

for x in range(len(scores)):
    if scores[x] > high[x]:
        high.append(scores[x])
    else:
        high.append(high[x])

for x in range(len(scores)):
    if scores[x] < low[x]:
        low.append(scores[x])
    else:
        low.append(low[x])

high.pop(0)
low.pop(0)

high_result = [value for index, value in enumerate(high) if value > high[index - 1]]
low_result = [value for index, value in enumerate(low) if value < low[index - 1]]

print(high_result)
print(low_result)
