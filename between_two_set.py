# a = [2, 4]
# b = [16, 32, 96]
# output = 3
# a = [3, 4]
# b = [24, 48]
# output = 2

a = [2,6]
b = [24,36]
# answer = [6,12]

# for x in range(2,b[-1]):
#     if (x % a[0]) == (x % a[1]) == (b[0] % x) == (b[1] % x) == (b[2] % x):
#         print(x)

result = list()
for mod in range(1,b[-1] * 2):
    answer = list()
    for x in a:
        answer.append(mod % x)
    for j in b:
        answer.append(j % mod)

    if len(set(answer)) == 1:
        result.append(mod)

print(result)
print(len(result))
