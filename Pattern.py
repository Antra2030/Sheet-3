n=int(input())
m=int(input())
for i in range (0,n-1):
    for j in range(0,m-1*i):
        print("*",end=" ")
    print()
