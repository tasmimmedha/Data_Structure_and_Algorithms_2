# Calculate a to the power b

def Power_Of_Element(base, n):
    if n == 0:
        return 1
    else:
        return base * Power_Of_Element(base, n - 1)


def main():
    base = int(input('Base value :'))
    n = int(input('Power of Element: '))

    print(Power_Of_Element(base, n))


main()