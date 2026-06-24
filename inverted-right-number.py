"""
name: inverted-right-number
Purpose: This code generates an inverted right number pattern based on the input number `n`.

"""
n=int(input("Enter the number of rows: "))
x = n * (n + 1) // 2 #if n=5 x= 5*(5+1)/2= 15
y = x
for i in range(n):
    for j in range(n, i, -1):
        print(y, end=" ")
        y -= 1
    print()