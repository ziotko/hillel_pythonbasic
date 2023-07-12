A: int = int(input("Enter the first number A: "))
B = int(input("Enter the second number B: "))

if A < B:
    for num in range(A, B+1):
        print(num, end=" ")
else:
    for num in range(A, B-1, -1):
        print(num, end=" ")
