def is_isogram(input_str):
    # Convert the input string to lowercase
    input_str = input_str.lower()

    # Create an empty set to store seen characters
    seen = set()

    for char in input_str:
        # If the character is not alphabetic, ignore it
        if not char.isalpha():
            continue

        # If the character is already seen, it's not an isogram
        if char in seen:
            return False

        # Add the character to the set
        seen.add(char)

    # If all characters are unique, it's an isogram
    return True

# Test the function
input_str = input()
result = is_isogram(input_str)
print(result)
