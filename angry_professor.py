k = 3
a = [-1, -3, 4, 2]

result = 'NO' if len([x for x in a if x <= 0]) >= k else 'YES'
print(result)
