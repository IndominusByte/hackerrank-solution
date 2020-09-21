s = [2,5,1,3,4,4,3,5,1,1,2,1,4,1,3,3,4,2,1]
d = 18
m = 7
# result = 3
# s = [1,2,1,3,2]
# d = 3
# m = 2

# result = list()
# for x in range(len(s) + 1):
#     try:
#         if s[x] + s[x + 1] == d:
#             result.append([s[x],s[x + 1]])
#     except IndexError:
#         if s[x] == d and len(result) == 0:
#             result.append([s[x]])
#         break

# print(len(result))

result = list()
for x in range(len(s)):
    if sum(s[x:m + x]) == d:
        result.append(s[x:m + x])

print(len(result))
