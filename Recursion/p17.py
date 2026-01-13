#Write a recursive program to count the odd/even numbers of an array of n integers
def count_odd_even(arr, index=0, odd=0, even=0):
    if index == len(arr):
        return odd, even

    if arr[index] % 2 == 0:
        even += 1
    else:
        odd += 1

    return count_odd_even(arr, index + 1, odd, even)

def main():
    arr = [1, 4, 5, 6, 7, 8, 10, 11, 15]
    odd_count, even_count = count_odd_even(arr)
    print("Odd numbers:", odd_count)
    print("Even numbers:", even_count)

main()
