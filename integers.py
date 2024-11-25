
def get_positive_numbers(numbers):
    return [num for num in numbers if num > 0]
numbers = [10, -5, 23, -1, 0, 34, -8, 50]
positive_numbers = get_positive_numbers(numbers)
print(f"Positive numbers from the list: {positive_numbers}")


