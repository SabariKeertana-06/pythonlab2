#Finding Factorial
n = int(input("Enter value of n :"))
i = 1
fact =1
for i in range(1,n+1):
    fact = fact*i
    i=i+1
print("The factorial of the given number is :",fact)
