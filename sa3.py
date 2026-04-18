def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
l=int(input("Enter the number: "))
res=fact(l)
print(f"Factorial of {l} is: ",res)
