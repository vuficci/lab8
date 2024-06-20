def reverse_number(number):
    """
    Reverses the digits of a given number.
    
    Args:
    number (int): The number to be reversed.
    
    Returns:
    int: The reversed number.
    """
    return int(str(number)[::-1])


def is_palindrome(number):
    """
    Checks if a number is a palindrome.
    
    Args:
    number (int): The number to be checked.
    
    Returns:
    bool: True if the number is a palindrome, False otherwise.
    """
    return str(number) == str(number)[::-1]


def process_numbers(numbers):
    """
    Processes a list of numbers by reversing each number and printing the reversed number.
    If a number is a palindrome, it also prints a message indicating that.
    
    Args:
    numbers (list): A list of numbers to be processed.
    """
    reversed_numbers = []
    for num in numbers:
        reversed_num = reverse_number(num)
        reversed_numbers.append(reversed_num)
        
        if is_palindrome(num):
            print(f"{num} is a palindrome!")
    
    print("Reversed numbers:", reversed_numbers)


# Ввод чисел с клавиатуры
numbers = []
while True:
    num = input("Enter a number (or 'done' to finish): ")
    if num.lower() == 'done':
        break
    try:
        num = int(num)
        numbers.append(num)
    except ValueError:
        print("Please enter a valid number.")

# Обработка чисел
if numbers:
    process_numbers(numbers)
else:
    print("No numbers were provided.")