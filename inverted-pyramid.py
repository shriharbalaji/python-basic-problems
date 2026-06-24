"""
name: inverted-pyramid
Purpose: This code generates an inverted pyramid star pattern based on the input number `n`.

"""
n = int(input("Enter a number: "))
for i in range(n):
    for s in range(i):
        print(" ", end="")
    for j in range(n - i):
        print("* ", end="")
    print()