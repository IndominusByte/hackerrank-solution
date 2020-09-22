n = 499999999
m = 999999998
s = 2

# noob version
# answer = 0
# while m > 0:
#     print("===",m)
#     i = s
#     while i < n + 1 and m > 0:
#         answer = i
#         print(answer)
#         i += 1
#         m -= 1
#     s = 1
print(((s - 1 + m - 1) % n) + 1)
