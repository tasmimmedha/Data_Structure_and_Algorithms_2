# Write a recursive program to reverse print an array of size n in given order.
def array_print(arr, index=0):
    if index == len(arr):
        return

    array_print(arr, index + 1)
    print(arr[index])


def main():
    arr = [1, 3, 5, 7, 10]
    array_print(arr)


main()