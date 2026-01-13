#Write a function print_even using divide-and-conquer algorithm to print the even numbers of an array of n integers.

def even(num):
    return True if num % 2 == 0 else False

def count_even(arr, start, end):
    if start == end:   # Base case: only one element
        return 1 if even(arr[start]) else 0
    else:   # Divide the array into two halves
        mid = (start + end) // 2
        left_count = count_even(arr, start, mid)
        right_count = count_even(arr, mid + 1, end)
        return left_count + right_count

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Array:", arr)
    result = count_even(arr, 0, len(arr)-1)
    print("Count of even numbers:", result)

main()
