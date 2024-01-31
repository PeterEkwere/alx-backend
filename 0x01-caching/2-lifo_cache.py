#!/usr/bin/env python3
"""
    This Module contains the LIFOCache thats a caching system
    Author: Peter Ekwere
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ FIFOCache system
    """

    def __init__(self):
        self.updated_key = ""
        super().__init__()

    def put(self, key, item):
        """ updates cache_data with the key and item

        Args:
            key (_type_): cache key
            item (_type_): cache value
        """
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.updated_key = key
            else:
                last_item = next(reversed(self.cache_data))
                if self.updated_key != "":
                    del self.cache_data[self.updated_key]
                    print(f"DISCARD: {self.updated_key}")
                else:
                    del self.cache_data[last_item]
                    print(f"DISCARD: {last_item}")
                    return last_item

        if item is not None and key is not None:
            self.cache_data.setdefault(key, item)
            self.updated_key = key

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
