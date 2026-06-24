"""
name: inverted-hollow-pyramid
Purpose: This code generates an inverted hollow pyramid star pattern based on the input number `n`.

"""
n = int(input("Enter a number: "))
for i in range(n):
    for s in range(i):
        print(" ", end=" ")
    for j in range(2 * (n - i) - 1):
        if i == 0 or i == n-1 or j == 0 or j == 2 * (n - i) - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()