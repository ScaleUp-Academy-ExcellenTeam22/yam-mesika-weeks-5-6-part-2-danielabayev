import time
from typing import IO


def fast_and_reliable(file: IO[str]):
    """
    This function receive file to read and read all the words in it to list and set, then check the average time take
    to find the word in the list/set.
    :param file: The file to read from.
    """
    words_list, words_set = [], set
    data = file.read()
    words_list = data.split()
    words_set = set(words_list)
    print("search in set take " + average_runtime(words_set).__str__())
    print("search in list take " + average_runtime(words_list).__str__())


def average_runtime(list_or_set: list / set) -> float:
    """
    This function receive list or set of words, then check the average time take to find the word zwitterion in the
    set/list.
    :param list_or_set: List or set of words to search in.
    :return: The time it take to search in the data structure in average.
    """
    sum_time = 0
    for check_number in range(1000):
        start = time.time()
        "zwitterion" in list_or_set
        end = time.time()
        sum_time += end - start
    return sum_time / 1000


if __name__ == "__main__":
    file_name = open("words.txt", "r")
    fast_and_reliable(file_name)
