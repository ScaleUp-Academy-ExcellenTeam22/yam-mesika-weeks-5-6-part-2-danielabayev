def interleave_function(*args: list[list[any]]) -> list[str]:
    """
    This function taken from the site:
    https://stackoverflow.com/questions/7946798/interleave-multiple-lists-of-the-same-length-in-python
    It receive a list of list from the same size and make them list of the items intertwined.
    If the lists are not of the same size it take the shortest length and intertwined them according to the shortest.
    :param args: The list of lists.
    :return: The new list combined the lists.
    """
    new_list = [val for lst in zip(*args) for val in lst]
    return new_list


def interleave_generator(*args: list[list[any]]) -> list[str]:
    """
    This generator taken from the site:
    https://stackoverflow.com/questions/7946798/interleave-multiple-lists-of-the-same-length-in-python
    It receive a list of list from the same size and make them list of the items intertwined.
    If the lists are not of the same size it take the shortest length and intertwined them according to the shortest.
    :param args: The list of lists.
    :return: The new list combined the lists.
    """
    new_list = [val for lst in zip(*args) for val in lst]
    yield new_list


if __name__ == "__main__":
    print(interleave_function('abc', [1, 2, 3], ('!', '@', '#')))
