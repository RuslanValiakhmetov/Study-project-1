import re
import sys
from calculator import Calculator


def user_input_value():
    binary_regex = r"^[0|1]+$"
    while True:
        user_input = input("Please, input binary value(big-endian): ")
        if re.search(binary_regex, user_input):
            decimal_side_length = Calculator.binary_to_integer(user_input)
            break
        else:
            print("Value is wrong, try again!")

    return decimal_side_length


def main():
    # Этот комментарий для IDE
    # noinspection PyBroadException
    try:
        calculator = Calculator(user_input_value())
        while True:
            user_input = input("\nPlease, make your choice: 'c'alculate, 's'ave, "
                               "'r'estore, 'v'iew, 'u'pdate values, 'q'uit: ")
            if user_input == 'c':
                calculator.calculate_sum_area()
            elif user_input == 's':
                calculator.save()
            elif user_input == 'r':
                calculator.restore()
            elif user_input == 'v':
                calculator.show()
            elif user_input == 'u':
                calculator.update_figures(user_input_value())
            elif user_input == 'q':
                break
            else:
                print("Invalid input, try again!")
    except Exception as exp:
        print("An exception occurred, message: %s" % exp)


if __name__ == '__main__':
    sys.exit(main())
