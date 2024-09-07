# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier < 6:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            print('Sum more than 25')
            pass
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

print("-" * 100)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_two_numbers(a, b):
    return a + b
print(sum_of_two_numbers(2, 2))

print("-" * 100)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def list_avarage(number):
    if len(number) == 0:
        return None
    return sum(number) / len(number)
list_number = [1, 2, 3, 4, 5]
print(list_avarage(list_number))

print("-" * 100)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def revers_row(row):
    return ''.join(reversed(row))

var_row = "Написати функцію, яка приймає рядок та повертає його у зворотному порядку"
print(revers_row(var_row))

print("-" * 100)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(word_list):
    return max(word_list, key=len)

random_words = ['Написати', 'функцію', 'яка', 'приймає']
print(longest_word(random_words))

print("-" * 100)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        return str1.index(str2)
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

print("-" * 100)

# task 7
def word_with_letter_h(input_word):
    """Check enter name contain letter H.
    
    Args: 
        input_word:   (str)   The word entered by the user

    Returns:
        None: Prints a message indicating whether the letter 'H' is present in the input word
    """

    var_word_upper = input_word.upper()
    
    if 'H' in var_word_upper:
        print(f"You enter a {input_word} with letter H")
    else:
        print(f"You enter a {input_word} without letter H")

user_input = input("Enter a word with letter H: ").strip()
word_with_letter_h(user_input)

print("-" * 100)

# task 8
def sum_unique_symbols_more_10(var_string):
    """Check if the input string contains more than 10 unique symbols.

    Args:
        var_string:   (str)   The string to be checked for unique symbols

    Returns:
        bool: True if input word contains more than 10 unique symbols and False otherwise
    """
    unique_symbols = set(var_string)

    if len(unique_symbols) > 10:
        print(True)
    else:
        print(False)

user_input_unique_symbol = input("Enter a symbols: ")
sum_unique_symbols_more_10(user_input_unique_symbol)

print("-" * 100)

# task 9
def string_list_sort(input_list):
    """Filter and return a list containing only string elements from the input list.

    Args:
        input_list:   (list)   The list from which to filter out string elements.

    Returns:
        list: A list containing only the string elements from the input_list.
    """
    string_list = [i for i in input_list if isinstance(i, str)]
    return string_list

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print("String value:", string_list_sort(lst1))


print("-" * 100)

# task 10
def sum_of_pair_numbers(input_numbers):
    """Calculate the sum of all even numbers in the given list.

    Args:
        input_numbers:   (list of int)   The list from which we count the sum of pair numbers.

    Returns:
        int: A sum of all even numbers in the list.
    """
    amount_pair_numbers = sum(x for x in input_numbers if x % 2 == 0)
    return amount_pair_numbers

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Amount of pair numbers:", sum_of_pair_numbers(lst1))

print("-" * 100)

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""