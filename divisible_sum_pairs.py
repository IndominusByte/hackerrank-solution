# k = 5
# arr = [1,2,3,4,5,6]
k = 3
arr = [1,3,2,6,1,2]

start = 1
result = list()
for i in range(len(arr)):
    for j in range(start,len(arr)):
        if (arr[i] + arr[j]) % k == 0:
            result.append([arr[i],arr[j]])
    start += 1

print(result)
