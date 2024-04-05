#!/usr/bin/env python3
""" Basic dictionary

This module contains the BasicCache class,
which represents a basic cache implementation.
It inherits from the BaseCaching class.

Attributes:
    cache_data (dict): A dictionary to store the cached items.

Methods:
    put(key, item): Add an item to the cache.
    get(key): Retrieve an item from the cache.

"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class represents a basic cache implementation.

    Attributes:
        cache_data (dict): A dictionary to store the cached items.

    Methods:
        put(key, item): Add an item to the cache.
        get(key): Retrieve an item from the cache.

    """
    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (str): The key to associate with the item.
            item (Any): The item to be added to the cache.

        Returns:
            None

        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key associated with the item.

        Returns:
            Any: The item associated with the key, or None if not found.

        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
