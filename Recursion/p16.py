#Write a recursive program to print the prime numbers of an array of n integers


def is_prime(num, divisor=2):
    if num < 2:
        return False
    if divisor * divisor > num:
        return True
    if num % divisor == 0:
        return False
    return is_prime(num, divisor + 1)

def print_primes(arr, index=0):
    if index == len(arr):
        return
    if is_prime(arr[index]):
        print(arr[index], end=' ')
    print_primes(arr, index + 1)

def main():
    arr = [3, 4, 7, 10, 13, 17, 22, 1, 0, 19]
    print("Prime numbers in the array are:")
    print_primes(arr)

main()
