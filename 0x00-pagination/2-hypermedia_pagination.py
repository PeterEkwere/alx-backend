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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        returns a dictionary
        """
        _range = index_range(page, page_size)
        data = Server.get_page(self, page, page_size)
        full_data = Server.dataset(self)
        next_page = page + 1 if len(full_data) > _range[1] else None
        previous_page = page - 1 if page > 1 else None
        total_pages = math.ceil(len(full_data) / page_size)

        hyper_data = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": previous_page,
            "total_pages": total_pages
        }
        return hyper_data
