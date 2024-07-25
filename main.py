def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def sum_of_list(numbers):
    return sum(numbers)

# Get user input for factorial calculation
number = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {number} is {factorial(number)}")

# Get user input for list sum calculation
#list_of_numbers = list(map(int, input("Enter a list of numbers separated by spaces to calculate their sum: ").split()))
#print(f"The sum of the list {list_of_numbers} is {sum_of_list(list_of_numbers)}")
