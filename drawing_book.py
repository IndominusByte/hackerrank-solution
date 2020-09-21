# book page
n = 6
# first page opened
p = 2

book = list(zip([x for x in range(0,n + 2,2)],[0 if x == n + 1 else x for x in range(1,n + 2,2)]))
first = list()
last = list()
for page in book:
    first.append(page)
    if p in page:
        break

book.reverse()
for page in book:
    last.append(page)
    if p in page:
        break

result = len(first) - 1 if len(first) < len(last) else len(last) - 1
print(result)
