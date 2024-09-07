def transposeMatrix(matrix):
    # Write your code here.
    n = len(matrix)
    m = len(matrix[0])
    # print(f"{n} x {m} matrix")
    if n == m and n == 1:
        return matrix
    result = []
    for i in range(0,m):
        row = []
        for j in range(0, n):
            # print(f"Appending: {matrix[j][i]}")
            row.append(matrix[j][i])
        # print(f"Row: {row}")
        result.append(row)
    return result
