arr = [1, 4, 4, 4, 5, 3]
# arr = [1,2,3,4,5,4,3,2,1,3,4]

# with open('test.txt') as f:
#     arr = f.read().strip('\n').split(' ')

type_ = [(x,arr.count(x)) for x in set(arr)]
high_freq = max([x[-1] for x in type_])
low_type = [x for x in type_ if x[-1] == high_freq]

print(type_)
print(high_freq)
print(low_type[0][0])
