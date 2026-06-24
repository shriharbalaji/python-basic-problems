"""
name: diamond-star
Purpose: This code generates a diamond star pattern based on the input number `n`.

"""
n = int(input("Enter the Number: "))
for i in range(0, n):
    for j in range(0, n-i-1):
        print(" ",end="")
    for j in range(0, i*2+1):
        print("*", end="")
    print()
for i in range(1, n):
    for j in range(0, i):
        print(" ",end="")
    for j in range(0, (n-i)*2-1):
        print("*", end="")
    print()