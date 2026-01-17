def validate_isbn(isbn, length=None):
    if length is None:
        return

    # Check if length is numeric and convert if needed
    if not isinstance(length, int):
        print("Length must be a number.")
        return

    # Check if length is valid (10 or 13)
    if length not in [10, 13]:
        print("Length should be 10 or 13.")
        return

    # Check for invalid characters
    if length == 10 and not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X')):
        print("Invalid character was found.")
        return
    elif length == 13 and not isbn.isdigit():
        print("Invalid character was found.")
        return

    #  Check if ISBN length matches given length
    if len(isbn) != length:
        print(f"ISBN-{length} code should be {length} digits long.")
        return

    # Split main digits and check digit
    main_digits = isbn[:length - 1]
    given_check_digit = isbn[-1]  # string, handles 'X'

    # Convert main digits to integers
    main_digits_list = [int(d) for d in main_digits]

    # Calculate expected check digit
    if length == 10:
        total = sum(digit * (10 - i) for i, digit in enumerate(main_digits_list))
        result = 11 - (total % 11)
        if result == 11:
            expected_check_digit = '0'
        elif result == 10:
            expected_check_digit = 'X'
        else:
            expected_check_digit = str(result)
    else:  # ISBN-13
        total = sum(digit if i % 2 == 0 else digit * 3 for i, digit in enumerate(main_digits_list))
        result = 10 - (total % 10)
        if result == 10:
            expected_check_digit = '0'
        else:
            expected_check_digit = str(result)

    # Compare check digit
    if given_check_digit == expected_check_digit:
        print("Valid ISBN Code.")
    else:
        print("Invalid ISBN Code.")


# ----------------- Main Function -----------------

def main():
    user_input = input("Enter ISBN and length: ")

    # Check for comma-separated values
    if ',' not in user_input:
        print("Enter comma-separated values.")
        return

    isbn, length = user_input.split(',', 1)
    isbn = isbn.strip()
    length = length.strip()

    # Check if length is numeric
    if not length.isdigit():
        print("Length must be a number.")
        return

    # Convert length to integer and call validator
    validate_isbn(isbn, int(length))


# main()

validate_isbn("1530051126", 10)
validate_isbn("9781530051120", 13)
validate_isbn("1530051125", 10)
validate_isbn("15-0051126", 10)
validate_isbn("1530051125", "A")
validate_isbn("1530051125")
validate_isbn("080442957X", 10)
validate_isbn("9781947172104", 13)


