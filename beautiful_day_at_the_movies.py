i = 20
j = 23
k = 6

result = [x for x in range(i,j + 1) if abs(x - int(str(x)[::-1])) % k == 0]
print(result)
