# fibbonacci series
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
print("fibbonacci series")
for i in range(1,10):
    print(fib(i),end=" ")