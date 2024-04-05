#!/usr/bin/env python3
""" LRU Caching
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU Cache class

    Attributes:
        queue (list): A list to keep track of the order of keys in the cache.

    Methods:
        __init__(): Initializes the LRU Cache.
        put(key, item): Adds an item to the cache.
        get(key): Retrieves an item from the cache by key.
    """

    def __init__(self):
        """ Initialize LRU Cache
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache

        Args:
            key: The key of the item to be added.
            item: The item to be added to the cache.
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.queue.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.cache_data[key] = item
            self.queue.append(key)
            if key in self.queue:
                self.queue.remove(key)
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key

        Args:
            key: The key of the item to be retrieved.

        Returns:
            The item associated with the given key,
            or None if the key is not found in the cache.
        """
        if key in self.queue:
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data.get(key, None)
