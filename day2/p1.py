matrix = [[1,2,3],[4,5,6],[7,8,9]]

    # print(li[i])
    # for j in range(0,len(li[i])):
    #     print(li[i][j])
rows = len(matrix)
colns = len(matrix[0])
# transpose = [[0 for j in range(rows)] for i in range(colns)]
# for i in range(rows):
#     for j in range(colns):
#         transpose[j][i] = matrix[i][j]
# for row in transpose:
#     print(row)
transpose = []
for i in range(colns):
    row = []
    for j in range(rows):
        row.append(matrix[j][i])
    transpose.append(row)
for row in transpose:
    print(row)