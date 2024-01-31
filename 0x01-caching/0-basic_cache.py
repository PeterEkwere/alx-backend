#!/usr/bin/env python3
"""
    This Module contains the BasicCache thats a caching system
    Author: Peter Ekwere
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic cache system
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ updates cache_data with the key and item

        Args:
            key (_type_): cache key
            item (_type_): cache value
        """
        if item is not None and key is not None:
            self.cache_data.setdefault(key, item)

    def get(self, key):
        """ Return  the data from the cache

        Args:
            key (str): key for data
        """
        if key is None:
            return None

        result = self.cache_data.get(key)
        if result is None:
            return None
        return result
