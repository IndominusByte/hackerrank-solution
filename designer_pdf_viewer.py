h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
word = 'abc'
# h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
# word = 'zaba'

index = list()
for x in word:
    for i in [(x,chr(97 + x)) for x in range(26)]:
        if x == i[1]:
            index.append(i[0])

num = list()
for x in index:
    num.append(h[x])

print(num)
print(max(num) * len(word))
