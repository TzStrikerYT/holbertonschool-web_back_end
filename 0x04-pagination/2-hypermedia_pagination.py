#!/usr/bin/env python3
""" pagination project"""

from typing import Tuple, List, Dict, Any
import csv
import math


index_range = __import__("0-simple_helper_function").index_range


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
        """ Return the elements with a pagination order """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        start, end = index_range(page, page_size)
        res_list = []

        if start >= len(self.dataset()):
            return res_list
        res_list = self.dataset()
        return res_list[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """ Returns a object """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        total_pages = int(len(self.dataset()) / page_size)
        next_page = page + 1 if (page + 1) < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
