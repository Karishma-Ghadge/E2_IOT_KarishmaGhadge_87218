def find_largest_number():
    
    input_values = input("Enter numbers separated by space : ")
    
    numbers = [int(num) for num in input_values.split()]
    
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    # Display the largest number
    print("The largest number in the list is : ", largest)

# Call the function
find_largest_number()