def calculate_absolute_difference(matrix1, matrix2):
    size = len(matrix1)
    absolute_diff = [[abs(matrix1[i][j] - matrix2[i][j]) for j in range(size)] for i in range(size)]
    return absolute_diff

# Get the size of the matrices
N = int(input())

# Input elements of matrix A

matrixA = [[int(x) for x in input().split()] for _ in range(N)]

# Input elements of matrix B

matrixB = [[int(x) for x in input().split()] for _ in range(N)]

# Calculate absolute difference
absolute_difference = calculate_absolute_difference(matrixA, matrixB)

# Print the absolute difference matrix
for row in absolute_difference:
    print(*row)
