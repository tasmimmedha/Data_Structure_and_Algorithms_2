#Write a recursive program to find the sum of the elements of an array of size n.

def sum_array(arr, index=0):
    if index == len(arr):
        return 0

    return arr[index] + sum_array(arr, index + 1)#starting value 1 +3+5+7+10=26


def main():
    arr = [1, 3, 5, 7, 10]
    total= sum_array(arr)
    print(total)


main()