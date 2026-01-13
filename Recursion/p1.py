# position element of Fibonacci
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def main():
    num = int(input('Enter a number: '))
    result = fibo(num)
    print(num, 'Position element of Fibonacci', result)


main()
