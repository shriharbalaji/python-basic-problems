"""
name: mirror-rhombus
Purpose: This code generates a mirror rhombus star pattern based on the input number `n`.

"""
n=int(input("Enter a number: "))
for i in range(n):
    print(" " * (n - i - 1), end=" ")
    for j in range(n):
        print("*", end=" ")
    print()