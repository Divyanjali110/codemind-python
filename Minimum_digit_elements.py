def count_elements_with_minimum_digits(arr):
    min_digits = float('inf')  
    count = 0  

    for num in arr:
        num_digits = len(str(num)) 
        if num_digits < min_digits:
            min_digits = num_digits  
            count = 1  
        elif num_digits == min_digits:
            count += 1 

    return count


n = int(input())
arr = list(map(int, input().split()))

# Call the function and display the count of elements with minimum digits
result = count_elements_with_minimum_digits(arr)
print(result)
