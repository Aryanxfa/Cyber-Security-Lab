print("\033[1mDictionary Attack: \033[0m")
print()
dictionary=["1111","124","125684","abcd","ABCD","mno","PQR","pqrs","0000","9999"]
x=str(input("Enter a Password: "))
if (x in dictionary):
    print("\033[102m    \033[0m Password found in Dictionary",x)
else:
    print("\033[101m    \033[0m Password does not exists in Dictionary")
