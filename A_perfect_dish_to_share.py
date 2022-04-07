from collections import Generator


def a_perfect_dish_to_share() -> Generator[int]:
    """
    This generator generate all the perfect number - numbers equal to the sum of their dividers.
    :return: The next perfect number.
    """
    checked_number = 2
    while True:
        if is_perfect(checked_number):
            yield checked_number
        checked_number += 1


def is_perfect(number_to_check: int) -> int:
    """
    This function taken from the site:
    https://www.geeksforgeeks.org/perfect-number/
    This function check if number is perfect number.
    :param number_to_check: The number to check.
    :return: True if the number is perfect number.
    """
    dividers_sum = 1

    # Find all divisors and add them
    divider = 2
    while divider * divider <= number_to_check:
        if number_to_check % divider == 0:
            dividers_sum = dividers_sum + divider + number_to_check / divider
        divider += 1

    return True if dividers_sum == number_to_check else False


if __name__ == "__main__":
    generator = a_perfect_dish_to_share()
    while True:
        print(next(generator))
