while True:
    var_word = input("Enter a word with letter H: ").strip()
    var_word_upper = var_word.upper()

    if 'H' in var_word_upper:
        print(f"You enter a {var_word} with letter H")
        break
    else:
        print(f"You enter a {var_word} without letter H")

