def sum_of_all_numbers(list_of_numbers):
    """Processes a list of strings containing numbers separated by commas,
    converts them to integers, and calculates the sum of the numbers in each string with check for except.

   Args:
       list_of_numbers:   (list)   A list of strings, where each string contains numbers separated by commas.

   Returns:
        None: The function prints the intermediate steps, and the final result or an error message.
   """
    try:
        split_string = [e.split(',') for e in list_of_numbers]
        print(split_string)
        list_int = [list(map(int, i)) for i in split_string]
        print(list_int)
        sums = [sum(i) for i in list_int]
        print(sums)
    except ValueError as e:
        print(f"Can't do it!: {e}")
    else:
        print(f"Результат: {sums}")

enter_data = ['1,2,3,4', '1,2,3,4,50', '1,2,3']
sum_of_all_numbers(enter_data)

#prints for check

