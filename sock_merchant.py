arr = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]

sock = sum([int(arr.count(x) / 2) for x in list(set(arr))])

print(sock)
