"""
name: hollow-square-star
Purpose: This code generates a hollow square star pattern based on the input number `n`.

"""
n=int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        if (i == 1 or i == 2) and (j == 1 or j == 2):
            print(" ", end="\t")
        else:
            print("*", end="\t")
    print()