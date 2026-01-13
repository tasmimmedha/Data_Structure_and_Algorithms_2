#print the reverse order

def printRevers(n):
    if n == 0:  # Base case: stop recursion when n reaches 0
        return
    print(n)
    printRevers(n - 1)


def main():
    num = int(input('Enter value : '))
    printRevers(num)


main()


