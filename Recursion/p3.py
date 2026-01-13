
#Factorial
def fact(n):
    if n==1:
        return 1
    else:
        return n *fact(n-1)

def main():
    num =int(input('Enter a number:'))
    result=fact(num)
    print('Factorial of',num,':',result)
main()