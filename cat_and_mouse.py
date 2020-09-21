def main(x,y,z):
    # cat a
    x = x
    # cat b
    y = y
    # mouse c
    z = z

    distance = list()
    if (z > x and z > y) or (z < x and z < y):
        # if all cat in left
        if z > x and z > y:
            if x > y:
                distance = [('b',y),('a',x),('c',z)]
            else:
                distance = [('a',x),('b',y),('c',z)]
        # if all cat in right
        if z < x and z < y:
            if x < y:
                distance = [('c',z),('a',x),('b',y)]
            else:
                distance = [('c',z),('b',y),('a',x)]
    else:
        # if mouse in between cat
        if x < z:
            distance = [('a',x),('c',z),('b',y)]
        else:
            distance = [('b',y),('c',z),('a',x)]

    a_distance = 0
    b_distance = 0
    if distance[1][0] == 'c':
        for x in distance:
            if x[0] == 'a':
                a_distance = distance[1][1] - x[1]
            if x[0] == 'b':
                b_distance = distance[1][1] - x[1]

        if abs(a_distance) == abs(b_distance):
            return "Mouse C"
        if abs(a_distance) < abs(b_distance):
            return "Cat A"
        return "Cat B"

    if distance[-1][0] == 'c':
        for x in distance:
            if x[0] == 'a':
                a_distance = distance[1][1] - x[1]
            if x[0] == 'b':
                b_distance = distance[1][1] - x[1]

    if distance[0][0] == 'c':
        for x in distance:
            if x[0] == 'a':
                a_distance = x[1] - distance[1][1]
            if x[0] == 'b':
                b_distance = x[1] - distance[1][1]

    if abs(a_distance) == abs(b_distance):
        return "Mouse C"
    if abs(a_distance) < abs(b_distance):
        return "Cat A"
    return "Cat B"


print(main(x=3,y=3,z=1))
