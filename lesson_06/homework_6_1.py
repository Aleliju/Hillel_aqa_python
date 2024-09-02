var_string = input("Enter a symbols: ")

unique_symbols = set(var_string)

if len(unique_symbols) > 10:
    print(True)
else:
    print(False)