#Write a recursive program to find the products of the elements of an array of size n.
def product_array(arr, index=0):
    if index == len(arr):
        return 1

    return arr[index]*product_array(arr, index +1)


def main():
    arr = [1, 2,5,10]
    total= product_array(arr)
    print(total)


main()