def count_length_without_spaces(s):
    # Remove spaces from the string
    s_without_spaces = s.replace(" ", "")

    # Count the length of the string without spaces
    length_without_spaces = len(s_without_spaces)

    return length_without_spaces

# Example usage
s = input()

length = count_length_without_spaces(s)
print(length)
