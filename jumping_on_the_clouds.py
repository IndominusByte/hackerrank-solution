c = [0,0,1,0]
k = 2

x = 0
alive = 100
while (x + k) % len(c) > 0:
    if c[(x + k) % len(c)] == 1: alive -= 3
    else: alive -= 1
    x += k

if c[(x + k) % len(c)] == 1: alive -= 3
else: alive -= 1
print(alive)
