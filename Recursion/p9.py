#Write a recursive program to print the even numbers in a given range.
def print_even(start,end):
    if start>end:
        return
    if start%2==0:
        print(start)

    print_even(start+1,end)




def main():
    var1=int(input("Enter the 1st: "))
    var2 = int(input("Enter the 2nd: "))
    print_even(var1,var2)
main()
