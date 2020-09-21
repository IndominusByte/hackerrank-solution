def main():
    keyboards = [4]
    drives = [5]
    b = 5

    answer = -1

    range_b = list()
    for key in keyboards:
        for drive in drives:
            range_b.append(int(key) + int(drive))

    range_b.sort()
    for x in range_b[::-1]:
        if b >= x:
            return x
            break

    return answer


print(main())
