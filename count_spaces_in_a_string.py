def count_spaces(s):
    space_count = 0
    for char in s:
        if char == ' ':
            space_count += 1
    return space_count

# Example usage
s = input()
space_count = count_spaces(s)
print(space_count)
