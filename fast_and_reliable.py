import time
from typing import IO


def fast_and_reliable(file: IO[str]):
    """
    This function receives a file to read, and reads all of the words from inside it into a list and into a set.
    Then, it checks the average time it takes to find a given word in the list/set.
    :param file: The file to read from.
    """
    words_list, words_set = [], set
    data = file.read()
    words_list = data.split()
    words_set = set(words_list)
    print("A search in set takes " + average_runtime(words_set).__str__())
    print("A search in list takes " + average_runtime(words_list).__str__())


def average_runtime(list_or_set: list / set) -> float:
    """
    This function receives list or set of words, then checks the average time it takes to find the word zwitterion in
    the set/list.
    :param list_or_set: List or set of words to search in.
    :return: The time it takes to search in the data structure in average.
    """
    sum_time = 0
    for check_number in range(1000):
        time_before_start_find = time.time()
        "zwitterion" in list_or_set
        time_after_end_find = time.time()
        sum_time += time_after_end_find - time_before_start_find
    return sum_time / 1000


if __name__ == "__main__":
    file_name = open("words.txt", "r")
    fast_and_reliable(file_name)
