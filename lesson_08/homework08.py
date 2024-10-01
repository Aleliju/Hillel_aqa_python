def sum_of_all_numbers(list_of_numbers):
    """Processes a list of strings containing numbers separated by commas,
    converts them to integers, and calculates the sum of the numbers in each string with check for except.

   Args:
       list_of_numbers:   (list)   A list of strings, where each string contains numbers separated by commas.

   Returns:
        None: The function prints the intermediate steps, and the final result or an error message.
   """
    for string in list_of_numbers:
        try:
            split_string = string.split(',')
            list_int = list(map(int, split_string))
            total_sums = sum(list_int)
            print(f"Sum of '{string}': {total_sums}")
        except ValueError as e:
            print(f"Can't do it for '{string}': {e}")


enter_data = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']
sum_of_all_numbers(enter_data)

