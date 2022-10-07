print("Enter a two digit key to Brute Force")
x =  int(input())
for i in range(99999):
    print(i,end=" ")
    if(i==x):
        print()
        print("Password is",i)
        break
