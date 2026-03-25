def input_matrix(r, c, name):
    matrix = []
    print("\nEnter elements of Matrix", name)
    for i in range(r):
        row = []
        for j in range(c):
            row.append(int(input(f"Element[{i+1}][{j+1}]: ")))
        matrix.append(row)
    return matrix

r1 = int(input("Enter rows of Matrix A: "))
c1 = int(input("Enter columns of Matrix A: "))
r2 = int(input("Enter rows of Matrix B: "))
c2 = int(input("Enter columns of Matrix B: "))

A = input_matrix(r1, c1, "A")
B = input_matrix(r2, c2, "B")

print("\n1. Matrix Addition")
print("2. Matrix Multiplication")

choice = int(input("Enter choice: "))

if choice == 1:
    if r1 == r2 and c1 == c2:
        result = [[A[i][j] + B[i][j] for j in range(c1)] for i in range(r1)]
        print("Addition Result:")
        for row in result:
            print(row)
    else:
        print("Addition not possible")

elif choice == 2:
    if c1 == r2:
        result = [[0 for j in range(c2)] for i in range(r1)]
        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    result[i][j] += A[i][k] * B[k][j]

        print("Multiplication Result:")
        for row in result:
            print(row)
    else:
        print("Multiplication not possible")


