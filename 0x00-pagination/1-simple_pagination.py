#!/usr/bin/env python3
"""
    Module contains a Class
    Author: Peter Ekwere
"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple:
    """
    This Function return a tuple of size two
    containing a start index and end index
    corresponding to the range of indexes
    """
    end_index = page_size * page
    start_index = end_index - page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        returns a page
        """
        assert isinstance(
            page, int) and page > 0, "'page' must be  greater than 0"
        assert isinstance(
            page_size, int) and page_size > 0, "'page_size'  than 0"

        try:
            _range = index_range(page, page_size)
            data = Server.dataset(self)
            new_data = []
            range_start = _range[0]
            range_end = _range[1]
            for index in range(range_start, min(range_end, len(data))):
                new_data.append(data[index])
            return new_data
        except AssertionError as e:
            print("Error:", e)
