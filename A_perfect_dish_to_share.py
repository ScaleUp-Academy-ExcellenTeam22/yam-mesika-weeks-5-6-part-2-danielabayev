def a_perfect_dish_to_share():
    checked_number = 2
    while True:
        if is_perfect(checked_number):
            yield checked_number
        checked_number += 1


def is_perfect(number_to_check):
    # To store sum of divisors
    dividers_sum = 1

    # Find all divisors and add them
    divider = 2
    while divider * divider <= number_to_check:
        if number_to_check % divider == 0:
            dividers_sum = dividers_sum + divider + number_to_check / divider
        divider += 1

    # If sum of divisors is equal to
    # n, then n is a perfect number
    return True if dividers_sum == number_to_check else False


if __name__ == "__main__":
    generator = a_perfect_dish_to_share()
    while True:
        print(next(generator))
