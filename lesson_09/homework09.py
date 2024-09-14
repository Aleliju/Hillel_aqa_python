def word_with_letter_h(input_word):
    """Check enter name contain letter H.

    Args:
        input_word:   (str)   The word entered by the user

    Returns:
        None: Prints a message indicating whether the letter 'H' is present in the input word
    """

    var_word_upper = input_word.upper()

    if 'H' in var_word_upper:
        return True
    else:
        return False


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


if __name__ == "__main__":
    user_input_unique_symbol = input("Enter a symbols: ")
    sum_unique_symbols_more_10(user_input_unique_symbol)


def string_list_sort(input_list):
    """Filter and return a list containing only string elements from the input list.

    Args:
        input_list:   (list)   The list from which to filter out string elements.

    Returns:
        list: A list containing only the string elements from the input_list.
    """
    string_list = [i for i in input_list if isinstance(i, str)]
    return string_list


def sum_of_pair_numbers(input_numbers):
    """Calculate the sum of all even numbers in the given list.

    Args:
        input_numbers:   (list of int)   The list from which we count the sum of pair numbers.

    Returns:
        int: A sum of all even numbers in the list.
    """
    amount_pair_numbers = sum(x for x in input_numbers if x % 2 == 0)
    return amount_pair_numbers


def find_substring(str1, str2):
    if str2 in str1:
        return str1.index(str2)
    else:
        return False


def sum_of_all_numbers(list_of_numbers):
    """Processes a list of strings containing numbers separated by commas,
    converts them to integers, and calculates the sum of the numbers in each string with check for except.

   Args:
       list_of_numbers:   (list)   A list of strings, where each string contains numbers separated by commas.

   Returns:
        None: The function prints the intermediate steps, and the final result or an error message.
   """
    result_sums = []
    for string in list_of_numbers:
        try:
            split_string = string.split(',')
            list_int = list(map(int, split_string))
            total_sums = sum(list_int)
            result_sums.append(total_sums)
        except ValueError as e:
            print(f"Can't do it for '{string}': {e}")
            return None
    return result_sums
