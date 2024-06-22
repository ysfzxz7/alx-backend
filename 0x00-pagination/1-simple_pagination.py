#!/usr/bin/env python3
"""
    Module of simple pagination
"""
import csv
import math
from typing import List


class Server:
    """
        Server class to paginate a database of popular baby names.
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

    def index_range(self, page: int, page_size: int) -> tuple:
        """
            Function that returns a tupe contains
            data that should be returned
        """
        res = ((page - 1) * page_size, page * page_size)
        return res

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            Function that returns the appropriated pages
        """
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0

        bounds = self.index_range(page, page_size)
        result = []
        with open(self.DATA_FILE, 'r') as reader:
            page = 0
            # ignore the first line of headings
            reader.readline()
            # read the second line
            line = reader.readline()
            while page < bounds[1] and line:
                if page >= bounds[0]:
                    info = line.split(',')
                    info[-1] = info[-1].replace('\n', '')
                    result.append(info)
                page += 1
                line = reader.readline()
            return result
