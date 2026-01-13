#Write a recursive program to find the maximum of the elements of an array of size n.

def Max_Element(arr, n):
    if n == 1:
        return arr[0]
    else:
        i = arr[n - 1]
        result = Max_Element(arr, n - 1)
        return i if i > result else result

def main():
    arr = [1, 2, 3, 4, 7, 10]
    print(Max_Element(arr, len(arr)))

main()
