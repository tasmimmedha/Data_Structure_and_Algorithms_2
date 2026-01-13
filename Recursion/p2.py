#Print element of Fibonacci series:
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def print_fibonacci_series(position):
    for i in range(position):
        result = fibo(i)
        print(result,end=' ')

def main():
    num = int(input('Enter the number of elements in the Fibonacci series: '))
    print_fibonacci_series(num)

main()