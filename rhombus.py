"""
name: rhombus
Purpose: This code generates a rhombus star pattern based on the input number `n`.

"""
n=int(input("Enter a number: "))
for i in range(n):
    print(" " * i, end=" ")
    for j in range(n):
        print("*", end=" ")
    print()