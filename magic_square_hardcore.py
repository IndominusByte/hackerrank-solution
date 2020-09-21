from copy import deepcopy

def get_vertical(arr):
    vertical = list()
    # get vertical
    for x in range(len(arr)):
        ver = list()
        for i in range(len(arr)):
            ver.append(arr[i][x])
        vertical.append(ver)

    return vertical

def get_horizontal(arr):
    s = deepcopy(arr)
    return [x for x in s]

def get_right_diagonal(arr):
    return [arr[x][len(arr) - x - 1] for x in range(len(arr))]

def get_left_diagonal(arr):
    return [arr[x][x] for x in range(len(arr))]

def main(arr):
    odd_num = [1,3,7,9]
    loop = True
    diagonal_index = 0
    v_index = 0

    while loop:
        print("===================================")
        matrix_ori = deepcopy(arr)

        filter_ = list()
        # center has to be 5
        if arr[1][1] != 5:
            filter_.append((arr[1][1],5))
            arr[1][1] = 5

        # 3 x 3 matrix
        horizontal = get_horizontal(arr)
        vertical = get_vertical(arr)
        right_to_left = get_right_diagonal(arr)
        left_to_right = get_left_diagonal(arr)

        # =============== vertical center ===============
        # if vertical[1][0] in odd_num and vertical[1][-1] not in odd_num:
        #     for x in odd_num:
        #         if (
        #             x not in horizontal[1] and
        #             sum([vertical[1][0],5,x]) == 15
        #         ):
        #             filter_.append((vertical[1][-1],x))
        #             vertical[1][-1] = x
        #             arr[-1][1] = x

        # if vertical[1][-1] in odd_num and vertical[1][0] not in odd_num:
        #     for x in odd_num:
        #         if (
        #             x not in horizontal[1] and
        #             sum([x,5,vertical[1][-1]]) == 15
        #         ):
        #             filter_.append((vertical[1][0],x))
        #             vertical[1][0] = x
        #             arr[0][1] = x

        v_center = list()
        if (vertical[1][0] not in odd_num and vertical[1][-1] not in odd_num) or sum(vertical[1]) != 15:
            for x in odd_num:
                for i in odd_num:
                    if (
                        x not in horizontal[1] and
                        i not in horizontal[1] and
                        sum([x,5,i]) == 15
                    ):
                        v_center.append([x,5,i])

        if len(v_center) > 0:
            print("v center -> ",v_center)
            for x in range(0,len(vertical[1]),2):
                for i in range(0,len(v_center[v_index]),2):
                    if (
                        vertical[1][x] != v_center[v_index][i] and
                        v_center[v_index][i] not in vertical[1][0::2] and
                        vertical[1][x] not in v_center[v_index][0::2]
                    ):
                        filter_.append((vertical[1][x],v_center[v_index][i]))
                        vertical[1][x] = v_center[v_index][i]
                        arr[x][1] = v_center[v_index][i]

        # reset all value
        horizontal = get_horizontal(arr)
        vertical = get_vertical(arr)
        right_to_left = get_right_diagonal(arr)
        left_to_right = get_left_diagonal(arr)

        # progres fix
        # ================== diagonal left ====================
        l_r = list()
        if sum(left_to_right) != 15:
            for x in range(2,10,2):
                for i in range(2,10,2):
                    if (
                        x not in right_to_left and
                        i not in right_to_left and
                        sum([x,5,i]) == 15
                    ):
                        l_r.append([x,5,i])

        if len(l_r) > 0:
            print("left diagonal -> ",l_r)
            for x in range(0,len(left_to_right),2):
                for i in range(0,len(l_r[diagonal_index]),2):
                    if (
                        left_to_right[x] != l_r[diagonal_index][i] and
                        l_r[diagonal_index][i] not in left_to_right[0::2] and
                        left_to_right[x] not in l_r[diagonal_index][0::2]
                    ):
                        filter_.append((left_to_right[x],l_r[diagonal_index][i]))
                        left_to_right[x] = l_r[diagonal_index][i]
                        arr[x][x] = l_r[diagonal_index][i]

        # reset all value
        horizontal = get_horizontal(arr)
        vertical = get_vertical(arr)
        right_to_left = get_right_diagonal(arr)
        left_to_right = get_left_diagonal(arr)

        # =============== horizontal last ===============
        if sum(horizontal[-1]) != 15:
            for x in range(2,10,2):
                if sum([x,horizontal[-1][1],horizontal[-1][2]]) == 15:
                    filter_.append((horizontal[-1][0],x))
                    horizontal[-1][0] = x
                    arr[-1][0] = x

        # reset all value
        horizontal = get_horizontal(arr)
        vertical = get_vertical(arr)
        right_to_left = get_right_diagonal(arr)
        left_to_right = get_left_diagonal(arr)

        # ============ vertical one ==================
        if sum(vertical[0]) != 15:
            for x in odd_num:
                if sum([vertical[0][0],x,vertical[0][-1]]) == 15:
                    filter_.append((vertical[0][1],x))
                    vertical[0][1] = x
                    arr[1][0] = x

        # reset all value
        horizontal = get_horizontal(arr)
        vertical = get_vertical(arr)
        right_to_left = get_right_diagonal(arr)
        left_to_right = get_left_diagonal(arr)

        # ============ horizontal center ============
        if sum(horizontal[1]) != 15:
            for x in odd_num:
                if sum([horizontal[1][0],5,x]) == 15:
                    filter_.append((horizontal[1][-1],x))
                    horizontal[1][-1] = x
                    arr[1][-1] = x

        # reset all value
        horizontal = get_horizontal(arr)
        vertical = get_vertical(arr)
        right_to_left = get_right_diagonal(arr)
        left_to_right = get_left_diagonal(arr)

        # ============ diagonal right ============
        if sum(right_to_left) != 15:
            for x in range(2,10,2):
                if sum([x,right_to_left[1],right_to_left[-1]]) == 15:
                    filter_.append((right_to_left[0],x))
                    right_to_left[0] = x
                    arr[0][-1] = x

        # reset all value
        horizontal = get_horizontal(arr)
        vertical = get_vertical(arr)
        right_to_left = get_right_diagonal(arr)
        left_to_right = get_left_diagonal(arr)

        if (
            sum(right_to_left) == 15 and
            sum(left_to_right) == 15 and
            [sum(x) for x in horizontal] == [15,15,15] and
            [sum(x) for x in vertical] == [15,15,15]
        ):
            for x in arr:
                print(x)
            print("")
            print("=== SUM ===")
            print("right diagonal -> ",sum(right_to_left))
            print("left diagonal -> ",sum(left_to_right))
            print("horizontal -> ",[sum(x) for x in horizontal])
            print("vertical -> ",[sum(x) for x in vertical])

            print("=== FILTER ===")
            print("filter -> ",filter_)
            print(sum([abs(x[0] - x[1]) for x in filter_]))

        arr = matrix_ori
        diagonal_index += 1

        if diagonal_index == len(l_r):
            v_index += 1
            diagonal_index = 0

        if (
            # sum(right_to_left) == 15 and
            # sum(left_to_right) == 15 and
            # [sum(x) for x in horizontal] == [15,15,15] and
            # [sum(x) for x in vertical] == [15,15,15]
        ):
            loop = False
            return sum([abs(x[0] - x[1]) for x in filter_])


if __name__ == '__main__':
    # arr = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
    # arr = [[4,9,2],[3,5,7],[8,1,5]]
    # arr = [[4,8,2],[4,5,7],[6,1,6]]

    # arr = [[4,5,8],[2,4,1],[1,9,7]]
    arr = [[4,4,7],[3,1,5],[1,7,9]]
    # arr = [[2,2,7],[8,6,4],[1,2,9]]

    # arr = [[6,1,7],[3,5,7],[1,9,4]]
    # arr = [[6,1,7],[3,5,7],[1,9,4]]
    # arr = [[8,1,7],[3,5,7],[1,9,2]]

    # arr = [[2,2,7],[8,6,4],[1,2,9]]

    print(main(arr))
