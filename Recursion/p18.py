
#Write a recursive program to count the prime numbers of an array of n integers


def is_prime(num, divisor=2):
    if num < 2:
        return False
    if divisor * divisor > num:
        return True
    if num % divisor == 0:
        return False
    return is_prime(num, divisor + 1)

def count_primes(arr, index=0, count=0):
    if index == len(arr):
        return count
    if is_prime(arr[index]):
        count += 1
    return count_primes(arr, index + 1, count)

def main():
    arr = [1, 2, 3, 4, 5, 9, 11, 13, 15, 17]
    prime_count = count_primes(arr)
    print("Total prime numbers in the array:", prime_count)

main()
