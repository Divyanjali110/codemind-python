def count_lowercase_letters(s):
    lowercase_count = 0

    # Iterate through each character in the string
    for char in s:
        # Check if the character is a lowercase letter
        if char.islower():
            lowercase_count += 1

    return lowercase_count

# Example usage
s = input()
lowercase_count = count_lowercase_letters(s)
print(lowercase_count)
