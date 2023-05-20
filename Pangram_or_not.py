import string

def is_pangram(input_string):
    # Create a set of lowercase alphabets
    alphabet_set = set(string.ascii_lowercase)

    # Convert the input string to lowercase and remove spaces
    input_string = input_string.lower().replace(" ", "")

    # Convert the input string to a set of characters
    input_set = set(input_string)

    # Check if the input set is equal to the alphabet set
    return input_set == alphabet_set

# Test the function
input_str = input()
is_pangram_result = is_pangram(input_str)

print(is_pangram_result)
