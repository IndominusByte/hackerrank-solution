bill = [3,10,2,9]
k = 1
b = 7

split = sum([value for index,value in enumerate(bill) if index != k]) / 2
if split == b:
    print("Bon Appetit")
print(abs(split - b))
