def odd_print(arr, start, end):
    if start == end:
        if arr[start] % 2 != 0:  # print odd numbers
            print(arr[start])
    else:
        mid = start + (end - start) // 2
        odd_print(arr, start, mid)
        odd_print(arr, mid + 1, end)


def main():
    arr = [2, 3, -1, 8, 9, 17, 10]
    odd_print(arr, 0, len(arr) - 1)


main()
