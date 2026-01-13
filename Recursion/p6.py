# max Element in array

def Max_Element(arr, n):
    if n == 1:
        return arr[0]
    else:
        i = arr[n - 1]
        result = Max_Element(arr, n - 1)
        return i if i > result else result


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
    print(Max_Element(arr, len(arr)))


main()