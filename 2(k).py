#To Check a number is PRIME or NOT
n = int(input("Enter value of n :"))
if n >1:
    for i in range (2,n):
        if (n%i)==0:
            print( n, "is NOT a PRIME number")
            break
    else:
        print(n,"is a PRIME number")
else:
    print(n,"is NOT a PRIME number")
    
