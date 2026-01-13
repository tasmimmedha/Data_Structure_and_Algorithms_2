def process_string_recursive(s, index=0):
    # Base case: if the index reaches the end of the string
    if index == len(s):
        return

    # Current character
    ch = s[index]

    # Process the rest of the string recursively
    rest = process_string_recursive(s, index + 1)

    # If current character is not a whitespace, convert to lowercase and include it
    if ch != " ":
        return ch.lower() + rest
    else:
        return rest


def main():
    user_input = input("Enter a string: ")
    result = process_string_recursive(user_input)
    print("Processed string:", result)


main()
