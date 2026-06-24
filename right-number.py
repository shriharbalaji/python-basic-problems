"""
name: right-number
Purpose: This code generates a right number pattern based on the input number `n`.

"""
n=int(input("Enter a number: "))
a = 1
for i in range(n):
    for j in range(i+1):
        print(a, end=" ")
        a = a+1
    print()