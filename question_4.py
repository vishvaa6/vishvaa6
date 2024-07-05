def sum_first_last(number):
    number_str = str(number)
    first_digit = int(number_str[0])
    last_digit = int(number_str[-1])
    return first_digit + last_digit

integer_value = input("Enter any digit number: ")
print(f"The sum of the first and last digit of {integer_value} is {sum_first_last(integer_value)}")
