#nth sum
def sumNum(n):
    if n == 0:               # Base case
        return 0
    else:
        return n + sumNum(n - 1)  # Recursive case

def main():
    num = int(input('Numbers of values to sum: '))
    result = sumNum(num)
    print('Sum of values:', result)

main()
