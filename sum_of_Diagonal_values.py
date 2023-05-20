def calculateDiagonalSum(matrix):
    diagonalSum = 0
    n = len(matrix)

    for i in range(n):
        diagonalSum += matrix[i][i]  # Add main diagonal element
        diagonalSum += matrix[i][n - i - 1]  # Add anti-diagonal element

    # Subtract the center element as it is added twice
    if n % 2 == 1:
        diagonalSum -= matrix[n // 2][n // 2]

    return diagonalSum


# Read input N and M
N, M = map(int, input().split())

# Read matrix elements
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

# Calculate diagonal sum
diagonalSum = calculateDiagonalSum(matrix)
print(diagonalSum)
