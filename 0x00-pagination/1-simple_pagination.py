import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple containing the start and end indexes for the given page.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indexes for
        the given page.
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get the requested page from the dataset.

        Args:
            page (int, optional): The page number. Defaults to 1.
            page_size (int, optional): The number of items per page.
                Defaults to 10.

        Returns:
            List[List]: The requested page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
