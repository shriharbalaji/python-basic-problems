n=int(input("Enter a number: "))
for i in range(n):
    for s in range(n-i-1):
        print(" ", end=" ")
    for j in range(2*i+1):
        if i == 0 or i == n-1 or j == 0 or j == 2*i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()