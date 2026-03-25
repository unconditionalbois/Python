n = int(input("Enter size of matrix: "))
matrix = []

print("Enter matrix elements:")

for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    matrix.append(row)

print("Matrix:")
for row in matrix:
    print(row)

print("\nSum of rows:")
for i in range(n):
    print("Row", i+1, "=", sum(matrix[i]))

print("\nSum of columns:")
for j in range(n):
    s = 0
    for i in range(n):
        s += matrix[i][j]
    print("Column", j+1, "=", s)

main_diag = 0
sec_diag = 0

for i in range(n):
    main_diag += matrix[i][i]
    sec_diag += matrix[i][n-i-1]

print("Main diagonal sum:", main_diag)
print("Secondary diagonal sum:", sec_diag)

