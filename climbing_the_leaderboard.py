# ranked = [100, 100, 50, 40, 40, 20, 10]
# player = [5, 25, 50, 120]
ranked = [100, 90, 90, 80, 75, 60]
player = [50, 65, 77, 90, 102]

# for x in player:
#     tmp_pos = list()
#     for i in range(len(rank)):
#         if i == 0 and x < rank[i][1]:
#             tmp_pos.append(rank[i][0] + 1)

#         if x >= rank[i][1]:
#             tmp_pos.append(rank[i][0])

#         print("pos -> ",tmp_pos)
#         print("x -> ",x)
#         print("rank -> ",rank[i])
#     print("")

#     position.append(tmp_pos[-1])

# rank = list(set(ranked))
# rank.sort(reverse=True)
# rank = [(x + 1,rank[x]) for x in range(len(rank))][::-1]

# position = list()
# for x in player:
#     i = 0
#     if x < rank[i][1]:
#         position.append(rank[i][0] + 1)
#         continue

#     try:
#         while x >= rank[i][1]: i += 1
#         if x >= rank[i - 1][1]:
#             position.append(rank[i - 1][0])
#     except IndexError:
#         if x >= rank[i - 1][1]:
#             position.append(rank[i - 1][0])

# print(position)

# ============== new
# rank = list(set(ranked))
# l_r = len(rank)
# rank.sort()

# position = list()
# for x in player:
#     i = 0

#     if x < rank[i]:
#         position.append(l_r + 1)
#         continue

#     try:
#         while x >= rank[i]:
#             i += 1
#         if x >= rank[i - 1]:
#             position.append(l_r + 1 - i)
#     except IndexError:
#         if x >= rank[i - 1]:
#             position.append(1)

# print(position)

# ============== new
rank = list(set(ranked))
rank.sort()
l_r = len(rank)

i = 0
position = list()
for x in player:
    while l_r > i and x >= rank[i]:
        i += 1
    position.append(l_r + 1 - i)

print(position)
