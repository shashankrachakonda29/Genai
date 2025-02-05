# Half pyramid
n=int(input("Enter any number:"))
for i in range(n+1):
    for j in range(i):
        print(j+1,end=' ')
    print()

# Inverted Half pyramid
n=int(input("Enter any number:"))
for i in range(n,0,-1):
    for j in range(i):
        print(j+1,end=' ')
    print()