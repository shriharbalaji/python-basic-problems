"""
name: full-pyramid-star
Purpose: This code generates a full pyramid star pattern based on the input number `n`.

"""
n=int(input("Enter a number: "))
for i in range(n):
    for s in range(-n, -i):
        print(" ", end="")
    for j in range(i+1):
        print("* ", end="")
    print()