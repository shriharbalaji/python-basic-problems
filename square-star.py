"""
name: square-star
Purpose: This code generates a square star pattern based on the input number `a`.

"""
a=int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        print("*",end="")
    print()